# 供应商付款申请单，查询供应商信息和其他往来单位信息
import searchdata
import math


def other_company(keyword, pageSize, curPage):
    # 首先获取其他往来单位列表信息，如果获取不到，则获取供应商信息。
    # 构造过滤条件
    filters = "FName like '%" + keyword + "%'"
    # 获取其他往来单位总行数和总页数
    total_data = searchdata.getdata("FIN_OTHERS", "count(1)", filters, 0, 0)
    rowsCounts = int(total_data[0][0])
    pageCounts = int(math.ceil(rowsCounts / 7))
    others = searchdata.getdata("FIN_OTHERS", "FName,F_good_Text1,F_good_Text", filters, pageSize,
                                pageSize * (curPage - 1))
    print(others)
    # 获取供应商的总行数和总页数
    filters_sup = "FName like '%" + keyword + "%' and FUseOrgId=448134"
    total_data_sup = searchdata.getdata("BD_Supplier", "count(1)", filters_sup, 0, 0)
    rowsCounts_sup = int(total_data_sup[0][0])
    pageCounts_sup = int(math.ceil(rowsCounts_sup / 7))
    suppliers = searchdata.getdata("BD_Supplier", "FName,FBankCode,FOpenAddressRec", filters_sup, pageSize,
                                   pageSize * (curPage - 1))
    data_list = []
    pc = 0
    cp = 0
    rc = 0
    data = {}
    list_da = []
    if len(others) > 0:
        pc = pageCounts
        cp = curPage
        rc = rowsCounts
        list_da = others
    else:
        pc = pageCounts_sup
        cp = curPage
        rc = rowsCounts_sup
        list_da = suppliers

    for index, sup in enumerate(list_da):
        data = {"id": index, "supplier": sup[0],
                "bankNumber": sup[1] if sup[1] != None else "", "location": sup[2] if sup[2] != None else ""}
        data_list.append(data)
    resu = {
        "success": True,
        "pageList": {
            "pageCount": pc,
            "curPage": cp,
            "rowsCount": rc,
            "colList": [
                {
                    "colEnName": "id"
                },
                {
                    "showName": "true",
                    "colZhName": "其他往来单位",
                    "widgetType": "textWidget",
                    "colEnName": "supplier"
                }
                ,
                {
                    "showName": "false",
                    "colZhName": "银行账号",
                    "widgetType": "textWidget",
                    "colEnName": "bankNumber"
                }
                ,
                {
                    "showName": "false",
                    "colZhName": "供应商开户行及网点",
                    "widgetType": "textWidget",
                    "colEnName": "location"
                }
            ],
            "dataList": data_list
        }
    }

    print(resu)
    return resu
