
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
import ftplib
import hashlib
import MySQLdb
import os.path

db = MySQLdb.connect(user='root', db='Ich_shopping', passwd='dlsxjspt7510', host='localhost', charset="utf8")
Query = "SELECT * FROM USER;"
cursor=db.cursor()
cursor.execute("set names utf8")
cursor.execute(Query)
result=cursor.fetchall()
print(result)
'''
for i in result:
	print(i)
	print("\n")
'''