# 本地Chrome浏览器设置方法
from bs4 import BeautifulSoup
from selenium import webdriver # 从selenium库中调用webdriver模块
import time # 调用time模块
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot') # 根据类名找到【点击加载更多】
button.click() # 点击
time.sleep(2) # 等待两秒

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') #  使用class_name找到评论
print(len(comments)) # 打印获取到的评论个数
for comment in comments: # 遍历列表
    sweet = comment.find_element_by_class_name('js_hot_text') # 找到评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论
driver.close() # 关闭浏览器
