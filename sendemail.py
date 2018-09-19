#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from email import encoders
import base64

def sendemail():
    sender='13058019302@163.com'
    email_list=['sunlinpeng@fangdd.com','339403375@qq.com']
    receiver= email_list
    mail_host='smtp.163.com'
    username="13058019302@163.com"
    password="520ainiyiwannian"
    #
    msg=MIMEMultipart('related')
    msg.attach(MIMEText('日报详情请查看附件!','plain','utf-8'))
    msg['From']='Tom<13058019302@163.com>'
    msg['To']="sunlinpeng@fangdd.com,339403375@qq.com"
    subject='日报'
    msg['Subject']=Header(subject,'utf-8')

    file='C:\\Users\\Administrator\\Desktop\\bug统计.xlsx'
    basename=os.path.basename(file)

    #构造附件
    fp=open(file,'rb')
    att = MIMEText(fp.read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', basename))
    encoders.encode_base64(att)
    msg.attach(att)

    try:
        smtp=smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error:无法发送邮件！")

sendemail()