# PostgreSQLのレプリケーションの設定(ストリーミング＆ホットスタンバイ)

PostgreSQL9.0から使えるようになったストリーミングレプリケーションを利用してレプリケーションを構築する。

バージョンは9.4.1
DBは下記のようにinitdb済みとする

  * マスタ : /usr/local/pgsql/9.4.1/data/
  * スレーブ : /usr/local/pgsql/9.4.1/data_slave/


## マスタの設定

### WALの保存場所を作る

```bash
mkdir /usr/local/pgsql/9.4.1/master_archive
```

### postgresql.conf

```
listen_addresses = 'localhost'                # what IP address(es) to listen on;
port = 54321                          # (change requires restart)
max_connections = 50                  # (change requires restart)

password_encryption = on

shared_buffers = 32MB                 # min 128kB

wal_level = hot_standby                        # minimal, archive, or hot_standby
archive_mode = on             # allows archiving to be done
archive_command = 'cp -i %p /usr/local/pgsql/9.4.1/master_archive/%f < /dev/null'		# command to use to archive a logfile segment

max_wal_senders = 5           # max number of walsender processes
wal_sender_delay = 200ms      # walsender cycle time, 1-10000 milliseconds
wal_keep_segments = 64              # in logfile segments, 16MB each; 0 disables
vacuum_defer_cleanup_age = 0  # number of xacts by which cleanup is delayed

client_encoding = utf-8               # actually, defaults to database
```

### レプリケーション用のユーザの作成

```bash
/usr/local/pgsql/9.4.1/bin/pg_ctl -D /usr/local/pgsql/9.4.1/data start
/usr/local/pgsql/9.4.1/bin/createuser -s -h localhost -p 54321 -P -E -W pgrepl
```

### レプリケーションユーザの認証設定

md5に変更する

```
# pg_hba.conf
#
# TYPE  DATABASE      USER      CIDR-ADDRESS      METHOD
host    replication   pgrepl    127.0.0.1/32      md5
```

## スレーブの設定

### マスタのWALの保存場所を作る

```bash
mkdir /usr/local/pgsql/9.4.1/slave_archive
```

### マスタのベースバックアップからコピー

ベースバックアップを取得し展開

```bash
mv data_slave{,.bk}
pg_basebackup -U user -h host -D /path/to/data_slave -x -P
```

### postgresql.conf

```
listen_addresses = 'localhost'                # what IP address(es) to listen on;
port = 54321                          # (change requires restart)
max_connections = 50                  # (change requires restart)

password_encryption = on

shared_buffers = 32MB                 # min 128kB

wal_level = hot_standby                        # minimal, archive, or hot_standby
archive_mode = on             # allows archiving to be done
archive_command = 'cp -i %p /usr/local/pgsql/9.4.1/slave_archive/%f < /dev/null'		# command to use to archive a logfile segment

max_wal_senders = 5           # max number of walsender processes
wal_sender_delay = 200ms      # walsender cycle time, 1-10000 milliseconds
wal_keep_segments = 64              # in logfile segments, 16MB each; 0 disables

hot_standby = on			# "on" allows queries during recovery
max_standby_archive_delay = 30s	# max delay before canceling queries
max_standby_streaming_delay = 30s	# max delay before canceling queries

client_encoding = utf-8               # actually, defaults to database
```

### recovery.conf

サンプルファイルがあるので持ってくる

```bash
cp /usr/local/pgsql/9.4.1/share/recovery.conf.sample /usr/local/pgsql/9.4.1/data_slave/recovery.conf
```

```
restore_command = 'cp /usr/local/pgsql/9.4.1/slave_archive/%f %p'            # e.g. 'cp /mnt/server/archivedir/%f %p'
archive_cleanup_command = '/usr/local/pgsql/9.4.1/bin/pg_archivecleanup /usr/local/pgsql/9.4.1/default/slave_archive %r'
standby_mode = 'on'
primary_conninfo = 'host=127.0.0.1 port=54321 user=pgrepl password=pgrepl'            # e.g. 'host=localhost port=5432'
trigger_file = '/usr/local/pgsql/9.4.1/data_slave/trigger_file'
```

## 動作の確認

スレーブを起動したときに以下のようなメッセージが出ていれば、とりあえず起動は成功

```bash
pg_ctl -D /usr/local/pgsql/9.4.1/data_slave start

LOG:  consistent recovery state reached at 0/70002E0
LOG:  database system is ready to accept read only connections
LOG:  replication connection authorized: user=pgrepl host=127.0.0.1 port=55801
LOG:  streaming replication successfully connected to primary
```

## 参考

  * [第25章 高可用性、負荷分散およびレプリケーション - PostgreSQL 9.3.2文書](http://www.postgresql.jp/document/current/html/warm-standby.html)
  * [第24章 バックアップとリストア - PostgreSQL 9.3.2文書](http://www.postgresql.jp/document/current/html/continuous-archiving.html)
