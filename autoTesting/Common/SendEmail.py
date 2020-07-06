#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import  MIMEMultipart


from email.header import Header

my_sender = '983982466@qq.com'  # 发件人邮箱账号
my_pass = 'fxjeppqynveubeag'  # 发件人邮箱密码
my_user = '767030703@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail(files_part=None):
    ret = True
    try:
        msg= MIMEMultipart()
        # files_part = r'D:\autoTesting\Reports\2020-05-10-11-11-52.html'


        if os.path.exists(files_part):
            filespart = MIMEApplication(open(files_part, 'rb').read())
            file_name = files_part.split("\\")[-1] # 获取文件名
            print("file_name=", file_name)
            filespart.add_header("Content-Disposition", "attachment",filename=file_name) # file_name是显示附件的名字，可随便自定义
            msg.attach(filespart)

        else:
            print("加载的附件不存在,发送无附件邮件")
        # msg = MIMEText('Python 邮件发送测试001...', 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as ex:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(ex)
        ret = False
    return ret


ret = mail(r'D:\autoTesting\Reports\2020-05-10-11-11-52.html')
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")