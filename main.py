# 返回供应商列表信息，用于新供应商申请物料价格
# 获取到请求后，发送原始数据给云之家互联控件
import time
import datetime

import flask, json

import decrypto
import material_interface, save
from flask import request
from RDpurchase import rd_material, rd_supplier, rd_mater_supp
from xsMaterial import xs_Material
from cptyjjswjggtzd import cpty_material
from supplierChange import insertSupplier, updateSupplier
from qtwldw import save_qtwldw
from gysfksq import search_Info
from wbsp import sc02
unitnode = {
    '升': 'L',
    'Pcs': 'Pcs',
    'kg': 'UOM002',
    '项': 'UOM003',
    '把': 'ba',
    '包': 'bao',
    '本': 'ben',
    '厘米': 'cm',
    '袋': 'dai',
    '栋': 'dong',
    '打': 'dozen',
    '副': 'fu',
    '付': 'fu2',
    '克': 'g',
    '个': 'ge',
    '根': 'gen',
    '盒': 'he',
    '时': 'hour',
    '件': 'jian',
    '卷': 'juan',
    '千克': 'kg',
    '千米': 'km',
    '块': 'kuai',
    '辆': 'liang',
    '米': 'm',
    '分': 'minute',
    '毫升': 'ml',
    '批': 'pi',
    '片': 'pian',
    '瓶': 'ping',
    '平方米': 'pingfangmi',
    '秒': 'second',
    '双': 'shuang',
    '台': 'tai',
    '套': 'tao',
    '条': 'tiao',
    '吨': 'ton',
    '桶': 'tong',
    '箱': 'xiang',
    '盏': 'zhan',
    '张': 'zhang',
    '只': 'zhi',
    '支': 'zhi2',
}
'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# 其他出库申请物料
@server.route('/material', methods=['get', 'post'])
def material():
    data = request.get_data()
    datas = data.decode('utf8')
    jsondata = json.loads(datas)
    print(jsondata)
    try:
        # 搜索关键字
        keyword = jsondata["keyword"]
        # 每页数据，目前固定
        pageSize = jsondata["pageSize"]
        # 当前页
        curPage = jsondata["curPage"]
        # 物料分组
        mater_group = jsondata["rowInfo"]["Ra_0"]
        resu = material_interface.material_inf(keyword, pageSize, curPage, mater_group)
    except Exception as e:
        print(e)
        resu = material_interface.material_inf("", 7, 1, '98qFnfl4')
    return json.dumps(resu, ensure_ascii=False)


# 其他出库新增erp后台
@server.route('/othercheckout', methods=['get', 'post'])
def othercheckout():
    data = json.loads(decrypto.decrypto(request.get_data()))
    print(data)
    # 取传来的数据中的有效数据部分
    widgetValue = data["data"]["formInfo"]["detailMap"]["Dd_0"]["widgetValue"]
    hearder_remarks = data["data"]["formInfo"]["widgetMap"]["_S_SERIAL"]["value"]
    emply_id = data["data"]["basicInfo"]["myPersonInfo"]["jobNo"]
    print(widgetValue)
    data_list = []
    for value in widgetValue:
        save_data = {  # 明细
            "FMaterialId": {
                "FNumber": value["iw_0"][0]["codecode"]
            },  # 物料编码
            "FQty": value["Nu_0"],
            "FUnitID": {
                "FNumber": unitnode[value["Te_3"]]
            },  # 单位
            "FStockStatusId": {
                "FNumber": "KCZT01_SYS"
            },  # 库存状态
            "FOwnerTypeId": "BD_OwnerOrg",  # 货主类型
            "FOwnerId": {
                "FNumber": "101.02"
            },  # 货主
            "FKeeperTypeId": "BD_KeeperOrg",  # 保管者类型
            "FKeeperId": {
                "FNumber": "101"
            },  # 保管者
            "FBaseUnitId": {
                "FNumber": unitnode[value["Te_3"]]
            },  # 基本单位
            # "FStockLocId": {
            #     "FNumber": "FC03C2"
            # },  # 仓位
            "FEntryNote": value["Te_4"],
            "FStockOrgIdEntry": {
                "FNumber": "101"
            },  # 库存组织
            "FStockId": {
                "FNumber": "CK009"
            },  # 仓库
        }
        data_list.append(save_data)

    # 获取当前时间, 其中中包含了year, month, hour, 需要import datetime
    today = datetime.date.today()
    save.save(str(today), "BM000505", emply_id, hearder_remarks, data_list)
    resu = {"success": "true"}
    return json.dumps(resu, ensure_ascii=False)


# 研发临时物料采购申请的物料列表
@server.route('/rdmaterial', methods=['get', 'post'])
def rdmaterial():
    data = request.get_data()
    datas = data.decode('utf8')
    jsondata = json.loads(datas)
    try:
        # 搜索关键字
        keyword = jsondata["keyword"]
        # 每页数据，目前固定
        pageSize = jsondata["pageSize"]
        # 当前页
        curPage = jsondata["curPage"]
        # 物料分组
        resu = rd_material.material_inf(keyword, pageSize, curPage)
    except Exception as e:
        print(e)
        resu = rd_material.material_inf("", 7, 1)
    return json.dumps(resu, ensure_ascii=False)


