# -*- coding: utf-8 -*-
import requests
url='https://www.cwb.gov.tw/V7/forecast/week/week.htm'
r = requests.get(url)  #取得網頁
r.encoding='big5hkcs'  #編碼
結果 = r.text
結果 = 結果.split('\n')
print (結果)   # 網頁內容
input('按任意鍵繼續')