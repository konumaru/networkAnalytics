# postgreSQLコマンド集

- バージョン確認
```
$ psql --version
```

- Postgresqlの起動
```
$ postgres -D /usr/local/var/postgres
```

- Postgresqlの停止
```
$ pkill postgres
```

- データベース一覧表示
```
$ psql -l
```

- データベースの削除
```
# drop database <DATABASE_NAME>;
```

- ユーザー一覧表示
```
# select * from pg_user;
```


## データベースを作ってPosticoで繋げるまで。
- ユーザーの作成
```
$ createuser -P <user-name>
```

- データベースの作成
```
$ createdb <db-name> -O <user-name>
```

以上をやればposticoで接続できる。


- データベースに接続
```
$ psql -U <user-name> <db-name>
```
