from selenium import webdriver
import time
import csv
 
driver = webdriver.Chrome()
driver.get("https://index.iresearch.com.cn/Pc/List")
driver.add_cookie({"name":"Hm_lvt_da86c497de4aabd9133a0e4ea10d9bae", 'value':"1589345361"})
driver.add_cookie({"name":"Hm_lpvt_da86c497de4aabd9133a0e4ea10d9bae", 'value': "1589345361"})
driver.add_cookie({"name":"kittyID", 'value':"6b71587683fbce6b19adf5dbd6de1ec0"})
driver.add_cookie({"name":"Hm_lvt_c33e4c1e69eca76a2e522c20e59773f6", 'value':"1589345351,1589345411"})
driver.add_cookie({"name":"Hm_lpvt_c33e4c1e69eca76a2e522c20e59773f6", 'value':"1589348788"})
time.sleep(5)
driver.find_element_by_class_name("more").click()
# 如果你的网络不好，就会只爬取到几个数据，这个时候增加sleep时间即可。
time.sleep(20)
# range里面的数字是滚轮下翻得次数，想爬取更多的数据，就填写更大的数字即可
for i in range(2):
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# sleep里面的数字，如果你网络不好爬取数据不全，加大 这个数字
time.sleep(10)
nameList = driver.find_element_by_name(today).find_elements_by_class_name(co13)
classList = driver.find_elements_by_xpath('//td[@class="col4 ng-binding"]')
numsList = driver.find_elements_by_xpath('//td[@class="col6 ng-binding"]')
increList = driver.find_elements_by_xpath('//td[@class="col7"]/span[1]')
result = zip(nameList, classList, numsList, increList)
apps = []
for i in result:
    app = []
    for j in i:
        app.append(j.text)
    apps.append(app)
print(apps)
with open("艾瑞电子商务.csv", 'w', newline="", encoding="gb18030") as f:
    writer = csv.writer(f)
    for i in apps:
        print(i)
        writer.writerow(i)
driver.quit()