# 研发临时物料采购申请的供应商列表
@server.route('/rdsupplier', methods=['get', 'post'])
def rdsupplier():
    data = request.get_data()
    datas = data.decode('utf8')
    jsondata = json.loads(datas)
    try:
        # 搜索关键字
        keyword = jsondata["keyword"]
        # 每页数据，目前固定
        pageSize = jsondata["pageSize"]
        # 当前页
        curPage = jsondata["curPage"]
        # 物料分组
        resu = rd_supplier.supplier_inf(keyword, pageSize, curPage)
    except Exception as e:
        print(e)
        resu = rd_supplier.supplier_inf("", 7, 1)
    return json.dumps(resu, ensure_ascii=False)


# 研发临时物料采购申请的供应商列表
@server.route('/rdmatersupplier', methods=['get', 'post'])
def rdmatersupplier():
    data = request.get_data()
    datas = data.decode('utf8')
    jsondata = json.loads(datas)
    print(jsondata)
    try:
        # 搜索关键字
        keyword = jsondata["keyword"]
        # 每页数据，目前固定
        pageSize = jsondata["pageSize"]
        # 当前页
        curPage = jsondata["curPage"]
        materid = jsondata["rowInfo"]["iw_4"][0]["materialId"]
        # 物料分组
        resu = rd_mater_supp.mater_sup(keyword, pageSize, curPage, materid)
    except Exception as e:
        print(e)
        resu = rd_mater_supp.mater_sup("", 7, 1, "550879")
    return json.dumps(resu, ensure_ascii=False)


# 售后业务委托书的物料列表
@server.route('/xsMaterial', methods=['get', 'post'])
def xsMaterial():
    data = request.get_data()
    datas = data.decode('utf8')
    jsondata = json.loads(datas)
    try:
        # 搜索关键字
        keyword = jsondata["keyword"]
        # 每页数据，目前固定
        pageSize = jsondata["pageSize"]
        # 当前页
        curPage = jsondata["curPage"]
        # 物料分组
        resu = xs_Material.material(keyword, pageSize, curPage)
    except Exception as e:
        print(e)
        resu = xs_Material.material("", 7, 1)
    return json.dumps(resu, ensure_ascii=False)


# 售后业务委托书的物料列表
@server.route('/cptymaterial', methods=['get', 'post'])
def cptyMaterial():
    data = request.get_data()
    datas = data.decode('utf8')
    jsondata = json.loads(datas)
    try:
        # 搜索关键字
        keyword = jsondata["keyword"]
        # 每页数据，目前固定
        pageSize = jsondata["pageSize"]
        # 当前页
        curPage = jsondata["curPage"]
        # 物料分组
        resu = cpty_material.material_inf(keyword, pageSize, curPage)
    except Exception as e:
        print(e)
        resu = cpty_material.material_inf("", 7, 1)
    return json.dumps(resu, ensure_ascii=False)


# 接收云之家新增供应商申请单，并写入erp
@server.route('/newSupplier', methods=['get', 'post'])
def newSupplier():
    data = json.loads(decrypto.decrypto(request.get_data()))
    # 处理逻辑
    insertSupplier.createSupplier(data)
    resu = {"success": "true"}
    return json.dumps(resu, ensure_ascii=False)


# 接收云之家更新供应商申请单，并写入erp
@server.route('/updateSupplier', methods=['get', 'post'])
def updateSup():
    data = json.loads(decrypto.decrypto(request.get_data()))
    # 处理逻辑
    updateSupplier.updateSup(data)
    resu = {"success": "true"}
    return json.dumps(resu, ensure_ascii=False)


# 接收云之家新增其他往来单位申请单，并写入erp
@server.route('/newOtherCorrespondents', methods=['get', 'post'])
def newOtherCor():
    data = json.loads(decrypto.decrypto(request.get_data()))
    # 处理逻辑
    save_qtwldw.save(data)
    resu = {"success": "true"}
    return json.dumps(resu, ensure_ascii=False)


# 供应商付款申请获取其他往来单位信息
@server.route('/otherCompany', methods=['get', 'post'])
def otherCompany():
    data = request.get_data()
    datas = data.decode('utf8')
    jsondata = json.loads(datas)
    try:
        # 搜索关键字
        keyword = jsondata["keyword"]
        # 每页数据，目前固定
        pageSize = jsondata["pageSize"]
        # 当前页
        curPage = jsondata["curPage"]
        # 物料分组
        resu = search_Info.other_company(keyword, pageSize, curPage)
    except Exception as e:
        print(e)
        resu = search_Info.other_company("", 7, 1)
    return json.dumps(resu, ensure_ascii=False)


# 接收云之家新增其他往来单位申请单，并写入erp
@server.route('/test', methods=['get', 'post'])
def test():
    data = json.loads(decrypto.decrypto(request.get_data()))
    # 处理逻辑
    print(data)
    resu = {"success": "true"}
    return json.dumps(resu, ensure_ascii=False)


@server.route('/wbspSc02', methods=['get', 'post'])
def wbspSc02():
    data = json.loads(decrypto.decrypto(request.get_data()))
    # 处理逻辑
    print(data)
    sc02.sendToYzj(data)
    resu = {"success": "true"}
    return json.dumps(resu, ensure_ascii=False)




if __name__ == '__main__':
    server.run(debug=True, port=37214, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
