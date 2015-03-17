# max_poolとnum_init_childrenについて

pgpool-IIからのPostgreSQLへの接続数を決定する設定値には、**max_pool**と**num_init_children**がある。

[max_poolの説明](http://pgpool.projects.postgresql.org/pgpool-II/doc/pgpool-ja.html#connection_pool_mode)を読むと
>pgpool-IIは、ユーザ名、データベースが同じならばコネクションを 再利用しますが、そうでなければ新たにPostgreSQLへのコネクションを確 立しようとします。したがって、ここでは想定される[ユーザ名:データベー ス名]のペアの種類の数だけをmax_poolに指定しておく必要があります。

つまりpgpoolを介しての接続が同ユーザ、同DBであるならばmax_poolは1でいいということになる。

次に[num_init_children](http://pgpool.projects.postgresql.org/pgpool-II/doc/pgpool-ja.html#common)の説明を読む。
>pgpool-IIに対してクライアントが同時に接続できる上限の数になります。

とあることから、クライアントからの想定接続数をnum_init_childrenに設定する必要がある。

また、複数のユーザ複数のDBを使う場合はmax_poolをパターン数分に設定する。
fooユーザがhoge DBに接続し、barユーザでfuga DBに接続するという2パターンの場合はmax_pool = 2となる。


## PostgreSQLの接続数

PostgreSQLのmax_connectionsを求める式は以下の通り。
```
(max_pool * num_init_children) + superuser_reserved_connections + wal_senders
```
