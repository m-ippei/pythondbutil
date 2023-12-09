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
from pythondbutil import DBM,DBT

# DB操作通常版
with DBM("test.db") as dbm:
    dbm.exec("DROP TABLE IF EXISTS items")

# DB操作トランザクション版
with DBT("test.db") as dbt:
    dbt.add("INSERT INTO items(item_id,name) VALUES(1,'firstitem')")
```