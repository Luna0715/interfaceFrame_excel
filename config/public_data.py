#encoding=utf-8
import os
#整个项目的根目录绝对路径
baseDir = os.path.dirname(os.path.dirname(__file__))
#print baseDir
#设置数据文件的绝对路径
file_path = baseDir + "\\TestData\\inter_test_data.xlsx"
#print file_path

API_apiName = 2
API_requestUrl = 3
API_requestMothod = 4
API_paramsType = 5
API_apiTestCaseFileName = 6
API_active = 7

CASE_requestData = 1
CASE_relyData = 2
CASE_responseCode = 3
CASE_responseData = 4
CASE_dataStore = 5
CASE_checkPoint = 6
CASE_active = 7
CASE_status = 8
CASE_errorInfo = 9

#存储请求参数里面的依赖数据
REQUEST_DATA = {}

#存储响应对象中的依赖数据
REPONSE_DATA = {}