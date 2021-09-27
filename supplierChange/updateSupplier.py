import interface, savedata, searchdata


def updateSup(data):
    # 构造接口查询数据
    print(data)
    org_data = data["data"]["formInfo"]["detailMap"]["Dd_0"]["widgetValue"]
    for datas in org_data:
        # filter_string = "CreateOrgId": "1", "Number": datas["Te_1"]
        filter_string = "FUseOrgId = 1 and FNumber = '" + datas["Te_1"] + "'"
        # #     获取物料在数据库中的内码id
        pk_ids = searchdata.getdata("BD_Supplier", "FSupplierId", filter_string, 2000, 0)
        print(pk_ids)
        update_data = {
            "Model": {
                "FSupplierId": pk_ids[0][0],
                "FBaseInfo": {
                    "FSupplierClassify": {
                        "FNumber": "GYSFL002"
                    },
                }
            }
        }
        savedata.save("BD_Supplier", update_data)
