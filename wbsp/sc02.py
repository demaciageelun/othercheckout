# 接收sc02单据的信息，取明细行的信息，自动生成多条sc03的审批流，并提交
import json
import time
from urllib import parse

import requests


def sendToYzj(data):
    # 先获取accesstoken
    millis = int(round(time.time() * 1000))
    url = "https://yunzhijia.com/gateway/oauth2/token/getAccessToken"
    header = {
        "Content-Type": "application/json"
    }
    d = {
        "appId": "SP19469603",
        "eid": "19469603",
        "secret": "vrur24QROfNHAt6oqrawxwJz2ITCSr",
        "timestamp": millis,
        "scope": "team"
    }
    r = requests.post(url=url, data=json.dumps(d), headers=header)
    accessToken = r.json()['data']['accessToken']
    print(accessToken)
    # 根据原始数据遍历取出有用的数据，依次写入目标数据中，并发送到云之家。
    # 基本信息(发起人之类)
    heard_data = data["data"]["basicInfo"]
    # 单据头信息
    widgetMap_data = data["data"]["formInfo"]["widgetMap"]
    list_data = data["data"]["formInfo"]["detailMap"]["Dd_0"]["widgetValue"]
    for datas in list_data:
        # 目标数据。
        send_data = {
            "skipWidgetAuthorityCheck": "true",
            "justDraft": "false",
            "useAlias": "false",
            "resubmit": "true",
            "formCodeId": "0d7ba785ce8649a29ddc154be16366d1",
            "widgetValue": {
                "_S_TITLE": widgetMap_data["Te_1"]["value"] + "&整改追踪&" + str(datas["Te_0"]) + "审计整改追踪单",  # 标题
                "S_APPLY": [heard_data["myPersonInfo"]["oid"]],  # 提交人
                "_S_DEPT": [heard_data["myDeptInfo"]["orgId"]],  # 所属部门
                "S_DATE": int(time.time())*1000,  # 申请日期
                "Ra_0": widgetMap_data["Ra_0"]["value"],  # 来源
                "Te_1": widgetMap_data["Te_1"]["value"],  # 报告编号
                "Te_2": "" if widgetMap_data["Ra_0"]["value"] == "AaBaCcDd" else widgetMap_data["Te_2"]["value"],
                # 其他来源说明
                "Ds_0": [datas["Ds_0"][0]],  # 责任部门
            },
            "oids": [heard_data["myPersonInfo"]["oid"]],
            "creator": heard_data["myPersonInfo"]["oid"],
            "details": {
                "Dd_0": {
                    "widgetValue": [{
                        "_id_": "1",
                        "Te_0": datas["Te_0"],  # 报告索引
                        "Ta_1": datas["Ta_1"],  # 审计发现
                        "Ps_0": [datas["Ps_0"][0]],  # 审计人员
                        "Ta_2": datas["Ta_2"],  # 原因分析
                        "Ta_3": datas["Ta_3"],  # 整改措施
                        "Ps_1": [datas["Ps_1"][0]],  # 整改责任人
                        "Da_0": datas["Da_0"]  # 整改期限
                    }]
                }
            }
        }
        url = "https://yunzhijia.com/gateway/workflow/form/thirdpart/createInst?accessToken=" + accessToken
        # header = {
        #     "Content-Type": "application/raw"
        # }
        d = send_data
        # d = parse.urlencode(d)
        print(d)
        r = requests.post(url=url, json=d)
        print(r.json())
