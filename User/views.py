# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
import string, string, math, time, os, glob, shutil, re, urllib, json
from django.views.decorators.csrf import csrf_exempt
import random
from importlib import reload
import sys
reload(sys)
import glob
import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta
import requests
import bleach
from flask import Flask, request, render_template, redirect
import flask
from django.contrib.auth import logout
import ftplib
import hashlib
import MySQLdb
import os.path


# Create your views here.
@csrf_exempt
def Signup(request):
	Template = get_template("Main/Base.html")
	Session = session_check(request)
	cu_test = '할렐루야'
	dic = {
		'MID_Page':'User/Signup.html',
		'Session':Session,
		'cu_test' : cu_test,
	}

	return HttpResponse(Template.render(dic, request))

@csrf_exempt
def ID_Check(request):
	Template = get_template("User/ID_Check.html")
	Session = session_check(request)

	userid = request.GET['id']

	db = MySQLdb.connect(user='root', db='Ich_shopping', passwd='dlsxjspt7510', host='localhost', use_unicode=True, charset="utf8")

	Query = "SELECT COUNT(u_id) FROM `USER` WHERE u_id = '" + userid + "';"
	cursor = db.cursor()
	cursor.execute("set names utf8")
	cursor.execute(Query)

	checked = cursor.fetchone()

	checked = int(checked[0])

	dic = {
		'Session':Session,
		'checked':checked,
		'userid':userid,
	}

	return render_to_response('User/ID_Check.html', dic)

@csrf_exempt
def signup_process(request):
	db = MySQLdb.connect(user='root', db='Ich_shopping', passwd='dlsxjspt7510', host='localhost', charset="utf8")
	ID = request.POST['id']
	PW = request.POST['pw']
	Name = request.POST['name']

	idtype = type(ID)
	
	Query = "INSERT INTO USER (`u_id`, `pw`, `name`) VALUES ('%s','%s', '%s');"%(ID, PW, Name)
	cursor = db.cursor()
	#asdf.append("1")
	cursor.execute(Query)
	db.commit()
	return HttpResponse("<script type='text/javascript'> alert('You have successfully signed up. Please log in.');location.href='/';</script>")

@csrf_exempt
def Login(request):
	Template = get_template("Main/Base.html")
	Session = session_check(request)
	cu_test = '할렐루야'
	dic = {
		'MID_Page':'User/Login.html',
		'Session':Session,
		'cu_test' : cu_test,
	}

	return HttpResponse(Template.render(dic, request))

@csrf_exempt
def login_process(request):
	db = MySQLdb.connect(user='root', db='Ich_shopping', passwd='dlsxjspt7510', host='localhost', charset="utf8")
	ID = request.POST['id']
	PW = request.POST['pw']

	Query = "SELECT * FROM USER WHERE `u_id`='%s' AND `pw`='%s';"%(ID,PW)

	cursor = db.cursor()
	cursor.execute("set names utf8")
	cursor.execute(Query)
	userinfo = cursor.fetchone()
	if userinfo is None:
		Session = -1
		return HttpResponse("<script type='text/javascript'> alert('Login Failed! Invalid ID and/or Password, Please try again');history.go(-1);</script>")

	else :		
		request.session['id'] = userinfo[1]
		request.session['username'] = userinfo[3]

		Session = session_check(request)

	return HttpResponse("<script type='text/javascript'> alert('로그인성공');location.href='/';</script>")

def session_check(request):
	session = -1
	if request.session.has_key('id') :
		session = []		
		session.append(request.session['id'])
		session.append(request.session['username'])
		
	return session

@csrf_exempt
def logout_process(request):
	logout(request)
	Session = -1


	return HttpResponse("<script type = 'text/javascript'> alert('로그아웃 되었습니다.');location.href='/';</script>")

@csrf_exempt
def Encoding_test(request):
	Template = get_template("Main/Base.html")
	Session = session_check(request)
	db = MySQLdb.connect(user='root', db='Ich_shopping', passwd='dlsxjspt7510', host='localhost', charset="utf8")
	Query = "SELECT * FROM USER;"
	cursor=db.cursor()
	cursor.execute(Query)
	result=cursor.fetchall()
	dic = {
		'MID_Page':'User/Encoding_test.html',
		'result':result,
	}

	return HttpResponse(Template.render(dic, request))