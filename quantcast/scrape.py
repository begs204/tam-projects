## Quantcast Scraping Module
## 9/15/11

import os, re, sys, urllib
from xlsxcessive.xlsx import Workbook, save


##Parse inbound Text file of sites
def open_file(filename):
	site_list = []
	f = open(filename,'rU')
	for site in f:
		site_list.append(site.rstrip('\n'))
	f.close()
	return site_list

##Make sure HTML is formatted properly, return HTML string if true
def good_HTML(url_file):
	info = url_file.info()
	if info.gettype() == 'text/html': 
		utext = url_file.read()
		return utext
	else: 
		print 'Error - dis ain\'t formatted correctly'
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
	#print site_list
	stats = {}
	for url1 in site_list:
		ufile = urllib.urlopen('http://www.quantcast.com/' + url1 +'/lifestyle')

		utext = good_HTML(ufile)		
		utext_sub = utext[utext.index('<p class="caption">Data Source: United States Monthly</p>'):utext.index('<div id="footer">')] 
		param = {}
		
		cat_tuples = re.findall(r'<td>([\w\d\+\.\s/-]+)</td>\n<td class="digit">([\d\.+]+)x</td>',utext_sub)
		for tuple in cat_tuples:
			param[tuple[0]] = tuple[1]
			
		stats[url1] = param
	return stats


##Reach Statistics		
def Reach_quant(site_list):
	stats = {}
	for url in site_list:
		ufile = urllib.urlopen('http://www.quantcast.com/' + url)
		
		utext = good_HTML(ufile)
		utext_sub = utext[utext.index('id="reach-wd'):utext.index('id="sparkline-wd:')]
		tuple = re.findall(r'">\n([\d\w\.]+)<p class="label">',utext_sub)
		
		stats[url] = tuple
	return stats



##Generate Excel File
def gen_xlsx(list_main, stats_dem, stats_lifestyle, stats_reach, workbook):
	sheet_dict = {}
	sheet_count = 1
	
	##Each URL in the provided input file
	for site in list_main:
		sheet_dict[site] = workbook.new_sheet(site)
		sheet_dict[site].cell(coords=(0,0), value=site)
		
		sheet_dict[site].cell(coords=(2,0), value = 'Demographic Stats')
		sheet_dict[site].cell(coords=(2,3), value = 'Reach Stats')
		sheet_dict[site].cell(coords=(2,6), value = 'LifeStyle Stats')
		
		sheet_dict[site].cell(coords=(2,1), value = '%')
		sheet_dict[site].cell(coords=(2,4), value = 'Monthly Uniques')
		sheet_dict[site].cell(coords=(2,7), value = 'Affinity')
		
		##Demographic Stats
		row_dem = 2; col_dem = 0
		for key1 in stats_dem[site].iterkeys():
			sheet_dict[site].cell(coords=(row_dem,col_dem), value=key1) ##Key
			sheet_dict[site].cell(coords=(row_dem,col_dem + 1), value=stats_dem[site][key1]) ##Value
			row_dem += 1
		
		##Reach Stats - Not stored in list, not dict
		row_reach = 3; col_reach = 3
		for key2 in stats_reach[site]:
			if row_reach == 3:
				sheet_dict[site].cell(coords=(row_reach,col_reach), value='US') ##Key
			elif row_reach == 4:
				sheet_dict[site].cell(coords=(row_reach,col_reach), value='Global') ##Key
			else:
				sheet_dict[site].cell(coords=(row_reach,col_reach), value='N/A') ##Key
			sheet_dict[site].cell(coords=(row_reach,col_reach+1), value=key2) ##Value
			row_reach +=1	

		##Lifestyle Stats
		row_lifestyle = 3; col_lifestyle = 6
		for key3 in stats_lifestyle[site].iterkeys():
			sheet_dict[site].cell(coords=(row_lifestyle,col_lifestyle), value=key3) ##Key
			sheet_dict[site].cell(coords=(row_lifestyle,col_lifestyle + 1), value=stats_lifestyle[site][key3]) ##Value
			row_lifestyle +=1			
			
	sheet_count +=1	
	save(workbook, 'test_file.xlsx')
	
	
	

def main():	
	args = sys.argv[1:]
	for filename in args:
		list_main = open_file(filename)
		stats_dem = quant(list_main)
		stats_lifestyle = LS_quant(list_main)
		stats_reach = Reach_quant(list_main)

		##Instantiate and compose the Excel File
		workbook = Workbook()		
		gen_xlsx(list_main, stats_dem, stats_lifestyle, stats_reach, workbook)
		

		
if __name__ == '__main__':
  main()