import requests
#引用requests库
res=requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
#歌曲的地址

with open('music.mp3','wb') as f:       
#open('文件地址'，'文件名'，'读写格式')，此处省略了文件地址，所以文件直接保存在程序运行的该目录下
    
    f.write(res.content)         
    #写入文件
    
    f.close()       
    #使用with open...as时可以省略close()函数