# 返回物料列表信息
import searchdata
import math

# 构造单位列表
unitnode = {
    "10099": "升",
    "10101": "Pcs",
    "796960": "kg",
    "956883": "项",
    "956886": "项",
    "100130": "把",
    "100131": "包",
    "100132": "本",
    "10089": "厘米",
    "100133": "袋",
    "10147": "栋",
    "10102": "双",
    "10103": "打",
    "100134": "副",
    "100135": "付",
    "10097": "克",
    "100136": "个",
    "100137": "根",
    "100138": "盒",
    "80507": "时",
    "100139": "件",
    "100140": "卷",
    "10095": "千克",
    "10088": "千米",
    "100141": "块",
    "10150": "辆",
    "10087": "米",
    "80506": "分",
    "10100": "毫升",
    "787307": "批",
    "100142": "片",
    "100143": "瓶",
    "100144": "平方米",
    "80505": "秒",
    "810369": "双",
    "10148": "台",
    "10149": "套",
    "100145": "条",
    "10096": "吨",
    "100146": "桶",
    "100147": "箱",
    "100148": "盏",
    "100149": "张",
    "100150": "只",
    "100151": "支"
}


def material(keyword, pageSize, curPage):
    # 构造过滤条件
    filters = "(FName like '%" + keyword + "%' or FNumber like '%" + keyword + "%' or FSpecification like '%" + keyword + "%') and FUseOrgId=100008"
    print(filters)
    # 获取总行数和总页数
    total_data = searchdata.getdata("BD_MATERIAL", "count(1)", filters, 0, 0)
    rowsCounts = int(total_data[0][0])
    pageCounts = int(math.ceil(rowsCounts / 7))
    # 获取物料列表信息
    materials = searchdata.getdata("BD_MATERIAL", "FName,FNumber,FSpecification,FPurchaseUnitId", filters,
                                   pageSize,
                                   pageSize * (curPage - 1))
    data_list = []
    for index, sup in enumerate(materials):
        data = {"id": index, "codecode": sup[1], "codename": sup[0], "codemodel": sup[2],
                "codeunit": unitnode[str(sup[3])]}
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
                    "colZhName": "物料代码",
                    "widgetType": "textWidget",
                    "colEnName": "codecode"
                },
                {
                    "showName": "false",
                    "colZhName": "物料名称",
                    "widgetType": "textWidget",
                    "colEnName": "codename"
                },
                {
                    "showName": "false",
                    "colZhName": "规格型号",
                    "widgetType": "textWidget",
                    "colEnName": "codemodel"
                },
                {
                    "showName": "false",
                    "colZhName": "单位",
                    "widgetType": "textWidget",
                    "colEnName": "codeunit"
                }
            ],
            "dataList": data_list
        }
    }
    return resu
