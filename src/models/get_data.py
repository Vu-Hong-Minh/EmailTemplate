from src.models.connection_db import conn_SQL

class GetData:
    # Hàm lấy 1 bản ghi
    def __init__(self, sql):
        self.sql = sql

    def get_data(self):
        try:
            conn = conn_SQL()
            mydb = conn.connection_db()
            cur = mydb.cursor()
            cur.execute(self.sql)
            row = cur.fetchone()
            return row

        finally:
            # Đóng kết nối (Close connection).
            cur.close()
            mydb.close()

    #Hàm lấy nhiều bản ghi
    def get_data_list(self):
        try:
            conn = conn_SQL()
            mydb = conn.connection_db()
            cur = mydb.cursor()
            cur.execute(self.sql)
            row = cur.fetchall()
            return row

        finally:
            # Đóng kết nối (Close connection).
            cur.close()
            mydb.close()

    #Hàm Update dữ liệu
    def update_data(self):
        try:
            conn = conn_SQL()
            mydb = conn.connection_db()
            cur = mydb.cursor()
            cur.execute(self.sql)
            mydb.commit()

        finally:
            # Đóng kết nối (Close connection).
            cur.close()
            mydb.close()