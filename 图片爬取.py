import requests
url='https://www.eyecareandcure.com/ECC-Products/Calipers'+'/Braunstein-Fixed-Caliper-3-0mm-3-5mm-image.jpg'
res = requests.get('https://bkimg.cdn.bcebos.com/pic/cefc1e178a82b90171fb4f6b7c8da9773912ef10?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UyMjA=,xp_5,yp_5')
#发出请求，并把返回的结果放在变量res中
#get后面填入图片的地址
pic=res.content
#把Reponse对象的内容以二进制数据的形式返回
photo = open('ppt.jpg','wb')
#新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
photo.write(pic) 
#获取pic的二进制内容
photo.close()
#关闭文件