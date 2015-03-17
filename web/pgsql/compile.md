# PostgreSQLのコンパイル

## コンパイル

```bash
sudo -s
cd /usr/local/src/pgsql
wget ftp://ftp2.jp.postgresql.org/pub/postgresql/source/v9.4.1/postgresql-9.4.1.tar.gz
tar zxf postgresql-9.4.1.tar.gz
cd postgresql-9.4.1
./configure --prefix=/usr/local/pgsql/9.4.1 --with-openssl --with-libxml --with-libxslt
make -j4
make install
```

## DBの初期化

```bash
chown -R postgres:postgres /usr/local/pgsql/9.4.1
sudo -u postgres /usr/local/pgsql/9.4.1/bin/initdb -E utf-8 -D /usr/local/pgsql/9.4.1/data --no-locale
```
