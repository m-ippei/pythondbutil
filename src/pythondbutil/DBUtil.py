import os
from .dbm import DBM

class DBUtil:
    """DB操作クラス"""

    def __init__(self,dbPath,createTableSqlDirPath) -> None:
        """操作パスの設定

        Args:
            dbPath (str): データベースのファイルパス
            createTableSqlDirPath (str): テーブル作成用のディレクトリ
        """
        self.dbPath = dbPath
        self.createTableSqlDirPath = createTableSqlDirPath

    def __readSQL(self,path):
        """SQLファイルを文字列で読み込む
        """
        with open(path,mode='r',encoding='utf-8') as f:
            return f.read()

    def __createTable(self):
        """テーブル作成
        """
        with DBM(self.dbPath) as dbm:
            sql_list = [self.__readSQL(os.path.join(self.createTableSqlDirPath,path)) for path in os.listdir(self.createTableSqlDirPath)]
            for sql_str in sql_list:
                dbm.exec(sql_str)

    def _getInsertSqlStr_fromDicAndTableName(self,tableName,raw_data_dic):
        """テーブル名と辞書型データからINSERTのSQL文を作成

        Args:
            tableName (str): データベースのテーブル名
            raw_data_dic (dict): INSERTを実行する辞書型データ

        Returns:
            sql_text (str): SQL文
        """
    
        data_dic = {}

        for key,value in raw_data_dic.items():

            #valueがNoneのものは追加しない
            if value != None:
                data_dic[key] = value

        values = []

        for v in data_dic.values():

            #文字列は''をつけて数字等はそのまま
            if type(v) == str:
                values.append(f"'{v}'")
            else:
                values.append(str(v))

        return f"INSERT INTO {tableName}({','.join(data_dic.keys())}) VALUES({','.join(values)})"
    

    def initTable(self):
        """データベースの初期化
        """

        with DBM(self.dbPath) as dbm:
            dbm.exec("PRAGMA foreign_keys = false")
            for fileName in os.listdir(self.createTableSqlDirPath):
                tablename,_ = os.path.splitext(fileName)
                dbm.exec(f"DROP TABLE IF EXISTS {tablename}")
            dbm.exec("PRAGMA foreign_keys = true")
        
        self.__createTable()

    def insert_dict(self,tableName: str,data: dict):
        """テーブル名と辞書型データからINSERTを実行

        Args:
            tableName (str): データベースのテーブル名
            data (dict): INSERTする辞書型データ

        """
        with DBM(self.dbPath) as dbm:
            dbm.exec(self._getInsertSqlStr_fromDicAndTableName(tableName,data))

