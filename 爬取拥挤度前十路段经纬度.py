import requests
import json
import csv
url = 'https://trp.autonavi.com/ajax/roadRank.do?roadType=0&timeType=0&cityCode=150100'
headers = {
    'referer':'https://y.qq.com/portal/search.html',# 请求来源
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
res = requests.get(url)
json_point=res.json()
list_piont=json_point['tableData']
print(list_piont)


# list=[]

# for i in list_piont:
#     list.append(i)


# with open("map.csv", 'w', newline="", encoding="gb18030") as f:
#     writer = csv.writer(f)
#     for i in list:
#         print(i)
#         writer.writerow(i)