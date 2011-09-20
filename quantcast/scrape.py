## Quantcast Scraping Module
## 9/15/11

import os
import re
import sys
import urllib

##Parse inbound Text file of sites
def open_file(filename):
	site_list = []
	f = open(filename,'rU')
	for site in f:
		site_list.append(site.rstrip('\n'))
	f.close()
	return site_list


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
		utext_sub = utext[utext.index('US Demographics'):utext.index('<h4>Audience Also Likes')] #start:end
		utext_sub = utext_sub[utext_sub.index('<tbody>'):]
		param = {}
		
		##get all the different factoids
		cat_tuples = re.findall(r'<td class="digit">(\d+)%</td>\n<td class="title border">([\w\d\+\$\.\s-]+)</td>',utext_sub)
		for tuple in cat_tuples:
			param[tuple[1]] = tuple[0]
		
		stats[url] = param

	for stat in stats:
		print stat, stats[stat]
	#return stats

		
		


def main():
	args = sys.argv[1:]
	for filename in args:
		list_main = open_file(filename)
		quant(list_main)

if __name__ == '__main__':
  main()