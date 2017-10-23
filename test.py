#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by susecjh on 2017/10/23

from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.header import Header

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

msg = MIMEText('hello , send by Python...','plain','utf-8')
from_addr = '571639000@qq.com'
password = 'hlzmwrvufyrrbcbf'
to_addr = 'susecjh@gmail.com'
smtp_server = 'smtp.qq.com'

msg['From'] = _format_addr('宏爸爸<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自宏爸爸的问候....','utf-8').encode()

import smtplib
server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(False)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()