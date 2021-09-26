from savedata import save

supplier_group = {
    "Vg9RytQm": "YC",
    "GLEP2S83": "DL",
    "p7vlqtAa": "DQ",
    "y2Tlqv7g": "FL",
    "cFC7W3Se": "JG",
    "lFxoT8UO": "WX",
    "PPhDWB2J": "ABS",
    "HE7i3pEF": "YY",
    "RjUjCd1a": "ZJ",
    "s9o5GVre": "NB",
    "r3OkE258": "QT",
}
depart_group = {
    "AaBaCcDd": "gyssybm001",
    "EeFfGgHh": "gyssybm002",
    "IiJjKkLl": "gyssybm003",
    "DTyZAiWd": "gyssybm004",
}
tax_group = {
    "o2c7Z7z8": "SL02_SYS",
    "7e7ZHZhq": "SL63_SYS",
    "DWSSFuMF": "SL03_SYS",
    "NTGpzG3i": "SL06_SYS",
    "cnrJK69B": "SL07_SYS",
    "Z840bRxh": "SL64_SYS",
    "P12Bqon0": "SL04_SYS"
}
settlement_group = {
    "sQNIGfx0": "001",
    "7bXIzsib": "002",
    "dI59W37P": "003",
    "iL0i1LYv": "004",
    "EzumHcZp": "005",
    "ucZByPxz": "006",
    "Fh64j6hc": "008"
}


def createSupplier(data):
    print(data)
    try:
        org_data = data["data"]["formInfo"]["detailMap"]["Dd_0"]["widgetValue"]
        for datas in org_data:
            insert_data = {
                "Model": {
                    "FName": datas["Te_0"],
                    "FCreateOrgId": {
                        "FNumber": "100"
                    },
                    "FNumber": datas["Te_1"],
                    "FUseOrgId": {
                        "FNumber": "100"
                    },
                    "FGroup": {  # 供应商分组
                        "FNumber": supplier_group[datas["Ra_0"]]
                    },
                    "F_good_Assistant": {  # 供应商使用部门
                        "FNumber": depart_group[datas["Ra_3"]]
                    },
                    "FBaseInfo": {
                        "FAddress": datas["Te_2"],
                        "FSupplierClassify": {
                            "FNumber": "GYSFL001"
                        },
                    },
                    "FFinanceInfo": {
                        "FPayCurrencyId": {
                            "FNumber": "PRE001"
                        },
                        "FPayCondition": {
                            "FNumber": settlement_group[datas["Ra_2"]]
                        },
                        "FTaxRateId": {
                            "FNUMBER": tax_group[datas["Ra_1"]]
                        },
                    },
                    "FSupplierContact": [
                        {
                            "FContact": datas["Te_5"],
                            "FMobile": datas["Nu_0"],
                        }
                    ]
                }
            }
            save("BD_Supplier", insert_data)
    except Exception as e:
        print(e)

    return
