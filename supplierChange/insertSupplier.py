
def createSupplier(data):
    print(data)
    insert_data = {
        "Model": {
            "FName": "测试供应商",
            "FCreateOrgId": {
                "FNumber": "1"
            },
            "FNumber": "123321",
            "FUseOrgId": {
                "FNumber": "1"
            },
            "FGroup": {  # 供应商分组
                "FNumber": "ABS"
            },
            "F_good_Assistant": {  # 供应商使用部门
                "FNumber": "gyssybm004"
            },
            "FFinanceInfo": {
                "FPayCurrencyId": {
                    "FNumber": "PRE001"
                },
                "FPayCondition": {
                    "FNumber": "001"
                },
                "FTaxRateId": {
                    "FNUMBER": "SL02_SYS"
                },
            }
        }
    }
    return
