import math

import searchdata


def mater_sup(keyword, pageSize, curPage, mater):
    filters = "FMaterialId = '" + mater + "' and FForbidStatus = 'A' and FDisableStatus = 'B' and FPriceType = 2"
    print(filters)
    price_list = searchdata.getdata("PUR_PriceCategory", "FName,FNumber", filters, pageSize,
                                    pageSize * (curPage - 1))
    print(price_list)
    data_list = []
    for sup in price_list:
        data = {"supplier_name": sup[0]}
        data_list.append(data)
    total_data = searchdata.getdata("PUR_PriceCategory", "count(1)", filters, 0, 0)
    rowsCounts = int(total_data[0][0])
    pageCounts = int(math.ceil(rowsCounts / 7))
    resu = {
        "success": True,
        "pageList": {
            "pageCount": pageCounts,
            "curPage": curPage,
            "rowsCount": rowsCounts,
            "colList": [
                {
                    "colEnName": "id"
                },
                {
                    "showName": "true",
                    "colZhName": "价目表名称",
                    "widgetType": "textWidget",
                    "colEnName": "supplier_name"
                }
            ],
            "dataList": data_list
        }
    }
    return resu
