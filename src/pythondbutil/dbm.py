import sqlite3

class DBM:
    """SqliteのDB操作クラス"""

    def __init__(self,dbPath: str):
        """
        Args:
            dbPath (str): 接続DBへのパス ./sample.db
        """
        self.dbPath = dbPath

    def __open(self):
        self._connection = sqlite3.connect(self.dbPath)
        self._cursor = self._connection.cursor()
        self.exec("PRAGMA foreign_keys = true")

    def exec(self,sql: str):
        """SQL文の実行

        Args:
            sql (str): sql文 
        """
        self._cursor.execute(sql)

    def fetch_all(self,sql: str) -> list:
        """SQLで実行結果をすべてリストで取得
        """
        return self._cursor.execute(sql).fetchall()

    def fetch_one(self,sql: str) -> tuple:
        """SQLで実行結果をtupleひとつ取得
        """
        return self._cursor.execute(sql).fetchone()

    def fetch_one_first(self,sql: str):
        """SQLで実行結果のtupleの0番目を取得
        """
        return self._cursor.execute(sql).fetchone()[0]

    def getColumnNamesTuple(self,tableName: str) -> tuple:
        """テーブル名をタプルで取得

        Args:
            tableName (str): テーブル名
        """
        return tuple([v[1] for v in self._cursor.execute(f"PRAGMA table_info({tableName})").fetchall()])

    def __enter__(self):
        self.__open()
        return self
    
    def __exit__(self, exception_type,exception_value,traceback):
        self._connection.commit()
        self._cursor.close()
        self._connection.close()
