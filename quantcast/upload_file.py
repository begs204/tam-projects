#!/usr/local/bin/python
#Upload Text File from web server
#9/22/11

import cgitb, urllib2, cgi

cgitb.enable()
form = cgi.FieldStorage()

fileitem = form["myfile"]
if fileitem.file:
	linecount = 0
	while 1:
		line = fileitem.file.readlines()
		if not line: break
		linecount += 1