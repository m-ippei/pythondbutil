# pythondbutil

PythonのSQLiteの操作を簡単にするためのライブラリ

## シェルコマンド一覧
#### インストール
```console
python -m pip install git+https://github.com/m-ippei/pythondbutil.git
```
#### アップデート
```console
python -m pip install git+https://github.com/m-ippei/pythondbutil.git
```
#### アンインストール
```console
python -m pip uninstall pythondbutil
```

### 使い方

```Python
from pythondbutil import DBM,DBT,DBUtil

# DB操作通常版
with DBM("tmp.db") as dbm:
    dbm.exec("DROP TABLE IF EXISTS items")

# DB操作トランザクション版
with DBT("tmp.db") as dbt:
    dbt.add("INSERT INTO items(item_id,name) VALUES(1,'firstitem')")

# dbへのパスとCREATE文が入ったSQLファイルのディレクトリを設定
dbu = DBUtil("tmp.db",r"./path/to/create_table_sql_dirctory")

# データベースの初期化
dbu.initTable()

# INSERT INTO users(user_id,user_nam) VALUES(1,'abc')
dbu.insert_dict("users",{
    "user_id":1,
    "user_name":"abc"
})

```