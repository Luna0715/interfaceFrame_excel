#encoding=utf-8
from config.public_data import REQUEST_DATA,REPONSE_DATA
from  utils.md5_encrypt import md5_encrypt
#REQUEST_DATA={"用户注册":{"1":{"username":"lyz001","password":"iloveyou"}}}
class GetKey(object):
    def __init__(self):
        pass
    #dataSource数据源
    #relyData依赖数据源
    @classmethod
    def get(self, dataSource,relyData):
        # print REQUEST_DATA
        # print REPONSE_DATA
        data=dataSource.copy()
        for key,value in relyData.items():
            if key == "request":
                #{"request": {"username": "用户注册->1", "password": "用户注册->1"}, "response": {"userid": "用户注册->1"}}
                #说明应该去REQUEST_DATA获取值
                for k,v in value.items():
                    interfaceName,case_id = v.split("->")
                    #print type(interfaceName)
                    val = REQUEST_DATA[interfaceName.decode("utf-8")][case_id][k]
                    if k == "password":
                        data[k]= md5_encrypt(val)
                    else:
                        data[k] = val
            elif key == "response":
                #说明应该去RESPONSE_DATA获取值
                for k,v in value.items():
                    interfaceName,case_id = v.split("->")
                    print interfaceName
                    data[k] = REQUEST_DATA[interfaceName.decode("utf-8")][case_id][k]
            return data


if __name__=='__main__':
    s={"username":"","password":""}
    rely={"request":{"username":"用户注册->1","password":"用户注册->1"}}
    print GetKey.get(s,rely)




