# !/usr/bin/python
# --*coding:utf-8 -*-

'''
auth:lzq
desc:监控Nginx后端服务响应的状态,一旦响应时间超过10ms,累计次数超过10次,将通过邮件告警
date:2016-12-06

remake:因为nginx每天23:59分会做一次备份,旧的access.log会被临时删掉，一旦删掉该监控程序将会
失效(问题暂时还不能通过python自身解决),只能通过把如下语句加入Nginx备份脚本配合,定时重启python程序,但能解决问题就OK了。

ps aux | grep monitoring.py | grep  -v "grep" | awk -F' ' '{print $2}' | xargs kill -9; python monitoring.py

'''

import re
import os
import sys
import time
import smtplib
import subprocess
from email.mime.text import MIMEText
from email.header import Header

# 匹配模式
pattern = r"(\[.*?\]).*?(10.10.101.[0-9][0-9]:8080)(ups_resp_time:.*)(request_time:.*)"
# 日志路径
logfile = 'host.access.log'
# ip地址统计字典
result = {}
# 当前日期时间
currntime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))


# 统计IP地址出现响应超时的次数
def counterror(ipaddr):
    if ipaddr not in result:
        result[ipaddr] = 0

    result[ipaddr] += 1

    return result


def analyzelog(lists):
    date = lists[0]
    ipaddr = lists[1]
    ups_resp_time = str(lists[2]).split(':')[1]
    # 当前日期时间
    currntime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    # print date,ipaddr+":"+ups_resp_time
    try:
        if float(ups_resp_time) > 10:
            counts = counterror(ipaddr)
            if counts[ipaddr] > 10:
                print(ipaddr, "》》 错误次数 超过10！！《《 ", currntime)
                msg = MIMEText(
                    '你好!! \n平台的 Nginx后端服务:' + ipaddr + ",响应时间超过阈值(10ms),当前为:" + ups_resp_time + " 毫秒! \n 响应缓慢,请联系管理员检查！",
                    'plain', 'utf-8')
                msg['Subject'] = Header("Nginx后端服务响应告警!!", 'utf-8')
                sendMail(msg)
                counts[ipaddr] = 0
    except ValueError:
        print(currntime, "值异常:", ups_resp_time)
    # monitoring(logfile)


def sendMail(msg):
    sender = 'lzq@sina.com'
    receiver = ["lzq@163.com", "abc@163.com.cn"]
    smtpserver = 'smtp.sina.com'
    user = 'lzq@sina.com'
    passwd = 'lzq'

    # 群发设置
    msg['To'] = ','.join(receiver)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user, passwd)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("OK")
    except:
        pass

def monitorlog(logfile):
    popen = subprocess.Popen('tail -f ' + logfile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print("文件读取开始.... ", currntime)
    pid = popen.pid
    print('Popen.pid:' + str(pid))

    while True:
        line = popen.stdout.readline().strip()
        matchObj = re.findall(pattern, line, re.M)

        if line and len(matchObj) > 0:
            analyzelog(matchObj[0])
        else:
            continue


if __name__ == "__main__":
    print("Start")
    print("监控的日志文件是%s" % logfile)
    monitorlog(logfile)