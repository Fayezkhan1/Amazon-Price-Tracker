import requests
from bs4 import BeautifulSoup
url="https://www.amazon.in/Fire-Boltt-Phoenix-Bluetooth-Calling-Monitoring/dp/B0B3RRWSF6/ref=sr_1_1?pd_rd_r=9c6594af-6e55-4827-9835-32c8173c5f77&pd_rd_w=QfadS&pd_rd_wg=OQeYi&pf_rd_p=c53de534-1196-4435-9d49-559c5370def0&pf_rd_r=0SWEP065D08YS9Y75QMC&qid=1680070627&sr=8-1"

#url="https://www.amazon.in/dp/B09WYW1WWL/ref=QAHzEditorial_en_IN_3?pf_rd_r=NRTVSRVF5HF1QJRHZY4Q&pf_rd_p=438c44e5-227b-4881-88e1-9cea5c254a67&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&pf_rd_t=&pf_rd_i=1389401031&ie=UTF8&ref_=CLP_MH8_BSAffordable_3"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0",
    "Accept-Language":"en"
}
r=requests.get(url,headers=headers)

soup =BeautifulSoup(r.text,"lxml")

# print(soup.prettify())

name=soup.select_one(selector="#productTitle").getText()
name=name.strip()
print(names)
