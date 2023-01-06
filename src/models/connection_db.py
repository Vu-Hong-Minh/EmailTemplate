import mysql.connector
# Kết nối tới MySQL.
class ConnSQL:
    def __init__(self, host, db, user, password):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=self.host, database=self.db, user=self.user, password=self.password)

    #Lấy 1 bản ghi
    def get_data(self, sql):
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            result = cur.fetchone()
            return result

        finally:
            # Đóng kết nối (Close connection).
            cur.close()
            self.connection.close()

    #Lấy nhiều bản ghi
    def get_data_list(self, sql):
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            return result

        finally:
            # Đóng kết nối (Close connection).
            cur.close()
            self.connection.close()

    #Cập nhật dữ liệu
    def update_data(self, sql):
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            self.connection.commit()

        finally:
            # Đóng kết nối (Close connection).
            cur.close()
            self.connection.close()

# Kết nối đến db email_template
class ConnDBEmailTeplate(ConnSQL):
    def __init__(self, host='localhost', db='email_template', user='root', password='123456@Aabc'):
        super().__init__(host, db, user, password)