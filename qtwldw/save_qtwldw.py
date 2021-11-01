# 新增其他往来单位
# 向erp中新建数据
# 第一步、获取erp采购价目表数据，并通过接口传给云之家的互联控件
# 第二步、获取云之家接口数据
# 第三步、将数据写入到erp中
# 第四步、提交审核数据

import json, requests
import submitData, auditData

login_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
save_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.save.common.kdsvc"
login_data = {"acctid": "608d3f72088e8d", "username": "周为", "password": "372169zw..", "lcid": 2052}


def login():  # 定义登录函数
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies

    # 返回cookies,方便下次访问时携带


def save(data):
    # 获取表名和数据，写入erp
    print(data)
    # 供应商类型（从系统选择，还是其他新增进其他往来单位）

    # 云之家流程创建人
    creater = data["data"]["basicInfo"]["myPersonInfo"]["name"]
    # 云之家流水号
    serialid = data["data"]["formInfo"]["widgetMap"]["_S_SERIAL"]["value"]
    # 其他往来单位信息,可能有多条，需循环
    other_data = data["data"]["formInfo"]["detailMap"]["Dd_1"]["widgetValue"]
    for datas in other_data:
        data_type = datas["Ra_8"]
        if data_type == "AaBaCcDd":
            ins = {
                "ValidateFlag": "true",
                "NumberSearch": "true",
                "Model": {
                    "FCreateOrgId": {
                        "FNumber": "101"
                    },
                    "FUseOrgId": {
                        "FNumber": "101"
                    },
                    "FName": datas["Te_15"],  # 名称
                    "F_good_Text": datas["Te_18"],  # 开户行
                    "F_good_Text1": datas["Te_12"],  # 银行卡号
                    "F_good_Text2": creater,  # 云之家创建人
                    "F_good_Text3": serialid  # 云之家流水号
                }
            }

            data = {"FormID": "FIN_OTHERS", "Data": json.dumps(ins)}
            response = requests.post(url=save_url, data=data, cookies=login())
            resp_data = json.loads(response.text)
            try:
                fnumber = resp_data["Result"]["Number"]
                subdata = {"Numbers": fnumber}
                submitData.submitToErp("FIN_OTHERS", subdata)
                auditData.auditToErp("FIN_OTHERS", subdata)
            except Exception as s:
                print(s)
            print(response.text)
