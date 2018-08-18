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
#from Users.views import session_check
#from Users.views import language_check
from PIL import Image, ExifTags
from User.views import session_check

# Create your views here.

@csrf_exempt
def Main(request):
	Template = get_template("Main/Base.html")
	Session = session_check(request)
	cu_test = '할렐루야'
        cu_test2 = 'dfdfdfdfdf'
	dic = {
		'MID_Page' : 'Main/Main.html',
		'cu_test' : cu_test,
		'Session' : Session,
	}

	return HttpResponse(Template.render(dic, request))
