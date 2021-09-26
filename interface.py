# 查询接口,获取物料的主键id
import json, requests

login_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
view_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.View.common.kdsvc"
login_data = {"acctid": "608d3f72088e8d", "username": "周为", "password": "372169zw..", "lcid": 2052}


def login():  # 定义登录函数
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies


def getPkIds(formId, data):
    data = {"FormId": formId, "Data": json.dumps(data)}
    print(data)
    response = requests.post(url=view_url, data=data, cookies=login())
    response_data = json.loads(response.text)
    print(response_data)
    pk_ids = response_data["Result"]["Result"]["Id"]
    return pk_ids

