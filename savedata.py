# 向erp中新建数据
# 第一步、获取erp采购价目表数据，并通过接口传给云之家的互联控件
# 第二步、获取云之家接口数据
# 第三步、将数据写入到erp中
# 第四步、提交审核数据

import json, requests

import allocateData
import interface
import submitData, auditData

login_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
save_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.save.common.kdsvc"
login_data = {"acctid": "608d3f72088e8d", "username": "周为", "password": "372169zw..", "lcid": 2052}


def login():  # 定义登录函数
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies

    # 返回cookies,方便下次访问时携带


def save(FormID, ins):
    data = {"FormID": FormID, "Data": json.dumps(ins)}
    response = requests.post(url=save_url, data=data, cookies=login())
    resp_data = json.loads(response.text)
    try:
        print(resp_data)
        fnumber = ins["Model"]["FNumber"]
        subdata = {"Numbers": fnumber}
        submitData.submitToErp("BD_Supplier", subdata)
        auditData.auditToErp("BD_Supplier", subdata)
        # 构造接口查询数据
        interface_data = {"Number": fnumber}
        # #     获取物料在数据库中的内码id
        pk_ids = interface.getPkIds("BD_Supplier", interface_data)
        # #     分配数据
        allocateData.allocateToErp("BD_Supplier", pk_ids)
        # # 提交数据
        submitData.submitToErp("BD_Supplier", subdata)
        # # 审核数据
        auditData.auditToErp("BD_Supplier", subdata)
    except Exception as s:
        print(s)
    print(response.text)
