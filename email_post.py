#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by susecjh on 2017/10/23

from re import match

"""封装qq邮箱，gmail邮箱，163邮箱的发送"""


def post ( type , from_addr , password , to_addr , msg , **kwargs ) :
	""" type:你发送邮箱的方式，可选内容为:qq,QQ,gmail,163
		from_addr:你的邮箱账号
		password:你的邮箱密码，其中qq方式的发送password为授权码
		msg:你想要发送的内容，可以是html的方式
		kwargs:
			subtype:发送内容的格式----   'plain'---发送的文本内容，是默认值
										'html'----发送html方式
										'all'----用时支持以上两种方式
			html_msg----'all' 存在时生效，存储html方式的内容
	"""

	if not isinstance( type , str ) :
		raise ValueError( 'type is not a str, please input "qq","QQ","gmail","163"!' )
	if type == 'qq' or type == 'QQ' :
		if match( '^\w+@qq.com$' , from_addr ) is not None :
			pass
		else :
			raise ValueError( 'The email, %s , is not a %s email' % from_addr , type )
	if type == 'gmail' :
		if match( '^\w+@gmail.com$' , from_addr ) is not None :
			pass
		else :
			raise ValueError( 'The email, %s , is not a %s email' % from_addr , type )
	if type == '163' :
		if match( '^\w+@163.cn$' , from_addr ) is not None :
			pass
		else :
			raise ValueError( 'The email, %s , is not a %s email' % from_addr , type )


def qq_post(from_addr,password,to_addr,message):

