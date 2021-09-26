import interface


def updateSup(data):
    # 构造接口查询数据
    print(data)
    org_data = data["data"]["formInfo"]["detailMap"]["Dd_0"]["widgetValue"]
    for datas in org_data:
        interface_data = {"Number": datas["Te_1"]}
        # #     获取物料在数据库中的内码id
        pk_ids = interface.getPkIds("BD_Supplier", interface_data)
        {
            "Model": {
                "FSupplierId": pk_ids,
                "FBaseInfo": {
                    "FSupplierClassify": {
                        "FNumber": "GYSFL002"
                    },
                }
            }
        }
