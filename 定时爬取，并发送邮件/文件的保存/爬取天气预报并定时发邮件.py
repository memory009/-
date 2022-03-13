import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')
#9-11行，把获取数据也放到函数的外面
def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://forecast.weather.com.cn/town/weather1dn/101280101004.shtml#around2'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    tem= soup.find(class_='temp').text
    wind= soup.find(class_='wind').text     #.text可以直接接着写，也可以再起一行写

    return tem,wind

def send_email(tem,wind):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content='亲爱的！现在广州金沙街道的温度是'+str(tem)+'度'+'吹'+wind+'哦'
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    tem,weather = weather_spider()     #调用weather_spider()
    send_email(tem,weather)            #调用函数send_email(),把参数传入
    print('任务完成')
    schedule.every(3).hour.do(job)  
while True:
    schedule.run_pending()
    time.sleep(1)
