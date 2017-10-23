#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by susecjh on 2017/10/23

from re import match
import smtplib
from email.mime.text import MIMEText
from email.header import Header

"""封装qq邮箱，gmail邮箱，163邮箱的发送"""


class EmailPost(object):
    def __init__(self, type, from_addr, password):
        """
        :param type: 你发送邮箱的方式，可选内容为:qq,QQ,gmail,163
        :param from_addr: 你的邮箱账号
        :param password: 你的邮箱密码，其中qq方式的发送password为授权码
        """
        if not isinstance(type, str):
            raise ValueError('type is not a str, please input "qq","QQ","gmail","163"!')
        if type == 'qq' or type == 'QQ':
            if match('^\w+@qq.com$', from_addr) is None:
                raise ValueError('The email, %s , is not a %s email' % (from_addr, type))
        if type == 'gmail':
            if match('^\w+@gmail.com$', from_addr) is None:
                raise ValueError('The email, %s , is not a %s email' % (from_addr, type))
        if type == '163':
            if match('^\w+@163.cn$', from_addr) is None:
                raise ValueError('The email, %s , is not a %s email' % (from_addr, type))
        self.__type = type
        self.__from_addr = from_addr
        self.__password = password
        self.__server = self.open()
    
    def open(self):
        """
        :param type: 邮箱类型
        :return: 返回一个SMTP_SSL对象
        """
        if self.__type == 'qq' or self.__type == 'QQ':
            self.__server = self.open_qq()
        if self.__type == 'gmail':
            self.__server = self.open_gmail()
        if self.__type == '163':
            self.__server = self.open_163()
        self.__server.login(self.__from_addr, self.__password)
    
    def open_qq(self):
        return smtplib.SMTP_SSL('smtp.qq.com', 465)
    
    def open_gmail(self):
        return smtplib.SMTP_SSL('smtp.gmail.com', 465)
    
    def open_163(self):
        return smtplib.SMTP_SSL('smtp.163.com', 465)
    
    def post(self, to_addr, msg, subject, subtype='plain', **kwargs):
        """
            msg:你想要发送的内容，可以是html的方式
            subject----主题
            kwargs:
                subtype:发送内容的格式----   'plain'---发送的文本内容，是默认值
                                           'html'----发送html方式
                                           'all'----用时支持以上两种方式
                html_msg----'all' 存在时生效，存储html方式的内容
                from_name----发送人昵称
                to_name----接受人昵称
                file_path-----附加文件地址
        """
        if subtype != 'plain' and subtype != 'html' and subtype != 'all':
            raise ValueError('The subtype is %s ,please input "plain" , "html" or "all".' % subtype)
        # 设置message内容
        message = MIMEText(msg, subtype, 'utf-8')
        message['From'] = _format_addr('%s<%s>'%(self.__from_addr,kwargs.get('from_addr','susecjh')))
        message['To'] = _format_addr('%s<%s>'%(to_addr,kwargs.get('to_addr','用户')))
        message['Subject'] = Header(subject,'utf-8').encode()
        self.__server.sendmail(from_addr=self.__from_addr, to_addrs=to_addrs, msg=message.as_string())

    def __del__(self):
        self.__server.quit()

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))