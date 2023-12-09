import sqlite3

class DBT:
    """Sqliteのトランザクション付きDB操作クラス"""

    def __init__(self,dbPath):
        """
        Args:
            dbPath (str): 接続DBへのパス ./sample.db
        """
        self.dbPath = dbPath

    def add(self,sql: str):
        """実行するSQL文の追加

        Args:
            sql (str): sql文 
        """
        self.sqlstr_exec_list.append(sql)

    def _exec(self,sql):
        self.cursor.execute(sql)

    def __enter__(self):
        self.sqlstr_exec_list = []
        self.connection = sqlite3.connect(self.dbPath)
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exception_type,exception_value,traceback):
        self._exec("PRAGMA foreign_keys = true")

        last_sql = ""

        try:
            for sql in self.sqlstr_exec_list:
                last_sql = sql
                self.connection.execute(sql)
            
            self.connection.commit()

        except Exception as e:
            self.connection.rollback()
            print(f"error message :{e}")
            print(f"last sql: {last_sql}")

        self.cursor.close()
        self.connection.close()
