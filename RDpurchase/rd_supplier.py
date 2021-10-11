# 返回供应商列表信息，用于新供应商申请物料价格
import searchdata
import math


def supplier_inf(keyword, pageSize, curPage):
    # 获取供应商列表信息
    # 构造过滤条件
    filters = "FName like '%" + keyword + "%' and FUseOrgId=448134"
    # 获取总行数和总页数
    total_data = searchdata.getdata("BD_Supplier", "count(1)", filters, 0, 0)
    rowsCounts = int(total_data[0][0])
    pageCounts = int(math.ceil(rowsCounts / 7))
    suppliers = searchdata.getdata("BD_Supplier", "FName", filters, pageSize,
                                   pageSize * (curPage - 1))
    data_list = []
    for index, sup in suppliers:
        data = {"id": index, "supplier": sup[0]}
        data_list.append(data)
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
                    "colZhName": "供应商",
                    "widgetType": "textWidget",
                    "colEnName": "supplier"
                }
            ],
            "dataList": data_list
        }
    }
    return resu
