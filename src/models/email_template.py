from datetime import datetime
from src.models.connection_db import *

class EmailTemplates:

    def __init__(self, id=None, employee_id=None, title=None, content=None, created_at=datetime.now(), updated_by=None, updated_at=datetime.now()):
        self.id = id
        self.employee_id = employee_id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_by = updated_by
        self.updated_at = updated_at

    def check_title_email_template(self):
        sql = "Select id from email_template where title =\'{}\'".format(self.title)
        data = conn_SQL_email_teplate()
        result = data.get_data(sql=sql)
        return result

    def get_email_template_by_id(self):
        sql = "Select merchant_id, title, content from email_template inner join employee on employee_id = employee.id where email_template.id = {}".format(self.id)
        data = conn_SQL_email_teplate()
        result = data.get_data(sql=sql)
        return result

    def insert_email_template(self):
        sql = "insert into email_template(employee_id, title, content, created_at) values ({}, \'{}\',\'{}\', \'{}\')".format(self.employee_id, self.title, self.content, self.created_at)
        data = conn_SQL_email_teplate()
        data.update_data(sql=sql)

    def update_email_template(self):
        sql = "Update email_template set title=\'{}\', content=\'{}\', updated_by={}, updated_at=\'{}\' where id={}".format(
            self.title, self.content, self.updated_by, self.updated_at, self.id)
        data = conn_SQL_email_teplate()
        data.update_data(sql=sql)

    def delete_email_template(self):
        sql = "Delete from email_template where id ={}".format(self.id)
        data = conn_SQL_email_teplate()
        data.update_data(sql=sql)

    def get_email_template_list(self, merchant_id):
        sql = "select title, content from email_template inner join employee on employee_id = employee.id where merchant_id = {} ".format(merchant_id)
        data = conn_SQL_email_teplate()
        result = data.get_data_list(sql=sql)
        return result

    def search_email_template(self, merchant_id, q):
        sql = 'Select title, content from email_template inner join employee on employee_id = employee.id where merchant_id = {} and title like "%{}%"'.format(merchant_id, q)
        data = conn_SQL_email_teplate()
        result = data.get_data_list(sql=sql)
        return result