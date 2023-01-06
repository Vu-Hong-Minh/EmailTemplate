from src.models.email_template import *
from flask import Blueprint, request, jsonify

email_templates = Blueprint("email_templates", __name__)

#Api lấy thông tin mẫu email
@email_templates.route("/v1/email-templates/<int:email_template_id>", methods=['GET'])
def get_email_template_by_id_service(email_template_id):
    email = EmailTemplates(id=email_template_id)
    result = email.get_email_template_by_id()
    if result != None:
        data = {
            "merchant_id": result[0],
            "title": result[1],
            "content": result[2]
        }
        return jsonify({
            "code": 200,
            "data": data,
            "internal_message": "Request thành công"
        })
    else:
        return jsonify({
            "code": 200,
            "user_message": "Mẫu email không tồn tại",
            "internal_message": "Request thành công"
        })

#Api cập nhật mẫu email
@email_templates.route("/v1/email-templates/<int:email_template_id>/edit", methods=['PUT'])
def update_email_template_service(email_template_id):
    data = request.json
    employee_id = data.get('employee_id')
    title = data.get('title')
    content = data.get('content')
    email = EmailTemplates(id=email_template_id, title=title, content=content, updated_by=employee_id)
    email.update_email_template()
    return jsonify({
        "code": 200,
        "user_message": "Update mẫu email thành công",
        "internal_message": "Request thành công"
    })

#Api xóa mẫu email
@email_templates.route("/v1/email-templates/<int:email_template_id>/delete", methods=['DELETE'])
def delete_email_template_service(email_template_id):
    email = EmailTemplates(id=email_template_id)
    email.delete_email_template()
    result = email.get_email_template_by_id()
    if result == None:
        return jsonify({
            "code": 200,
            "user_message": "Xóa mẫu email thành công",
            "internal_message": "Request thành công"
        })

#Api lấy danh sách mẫu email
@email_templates.route("/v1/email-templates", methods=['GET'])
def get_email_template_list_service():
    data = request.json
    merchant_id = data.get('merchant_id')
    email = EmailTemplates()
    result = email.get_email_template_list(merchant_id=merchant_id)
    data = []
    for i in result:
        temp = {
            "title": i[0],
            "content": i[1]
        }
        data.append(temp)
    return jsonify({
        "code": 200,
        "data": data,
        "internal_message": "Request thành công"
    })

#Api thêm mới mẫu email
@email_templates.route("/v1/email-templates/add", methods=['POST'])
def insert_email_template_service():
    data = request.json
    employee_id = data.get('employee_id')
    title = data.get('title')
    content = data.get('content')
    email = EmailTemplates(employee_id=employee_id, title=title, content=content)
    result1 = email.check_title_email_template()
    if result1 == None:
        email.insert_email_template()
        result = email.check_title_email_template()
        if result != None:
            return jsonify({
                "code": 200,
                "user_message": "Thêm mới mẫu email thành công",
                "internal_message": "Request thành công"
            })
    else:
        return jsonify({
            "code": 200,
            "user_message": "Tiêu đề mẫu email của bạn đã tồn tại, vui lòng đặt tiêu đề khác!",
            "internal_message": "Request thành công"
        })

#Api tìm kiếm mẫu email
@email_templates.route("/v1/email-template/search", methods=['GET'])
def search_email_template_service():
    data = request.json
    q = request.args['q']
    merchant_id = data.get('merchant_id')
    email = EmailTemplates()
    result = email.search_email_template(merchant_id=merchant_id, q=q)
    data = []
    for i in result:
        temp = {
            "title": i[0],
            "content": i[1]
        }
        data.append(temp)
    return jsonify({
        "code": 200,
        "data": data,
        "internal_message": "Request thành công"
    })

#Api Copy mẫu email
@email_templates.route("/v1/email-template/copy", methods=['POST'])
def copy_email_template_service():
    data = request.json
    email_template_id = data.get('email_template_id')
    employee_id = data.get('employee_id')
    #Lấy thông tin email cần copy
    result = EmailTemplates(id=email_template_id).get_email_template_by_id()
    title = result[1]
    content = result[2]
    title = title + " (1)"
    #Check title email và thêm mới email
    email = EmailTemplates(employee_id=employee_id, title=title, content=content)
    while email.check_title_email_template() != None:
        if title[-2].isnumeric():
            temp = int(title[-2]) + 1
            title = title[:-2] + str(temp) + ")"
        email = EmailTemplates(employee_id=employee_id, title=title, content=content)
    email.insert_email_template()
    return jsonify({
        "code": 200,
        "user_message": "Sao chép mẫu email thành công",
        "internal_message": "Request thành công"
    })
