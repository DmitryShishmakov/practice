# -*- coding: utf8 -*-
from os import listdir
from django.http import HttpResponse

def listing(request, param):
		content = ""
		if(param == 'apt/'):
			items = listdir("/var/log/apt/")
		else:
			items = listdir("/var/log/")

		for item in items:
			content += item + "<br />"
		return HttpResponse(content)
