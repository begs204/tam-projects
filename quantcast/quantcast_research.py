## Quantcast Scraping Module
## 9/28/11

import os, re, sys, urllib
from xlsxcessive.xlsx import Workbook, save


##Parse inbound Text file of sites
def open_file(filename):
	site_list = []
	f = open(filename,'rU')
	for site in f:
		site_list.append(site.rstrip('\n').strip().lower())
	f.close()
	return site_list

##Make sure HTML is formatted properly, return HTML string if true
def good_HTML(url_file):
	info = url_file.info()
	if info.gettype() == 'text/html': 
		utext = url_file.read()
		return utext
	else: 
		print 'Error - file not formatted properly'
		sys.exit(1)


##Contruct queries, ping quantcast, retrieve data, clean
def quant(site_list):
	
	stats = {}
	for url in site_list:
		ufile = urllib.urlopen('http://www.quantcast.com/' + url)
		
		#print str(utext.index('id="demographic-tooltip"')) + ' start'
		#print str(utext.index('Audience Also Likes')) + ' finish'
		
		##Retrieve relevant substring
		utext = good_HTML(ufile)
		if not (re.search('id="demographic-tooltip"',utext) and re.search('id="simaudience-tooltip"',utext)):
			print 'Could not locate Demographic Statistics for ' + url
			continue ##Error Handling
			
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
	for url1 in site_list:
		ufile = urllib.urlopen('http://www.quantcast.com/' + url1 +'/lifestyle')

		utext = good_HTML(ufile)
		if not (re.search('<p class="caption">Data Source: United States Monthly</p>',utext) and re.search('<div id="footer">',utext)):
			print 'Could not locate Lifestyle Statistics for ' + url
			continue ##Error Handling
		
		utext_sub = utext[utext.index('<p class="caption">Data Source: United States Monthly</p>'):utext.index('<div id="footer">')] 
		param = {}
		
		cat_tuples = re.findall(r'<td>([\w\d\+\.\s/-]+)</td>\n<td class="digit">([\d\.+]+)x</td>',utext_sub)
		for tuple in cat_tuples:
			param[tuple[0]] = float(tuple[1])
		
		stats[url1] = param
	return stats


##Generate Excel File
def gen_xlsx(list_main, stats_dem, stats_lifestyle, workbook, name):
	sheet_dict = {}
	sheet_dict['Research'] = workbook.new_sheet('Research')
	
	site_row = 3; index_dem = 1; 
	dem_dict = {}
	ls_dict = {}
	
	##Determine How many distinct Demographic fields are present
	dem_max_dict = []; dem_max_index = 1
	for site2 in list_main:
		for key_dem in stats_dem[site2].iterkeys():
			if	key_dem not in dem_max_dict:
				dem_max_dict.append(key_dem)
				dem_max_index +=1
	
	##Each URL in the provided input file
	for site in list_main:
		sheet_dict['Research'].cell(coords=(site_row,0), value=site)
		
		##Demographic Info
		for key1 in stats_dem[site].iterkeys():
		
			##Check if Parameter has been added
			if key1 not in dem_dict.keys():
				sheet_dict['Research'].cell(coords=(2,index_dem), value=key1) ## Add Key
				sheet_dict['Research'].cell(coords=(site_row,index_dem), value=stats_dem[site][key1]) ##Value
				dem_dict[key1] = index_dem
				index_dem +=1
			else:
				prev_index = dem_dict[key1] ##index of parameter that has been added already
				sheet_dict['Research'].cell(coords=(site_row,prev_index), value=stats_dem[site][key1]) ##Value
		
		index_ls = dem_max_index + 2; prev_index = -1
		##Lifestyle Stats
		for key2 in stats_lifestyle[site].iterkeys():
		
			##Check if Parameter has been added
			if key2 not in ls_dict.keys():
				sheet_dict['Research'].cell(coords=(2,index_ls), value=key2) ## Add Key
				sheet_dict['Research'].cell(coords=(site_row,index_ls), value=stats_lifestyle[site][key2]) ##Value
				ls_dict[key2] = index_ls
				index_ls +=1
			else:
				prev_index = ls_dict[key2] ##index of parameter that has been added already
				sheet_dict['Research'].cell(coords=(site_row,prev_index), value=stats_lifestyle[site][key2]) ##Value
			
		site_row +=1
	save(workbook, name + '.xlsx')
	
	
def main():	
	args = sys.argv[1:]
	for filename in args:
		list_main = open_file(filename)
		stats_dem = quant(list_main)
		stats_lifestyle = LS_quant(list_main)

		##Instantiate and compose the Excel File
		workbook = Workbook()		
		name = filename[:filename.index('.')]
		gen_xlsx(list_main, stats_dem, stats_lifestyle, workbook, name)
		

		
if __name__ == '__main__':
  main()