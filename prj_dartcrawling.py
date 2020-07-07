import requests
import pandas as pd
from io import BytesIO

u_a = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
rcp_no = '20190814002218'
dcm_no = '6846651'
url_1908 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no="+ rcp_no + "&dcm_no=" + dcm_no +"&lang=ko"
url_2005 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20200515002179&dcm_no=7343256&lang=ko"
pocket = ["연결 재무상태표","연결 자본변동표","연결 손익계산서","연결 포괄손익계산서", "연결 자본변동표", "연결 현금흐름표"]



"""for period,url in zip(["1908","2005"],[url_1908,url_2005]) :
    resp = requests.get(url,headers ={"user-agent" : u_a })
    for sheet in ["기본정보", "연결 재무상태표","연결 손익계산서", "연결 포괄손익계산서"] :
        table = BytesIO(resp.content)
        data = pd.read_excel(table, sheet_name=sheet, skiprows=5)
        data.to_csv(period+sheet + ".csv", encoding="euc-kr")
print(url_1908)
"""
def download_excel(url1,period,company) :
    for period, url in zip([period], [url1]):
        resp = requests.get(url1, headers={"user-agent": u_a})
        for sheet in ["기본정보", "연결 재무상태표", "연결 손익계산서", "연결 포괄손익계산서"]:
            table = BytesIO(resp.content)
            data = pd.read_excel(table, sheet_name=sheet, skiprows=5)
            data.to_csv(company+period + sheet + ".csv", encoding="euc-kr")
print(url_1908)

def download_excel_2(period, rcp_no, dcm_no,company) :
    url1 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=" + rcp_no + "&dcm_no=" + dcm_no + "&lang=ko"
    resp = requests.get(url1, headers={"user-agent": u_a})
    for sheet in ["기본정보", "연결 재무상태표", "연결 손익계산서", "연결 포괄손익계산서"]:
        table = BytesIO(resp.content)
        data = pd.read_excel(table, sheet_name=sheet, skiprows=5)
        data.to_csv(str(period)+company + sheet + ".csv", encoding="euc-kr")

download_excel(url_1908,"1908_","삼성전자")
download_excel(url_2005,"2005_","삼성전자")
download_excel_2(rcp_no,dcm_no,"1908_","삼성전자")

df=pd.read_csv("pocket.csv")
print(df)

for period, rdp_no, dcm_no in zip(df['period'].values, df['rcp_no'].values, df['dcm_no'].values) :
    print(period, rcp_no, dcm_no)
    download_excel_2(period,rcp_no,dcm_no,"삼성전자")


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

