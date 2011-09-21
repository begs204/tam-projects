## Quantcast Scraping Module
## 9/15/11

import os, re, sys, urllib


##Parse inbound Text file of sites
def open_file(filename):
	site_list = []
	f = open(filename,'rU')
	for site in f:
		site_list.append(site.rstrip('\n'))
	f.close()
	return site_list

##Make sure HTML is formatted properly
def good_html(url_file):
	info = url_file.info()
	if info.gettype() == 'text/html': 
		utext = ufile.read()
		return utext
	else: 
		print 'Error - dis ain\'t formatted correctly'
		sys.exit(1)


##Contruct queries, ping quantcast, retrieve data, clean
def quant(site_list):
	
	stats = {}
	for url in site_list:
		ufile = urllib.urlopen('http://www.quantcast.com/' + url)
		info = ufile.info()
		
		##Ensures it's a text-based page
		if info.gettype() == 'text/html': 
			utext = ufile.read()
		else: 
			print 'Error - shit ain\'t formatted correctly'
			sys.exit(1)
		
		#print str(utext.index('id="demographic-tooltip"')) + ' start'
		#print str(utext.index('Audience Also Likes')) + ' finish'
		
		##Retrieve relevant substring
		utext_sub = utext[utext.index('id="demographic-tooltip"'):utext.index('id="simaudience-tooltip"')]
		utext_sub = utext_sub[utext_sub.index('<tbody>'):]
		param = {}
		
		##get all the different factoids
		cat_tuples = re.findall(r'<td class="digit">(\d+)%</td>\n<td class="title border">([\w\d\+\$\.\s-]+)</td>',utext_sub)
		for tuple in cat_tuples:
			param[tuple[1]] = tuple[0]
		
		stats[url] = param

	return stats


##Lifestyle Numbers
def LS_quant(site_list):

	stats = {}
	for url in site_list:
		ufile = urllib.urlopen('http://www.quantcast.com/' + url +'/lifestyle')

		utext = good_HTML(ufile)		
		utext_sub = utext[utext.index('<p class="caption">Data Source: United States Monthly</p>'):utext.index('<div id="footer">')] 
		param = {}
		
		cat_tuples = re.findall(r'<td>([\w\d\+\.\s/-]+)</td>\n<td class="digit">([\d\.+]+)x</td>',utext_sub)
		for tuple in cat_tuples:
			param[tuple[0]] = tuple[1]
			
		stats[url] = param
		return stats


##Reach Statistics		
def Reach_quant(site_list):
	stats = {}
	for url in site_list:
		ufile = urllib.urlopen('http://www.quantcast.com/' + url)
		info = ufile.info()
		
		##Ensures it's a text-based page
		if info.gettype() == 'text/html': 
			utext = ufile.read()
		else: 
			print 'Error - shit ain\'t formatted correctly'
			sys.exit(1)
		
		utext_sub = utext[utext.index('id="reach-wd'):utext.index('id="sparkline-wd:')]
		tuple = re.findall(r'">\n([\d\w\.]+)<p class="label">',utext_sub)
		
		stats[url] = tuple
	#print stats
	return stats

def main():
	args = sys.argv[1:]
	for filename in args:
		list_main = open_file(filename)
		stats_main = quant(list_main)
		stats_lifestyle = LS_quant(list_main)
		Reach_quant(list_main)

if __name__ == '__main__':
  main()