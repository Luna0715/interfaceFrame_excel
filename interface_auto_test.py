#encoding=utf-8
import  requests
import json
from utils.ParseExcel import ParseExcel
from config.public_data import file_path
from config.public_data import *
from utils.HttpClient import HttpClient
from action.get_rely import GetKey
from action.data_store import RelyDataStore
from action.check_result import CheckResult
from action.write_result import write_result

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    #file_path=r"D:\20170721exercise\interfaceFrame201807\TestData\inter_test_data.xlsx"
    parseE = ParseExcel()
    parseE.loadWorkBook(file_path)
    sheetObj = parseE.getSheetByName(u"API")
    #print sheetObj
    activeList = parseE.getColumn(sheetObj, 7)
    #print activeList
    #for i in activeList:
        #print i.value
    #外层for循环，遍历的api的sheet表
    for idx, cell in enumerate(activeList[1:],2):
        #print idx
        if cell.value == "y":
             # 需要执行的接口所在行的行对象
            rowObj = parseE.getRow(sheetObj, idx)
            #print type(rowObj)
            apiName = rowObj[API_apiName-1].value
            requestUrl = rowObj[API_requestUrl-1].value
            requestMethod = rowObj[API_requestMothod-1].value
            paramsType = rowObj[API_paramsType-1].value
            apiTestCaseFileName = rowObj[API_apiTestCaseFileName-1].value
            #print apiName, requestUrl, requestMothod, paramsType, apiTestCaseFileName
            # 下一步读用例sheet表，准备执行测试用例
            caseSheetObj = parseE.getSheetByName(apiTestCaseFileName)
            caseActiveObj = parseE.getColumn(caseSheetObj, CASE_active)
            # for i in  caseActiveObj:
            #     print i.value
            #内层for循环，遍历的测试用例的sheet
            for c_idx, col in enumerate(caseActiveObj[1:], 2):
                if col.value == "y":
                    # 说明此case行需要执行
                    caseRowObj = parseE.getRow(caseSheetObj, c_idx)
                    requestData = caseRowObj[CASE_requestData - 1].value
                    relyData = caseRowObj[CASE_relyData - 1].value
                    # print requestData
                    # print relyData
                    dataStore=caseRowObj[CASE_dataStore-1].value
                    checkPoint=caseRowObj[CASE_checkPoint-1].value
                    if relyData:
                        #发送接口请求之前，先做依赖数据的处理
                        requestData = "%s" %GetKey.get(eval(requestData),eval(relyData))
                    #print type(requestData)
                    #print requestData
                    # 拼接接口请求参数，发送接口请求
                    #print type(requestData)
                    httpC = HttpClient()
                    #print requestMethod, requestUrl, paramsType, requestData
                    response = httpC.request(requestMethod=requestMethod,requestUrl=requestUrl,paramsType=paramsType,requestData=requestData)
                    if response.status_code==200:
                        responseData = response.json()
                        #存储依赖数据
                        if dataStore:
                            RelyDataStore.do(eval(dataStore),apiName,c_idx-1,eval(requestData),responseData)
                        #比对结果
                        errorKey = CheckResult.check(responseData,eval(checkPoint))
                        write_result(parseE,caseSheetObj,responseData,errorKey,c_idx)
                        # if not errorKey:
                        #     print "校验结果通过"
                        # else:
                        #     print "校验失败",errorKey

                    else:
                        print response.status_code
                else:
                    print "用例被忽略执行"

        else:
            print "接口被设置忽略执行"




if __name__ == '__main__':
    main()
