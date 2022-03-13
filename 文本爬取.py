import requests
#引用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
with open('《三国演义》.txt','a+') as f:
#创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
    f.write(res.text[:200])
#写进文件中     
    f.close()
#关闭文档,当使用with open....as时可以省略关闭文档