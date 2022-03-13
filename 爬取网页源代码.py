# 调用requests模块
import requests
# 获取网页源代码，得到的res是response对象。
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='http://www.xuexi.la/gongzuobaogao/41909.html'
res = requests.get(url,headers=headers) 
# 检测请求是否正确响应
print(res.status_code) 
# 正确响应，进行读写操作
# 新建一个名为book的html文档，你看到这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 字符串需要以w读写。你在学习open()函数时接触过它。
if res.status_code == 200:
    #输出200就是正确响应的意思
    with open('jjb.html','w',encoding='utf-8') as f:
    # res.text是字符串格式，把它写入文件内。
        f.write(res.text) 
print(res.text)
