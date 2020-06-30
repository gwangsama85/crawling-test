import requests
import pandas as pd
from io import BytesIO

u_a = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
url_2005 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20200515002179&dcm_no=7343256&lang=ko"
url_1908 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20190814002218&dcm_no=6846651&lang=ko"
pocket = ["연결 재무상태표","연결 자본변동표","연결 손익계산서","연결 포괄손익계산서", "연결 자본변동표", "연결 현금흐름표"]

for period,url in zip(["1908","2005"],[url_1908,url_2005]) :
    resp = requests.get(url,headers ={"user-agent" : u_a })
    for sheet in ["기본정보", "연결 재무상태표","연결 손익계산서", "연결 포괄손익계산서"] :
        table = BytesIO(resp.content)
        data = pd.read_excel(table, sheet_name=sheet, skiprows=5)
        data.to_csv(period+sheet + ".csv", encoding="euc-kr")
print(url_1908)

"""data=pd.read_excel(table, s
heet_name="기본정보",skiprows=5)
data.to_csv("기본정보.csv",encoding="euc-kr")

data=pd.read_excel(table, sheet_name="연결 손익계산서",skiprows=5)
data.to_csv("연결 손익계산서.csv",encoding="euc-kr")

data=pd.read_excel(table, sheet_name="연결 포괄손익계산서",skiprows=5)
data.to_csv("연결 재무상태표.csv",encoding="euc-kr")
"""
print(type(pocket))
print(pocket)
print(pocket)

