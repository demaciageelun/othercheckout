# 分配数据

import json, requests

login_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
audit_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Allocate.common.kdsvc"
login_data = {"acctid": "608d3f72088e8d", "username": "周为", "password": "372169zw..", "lcid": 2052}


def login():  # 定义登录函数
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies

    # 返回cookies,方便下次访问时携带


# 获取表名和数据，写入erp
# PkIds是物料内码
def allocateToErp(formId, data):
    datas = {"PkIds": data, "TOrgIds": "100008,448133,448134,448135,1382935,1855665"}
    data = {"FormId": formId, "Data": json.dumps(datas)}
    response = requests.post(url=audit_url, data=data, cookies=login())
    print(response.text)
