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


def save(date, dept, employ, hearder_remarks, save_data):
    # 获取表名和数据，写入erp
    ins = {
        "ValidateFlag": "true",
        "NumberSearch": "true",
        "Model": {
            "FBillTypeID": {
                "FNUMBER": "CKSQ01_SYS"
            },
            "FStockOrgId": {
                "FNumber": "101"
            },  # 申请组织id
            "FDate": date,  # 日期
            "FDeptId": {
                "FNumber": "BM000505"
            },  # 领料部门,目前就是制造部
            "FNote": hearder_remarks,
            "FOwnerTypeIdHead": "BD_OwnerOrg",  # 货主类型
            "F_Good_Base": {
                "FSTAFFNUMBER": employ
            },  # 领料人
            "F_Good_Assistant2": {
                "FNumber": "LL003"
            },  # 领料用途
            # "FUPDATETIME":"2021-08-03 10:47",
            "FEntity": save_data
        }
    }

    # [{  # 明细
    #                 "FMaterialId": {
    #                     "FNumber": "Y0902010131"
    #                 },  # 物料编码
    #                 "FQty":1,
    #                 "FUnitID": {
    #                     "FNumber": "jian"
    #                 },
    #                 "FStockStatusId": {
    #                     "FNumber": "KCZT01_SYS"
    #                 },  # 库存状态
    #                 "FOwnerTypeId": "BD_OwnerOrg",  # 货主类型
    #                 "FOwnerId": {
    #                     "FNumber": "101.02"
    #                 },  # 货主
    #                 "FKeeperTypeId": "BD_KeeperOrg",  # 保管者类型
    #                 "FKeeperId": {
    #                     "FNumber": "101"
    #                 },  # 保管者
    #                 "FBaseUnitId": {
    #                     "FNumber": "jian"
    #                 },  # 基本单位
    #                 # "FStockLocId": {
    #                 #     "FNumber": "FC03C2"
    #                 # },  # 仓位
    #                 "FStockOrgIdEntry": {
    #                     "FNumber": "101"
    #                 },
    #                 "FStockId": {
    #                     "FNumber": "CK009"
    #                 },  # 仓库
    #             }]
    data = {"FormID": "STK_OutStockApply", "Data": json.dumps(ins)}
    response = requests.post(url=save_url, data=data, cookies=login())
    resp_data = json.loads(response.text)
    try:
        fnumber = resp_data["Result"]["Number"]
        subdata = {"Numbers": fnumber}
        submitData.submitToErp("STK_OutStockApply", subdata)
        auditData.auditToErp("STK_OutStockApply", subdata)
    except Exception as s:
        print(s)
    print(response.text)
