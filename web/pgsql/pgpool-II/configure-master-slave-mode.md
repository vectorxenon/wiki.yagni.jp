# pgpool-IIのマスタースレーブモードの設定

## pgpool.confの設定変更箇所

```
load_balance_mode = true

master_slave_mode = true
master_slave_sub_mode = 'stream'
health_check_user = 'health_check'
```

## MD5による認証

マスタースレーブモードにおいてmd5による認証を実現するにはpool_passwdというファイルを作り、そこに`ユーザ名:md5ハッシュ`という形式で登録することで利用できるようになる。

やり方は[ユーザマニュアル](http://pgpool.projects.postgresql.org/pgpool-II/doc/pgpool-ja.html#md5)にある通り

  1. `pg_md5 --md5auth -p`を実行。
     $PGPOOL_HOME/etcにpool_passwdというファイルが作成される。
  2. pool_hba.confにmd5認証のエントリを作成。
  3. pg_hba.confで該当ユーザの認証をmd5以外の認証に変更する。
