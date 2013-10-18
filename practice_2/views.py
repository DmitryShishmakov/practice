# Задание: Представление, работающее по разным url
# # -*- coding: utf8 -*-
# from os import listdir
# from django.http import HttpResponse

# def listing(request, param):
# 		content = ""
# 		if(param == 'apt/'):
# 			items = listdir("/var/log/apt/")
# 		else:
# 			items = listdir("/var/log/")

# 		for item in items:
# 			content += item + "<br />"
# 		return HttpResponse(content)


# Задание: Ссылки на подкаталоги
# # -*- coding: utf8 -*-
# from os import listdir
# from os.path import isfile
# from django.shortcuts import render

# def listing(request, param):
# 		listFiles = []
# 		listDirs = []
# 		path = "/var/log/" + param
# 		items = listdir(path)

# 		for item in items:
# 			if(isfile(path + "/" + item)):
# 				listFiles.append(item)
# 			else:
# 				listDirs.append(item)

# 		context = {'listDirs': listDirs, 'listFiles' : listFiles}
# 		return render(request, 'listing.html', context)


