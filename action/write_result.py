#encoding=utf-8
from config.public_data import *


def write_result(wbObj,sheetObj,responseData,errorKey,rowNum):
    try:
        #写响应body
        wbObj.writeCell(sheet=sheetObj,content="%s" %responseData,rowNo=rowNum,colsNo=CASE_responseData)
        #写校验结果状态列及错误信息列
        #errorKey有值的时候写
        if errorKey:
            wbObj.writeCell(sheet=sheetObj,content="faild",rowNo=rowNum,colsNo=CASE_status)
            wbObj.writeCell(sheet=sheetObj,content="%s" %errorKey,rowNo=rowNum,colsNo=CASE_errorInfo)
        else:
            #只需要写状态列
            #errorKey空，只写状态列
            wbObj.writeCell(sheet=sheetObj,content="pass",rowNo=rowNum,colsNo=CASE_status)
    except Exception,e:
        raise e

