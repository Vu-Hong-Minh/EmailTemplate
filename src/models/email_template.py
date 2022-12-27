from src.models.get_data import GetData
from datetime import datetime

class EmailTemplates:

    def __init__(self, id=None, merchant_id=None, employee_id=None, title=None, content=None, created_at=datetime.now(), updated_by=None, updated_at=datetime.now()):
        self.id = id
        self.merchant_id = merchant_id
        self.employee_id = employee_id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_by = updated_by
        self.updated_at = updated_at

    def check_title_email_template(self):
        sql = "Select id from email_template where title =\'{}\'".format(self.title)
        data = GetData(sql=sql)
        result = data.get_data()
        return result

    def get_email_template_by_id(self):
        sql = "Select merchant_id, title, content from email_template where id ={}".format(self.id)
        data = GetData(sql=sql)
        result = data.get_data()
        return result


    def insert_email_template(self):
        sql = "insert into email_template(merchant_id, employee_id, title, content, created_at) values ({}, {}, \'{}\',\'{}\', \'{}\')".format(
            self.merchant_id, self.employee_id, self.title, self.content, self.created_at)
        data = GetData(sql=sql)
        data.update_data()

    def update_email_template(self):
        sql = "Update email_template set title=\'{}\', content=\'{}\', updated_by={}, updated_at=\'{}\' where id={}".format(
            self.title, self.content, self.updated_by, self.updated_at, self.id)
        data = GetData(sql=sql)
        data.update_data()

    def delete_email_template(self):
        sql = "Delete from email_template where id ={}".format(self.id)
        data = GetData(sql=sql)
        data.update_data()

    def get_email_template_list(self):
        sql = "select title, content from email_template where merchant_id = {}".format(self.merchant_id)
        data = GetData(sql=sql)
        result = data.get_data_list()
        return result

    def search_email_template(self, q):
        sql = 'Select title, content from email_template where merchant_id = {} and title like "%{}%"'.format(self.merchant_id, q)
        data = GetData(sql=sql)
        result = data.get_data_list()
        return result