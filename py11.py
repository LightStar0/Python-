import requests
url = "https://www.cwb.gov.tw/V7/forecast/week/week.htm"
r = requests.get(url) #取得網頁
r.encoding = 'big5hkcs'  #編碼
結果 = r.text
print(結果)

input()
