{'data': {'formInfo': {
    'widgetMap': {'Te_2': {'codeId': 'Te_2', 'extendFieldMap': {}, 'title': '其他来源说明', 'type': 'textWidget'},
                  'Te_1': {'codeId': 'Te_1', 'extendFieldMap': {}, 'title': '报告编号', 'type': 'textWidget',
                           'value': '12'},
                  '_S_SERIAL': {'codeId': '_S_SERIAL', 'extendFieldMap': {}, 'title': '流水号', 'type': 'serialNumWidget',
                                'value': 'SJZGT-20211029-001'},
                  '_S_DATE': {'codeId': '_S_DATE', 'fromNowOn': 'False', 'title': '申请日期', 'type': 'dateWidget',
                              'value': 1635487815169}, 'Ra_0': {'codeId': 'Ra_0', 'extendFieldMap': {},
                                                                'displaylinkageVos': [{'additional': {
                                                                    'state': {'label': '必填', 'value': 'required'},
                                                                    'option': [{'label': '审计报告', 'value': 'AaBaCcDd'}],
                                                                    'target': {'label': '报告编号', 'value': 'Te_1'}},
                                                                                       'rule': {
                                                                                           'or': [{'eq': 'AaBaCcDd'}]},
                                                                                       'behavior': {'Te_1': {
                                                                                           'state': 'required'}}}, {
                                                                                          'additional': {
                                                                                              'state': {'label': '隐藏',
                                                                                                        'value': 'hidden'},
                                                                                              'option': [
                                                                                                  {'label': '审计报告',
                                                                                                   'value': 'AaBaCcDd'}],
                                                                                              'target': {
                                                                                                  'label': '其他来源说明',
                                                                                                  'value': 'Te_2'}},
                                                                                          'rule': {'or': [
                                                                                              {'eq': 'AaBaCcDd'}]},
                                                                                          'behavior': {'Te_2': {
                                                                                              'state': 'hidden'}}}, {
                                                                                          'additional': {
                                                                                              'state': {'label': '隐藏',
                                                                                                        'value': 'hidden'},
                                                                                              'option': [{'label': '其他',
                                                                                                          'value': 'EeFfGgHh'}],
                                                                                              'target': {
                                                                                                  'label': '报告编号',
                                                                                                  'value': 'Te_1'}},
                                                                                          'rule': {'or': [
                                                                                              {'eq': 'EeFfGgHh'}]},
                                                                                          'behavior': {'Te_1': {
                                                                                              'state': 'hidden'}}}, {
                                                                                          'additional': {
                                                                                              'state': {'label': '必填',
                                                                                                        'value': 'required'},
                                                                                              'option': [{'label': '其他',
                                                                                                          'value': 'EeFfGgHh'}],
                                                                                              'target': {
                                                                                                  'label': '其他来源说明',
                                                                                                  'value': 'Te_2'}},
                                                                                          'rule': {'or': [
                                                                                              {'eq': 'EeFfGgHh'}]},
                                                                                          'behavior': {'Te_2': {
                                                                                              'state': 'required'}}}],
                                                                'options': [{'checked': 'False', 'value': '审计报告',
                                                                             'key': 'AaBaCcDd'},
                                                                            {'checked': 'False', 'value': '其他',
                                                                             'key': 'EeFfGgHh'}], 'linkRule': [],
                                                                'title': '来源', 'type': 'radioWidget',
                                                                'value': 'AaBaCcDd'},
                  'Im_0': {'codeId': 'Im_0', 'extendFieldMap': {}, 'maximum': 200, 'title': '图片', 'type': 'imageWidget',
                           'value': []},
                  '_S_APPLY': {'eid': '19469603', 'codeId': '_S_APPLY', 'existEcosphere': 'False', 'title': '提交人',
                               'type': 'personSelectWidget', 'personInfo': [
                          {'image': 'https://static.yunzhijia.com/space/c/photo/load?id=60d59879fc15d6000143ffae',
                           'companyName': '江苏谷登重型机械装备科技有限公司', 'jobTitle': 'ERP专员', 'name': '周为',
                           'deptLongName': '江苏谷登重型机械装备科技有限公司/运营中心/信息化部', 'oid': '5f2e53bce4b0ce6aad23fa1e',
                           'dept': '信息化部', 'userId': '5f2686c2e4b0aa487b634a9c'}],
                               'value': ['5f2e53bce4b0ce6aad23fa1e']},
                  'Ta_0': {'codeId': 'Ta_0', 'extendFieldMap': {}, 'title': '说明', 'type': 'textAreaWidget',
                           'value': ''}, 'At_0': {'codeId': 'At_0', 'extendFieldMap': {}, 'maximum': 200, 'title': '文件',
                                                  'type': 'attachmentWidget', 'value': []},
                  '_S_DEPT': {'eid': '19469603', 'codeId': '_S_DEPT', 'title': '所属部门', 'type': 'departmentSelectWidget',
                              'deptInfo': [{'name': '信息化部', 'orgId': '4eebc4b6-0c4e-11ec-8a77-ecf4bbea1498',
                                            'realLongName': '江苏谷登重型机械装备科技有限公司!运营中心!信息化部', 'longName': '信息化部(运营中心)'}],
                              'selectCompanyOnly': 'False', 'value': ['4eebc4b6-0c4e-11ec-8a77-ecf4bbea1498']},
                  '_S_TITLE': {'codeId': '_S_TITLE', 'extendFieldMap': {'titleEntity': {'kind': 'TITLE_DEFAULT',
                                                                                        'list': [
                                                                                            {'formItem': '_S_APPLY',
                                                                                             'kind': 'ITEM_FORM_ITEM'},
                                                                                            {'formItem': '的',
                                                                                             'kind': 'ITEM_STRING'},
                                                                                            {'formItem': '模板名称',
                                                                                             'kind': 'ITEM_TEMPLATENAME'}]},
                                                                        'defaultTitle': 'True'}, 'title': '标题',
                               'type': 'textWidget', 'value': '周为的测试SC02 审计整改通知单'}}, 'detailMap': {
        'Dd_0': {'buttonName': '添加明细', 'codeId': 'Dd_0', 'widgetVos': {
            'Ds_0': {'eid': '19469603', 'codeId': 'Ds_0', 'extendFieldMap': {}, 'deptTypeSetting': 'allBusinessUnit',
                     'title': '责任部门', 'type': 'departmentSelectWidget', 'deptInfo': [], 'selectCompanyOnly': 'False',
                     'option': 'single'},
            'Ps_0': {'eid': '19469603', 'codeId': 'Ps_0', 'roleIds': [], 'extendFieldMap': {}, 'existEcosphere': 'False',
                     'optSource': 'org', 'title': '审计人员', 'type': 'personSelectWidget', 'personInfo': [],
                     'option': 'single'},
            'Ps_1': {'eid': '19469603', 'codeId': 'Ps_1', 'roleIds': [], 'extendFieldMap': {}, 'existEcosphere': 'False',
                     'optSource': 'org', 'title': '整改责任人', 'type': 'personSelectWidget', 'personInfo': [],
                     'option': 'multi'},
            'Te_0': {'codeId': 'Te_0', 'extendFieldMap': {'wordLimit': 200}, 'title': '报告索引', 'type': 'textWidget'},
            'Ta_3': {'codeId': 'Ta_3', 'extendFieldMap': {'wordLimit': 5000}, 'title': '整改措施',
                     'type': 'textAreaWidget'},
            'Ta_2': {'codeId': 'Ta_2', 'extendFieldMap': {'wordLimit': 5000}, 'title': '原因分析',
                     'type': 'textAreaWidget'},
            'Ta_1': {'codeId': 'Ta_1', 'extendFieldMap': {'wordLimit': 5000}, 'title': '审计发现',
                     'type': 'textAreaWidget'},
            'Da_0': {'codeId': 'Da_0', 'dateFormat': 'yyyy-MM-dd', 'extendFieldMap': {}, 'fromNowOn': 'False',
                     'title': '整改期限', 'type': 'dateWidget'}}, 'extendFieldMap': {'showSerialNum': 'False'},
                 'widgetValue': [
                     {'Ds_0': ['b3a83a19-f95a-11ea-a634-ecf4bbea149a'], 'Ps_0': ['5f2e53bce4b0ce6aad23fa1e'],
                      'Ps_1': ['5f2e53bce4b0ce6aad23fa1e'], 'Te_0': '索引1', 'Ta_3': '整改措施1', 'Ta_2': '原因分析1',
                      'Ta_1': '发现1', '_id_': '1', 'Da_0': 1635609600000}], 'imageInfo': {}, 'title': '审计报告内容',
                 'type': 'detailedWidget'}}},
          'basicInfo': {'nodeName': '完成审批', 'eid': '19469603', 'eventId': '2f1795b7-bcff-49a4-96e7-ada45e792b3a',
                        'formDefId': '617b8fd396147300015a4827', 'dataType': 1,
                        'myNetworkInfo': {'eid': '19469603', 'name': '江苏谷登重型机械装备科技有限公司'}, 'nodeType': 'END',
                        'title': '测试SC02 审计整改通知单', 'flowInstId': '617b9047f714bb000102616f',
                        'formCodeId': '7813500523e345259fc25f7189d79e01', 'actionType': 'reach', 'myPersonInfo': {
                  'image': 'https://static.yunzhijia.com/space/c/photo/load?id=60d59879fc15d6000143ffae',
                  'jobNo': '20080103', 'name': '周为', 'oid': '5f2e53bce4b0ce6aad23fa1e'},
                        'formInstId': '617b9047b8e90c00011795a6', 'eventTime': 1635487816842,
                        'myDeptInfo': {'name': '信息化部', 'orgId': '4eebc4b6-0c4e-11ec-8a77-ecf4bbea1498'},
                        'interfaceId': 'JM2oUZ4I', 'interfaceName': '测试接口', 'returned': 'False',
                        'nodeId': '617b9048f714bb00010261e2'}}, 'success': 'True', 'errorCode': 0}
