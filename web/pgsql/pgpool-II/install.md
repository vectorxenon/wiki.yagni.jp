# pgpool-IIのインストール

## コンパイル

```bash
tar jxf pgpool-II-3.4.1.tar.bz2
cd pgpool-II-3.4.1
./configure --prefix=/usr/local/pgpool/3.4.1 --with-pgsql=/usr/local/pgsql/9.4.1 --with-openssl --with-pam
make -j2
sudo make install
```


## 管理ユーザの作成

```bash
useradd postgres && chown -R postgres:postgres /usr/local/pgpool/current
```


## システムDBの作成

```bash
createdb -U pgpool -h dbhost -p 5432 -E UTF-8 pgpool
psql -U pgpool -h dbhost -p 5432 pgpool < pgpool-II-3.4.1/src/sql/system_db.sql
```

## 起動ファイルの編集

### /etc/init.d/pgpool

```bash
PGPOOLHOME=/path/to/pgpool
PGPOOLDAEMON=$PGPOOLHOME/bin/pgpool
PGPOOLCONF=$PGPOOLHOME/etc/pgpool.conf
PGPOOLPIDDIR=/var/run
PGPOOLLOG=/var/log/pgpool/pgpool.log

stop(){
  echo -n $"Stopping ${NAME} service: "
  if [ $UID -ne 0 ]; then
    RETVAL=1
    failure
  else
    $PGPOOLDAEMON stop >> "$PGPOOLLOG" 2>&1 < /dev/null
    RETVAL=$?
    if [ $RETVAL -eq 0 ]; then
      rm -f /var/lock/subsys/${NAME}
      success
    else
      failure
    fi
  fi;
  echo
  return $RETVAL
}
```

## 設定ファイルの設置

```bash
cd /path/to/pgpool/etc
cp pcp.conf.sample pcp.conf
cp pgpool.conf.sample pgpool.conf
cp pool_hba.conf.sample pool_hba.conf
```

### pcp.conf

```bash
pg_md5 -p
  なんかパスワード
```

```
# IDは好きなものを
# PASSWORDは、さっきのコマンドで出力されたmd5ハッシュ
ID:PASSWORD
```

### pgpool.conf

```ini
listen_addresses = 'localhost'
port = 5432
num_init_children = 32
max_pool = 4
logdir = '/var/log/pgpool'
pid_file_name = '/var/run/pgpool.pid'
insert_lock = false

system_db_hostname = 'dbhost1'
system_db_port = 5432
system_db_dbname = 'pgpool'
system_db_schema = 'pgpool_catalog'
system_db_user = 'pgpool'
system_db_password = 'パスワード'

backend_hostname0 = 'dbhost2'
backend_port0 = 5432
backend_weight0 = 1
backend_data_directory0 = ''

recovery_user = 'pgpool_recover'
recovery_password = 'パスワード'
```

## RPMでのインストール

RPMでインストールしたい場合は、[公式リポジトリ](http://www.pgpool.net/mediawiki/index.php/Downloads#Direct_RPM_download)が提供されているので、そちらを利用する。
