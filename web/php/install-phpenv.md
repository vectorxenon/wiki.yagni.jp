# phpenvで複数のPHPのバージョンを利用する

## phpenvのインストール

```bash
git clone https://github.com/phpenv/phpenv.git ~/.phpenv
```

次にPATHを通す。
bashならbash_profileに、zshならzshenvに追記する。

```bash
# phpenv
export PHPENV_ROOT="${HOME}/.phpenv"
if [ -d "${PHPENV_ROOT}" ]; then
    export PATH="${PHPENV_ROOT}/bin:${PATH}"
    eval "$(phpenv init -)"
fi
```

## 使い方の簡単な説明

### PHPのソースの取得

```bash
phpenv install --releases
```

### インストール

```bash
phpenv install php-5.6.6
```

### 利用するバージョンの切り替え

```bash
phpenv global 5.6.6
```

### ローカルのバージョンの指定

```bash
phpenv local 5.6.6
```
