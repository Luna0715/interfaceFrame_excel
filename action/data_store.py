#encoding=utf-8
from config.public_data import REPONSE_DATA,REQUEST_DATA

class RelyDataStore(object):
    def __init__(self):
        pass

    @classmethod
    def do(cls,storePoint,apiName,caseId,request_source={},response_source={}):
        #print apiName, request_source, response_source
        #{"request": ["username", "password"], "response": ["userid"]}
        for key,value in storePoint.items():
            if key =="request":
                #说明存储的数据来自请求参数
                for i in value:
                    if request_source.has_key(i):
                        if not REQUEST_DATA.has_key(apiName):
                            #说明存储数据的结构还未生成，需要指明数据存储结构
                            REQUEST_DATA[apiName]={str(caseId):{i:request_source[i]}}
                        else:
                            #说明存储数据结构中最外层结构完整
                            if REQUEST_DATA[apiName].has_key(str(caseId)):
                                REQUEST_DATA[apiName][str(caseId)][i]=request_source[i]
                            else:
                                REQUEST_DATA[apiName][str(caseId)]={i:request_source[i]}
                    else:
                        print "请求参数中不存在字段"+i
            elif key == "response":
                #说明存储数据来自响应body
                for j in value:
                    if response_source.has_key(j):
                        if not REPONSE_DATA.has_key(apiName):
                            #说明存储数据的结构还未生成，需要指明数据存储结构
                            REPONSE_DATA[apiName]={str(caseId):{j:response_source[j]}}
                        else:
                            #说明存储数据结构中最外层结构完整
                            if REPONSE_DATA[apiName].has_key(str(caseId)):
                                REPONSE_DATA[apiName][str(caseId)][j]=response_source[j]
                            else:
                                REPONSE_DATA[apiName][str(caseId)]={j:response_source[j]}
                    else:
                        print "响应body中不存在字段"+j


if __name__ == '__main__':
    r={"username":"srwcx02","password":"wcx123wac1","email":"wcx@qq.com"}
    s={"request":["username","password"],"response":["userid"]}
    res={"userid":12,"code":"00"}
    RelyDataStore.do(s,"register",r,res,)
    print REQUEST_DATA
    print REPONSE_DATA
