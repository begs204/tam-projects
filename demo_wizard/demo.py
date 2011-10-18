## Demo Wizard
## 10/18/11

##Notes:
# Have every name of the button be able to input from command line

import os, sys, re, urllib, array
from PIL import Image

##Parse inbound Text file
def open_file(filename):
	button_list = []
	f = open(filename, 'rU')
	for button in f:
		button_list.append(button.rstrip('\n').strip())
	f.close()
	return button_list

##Extract Parameter Names
def value_extract(button_list):
	count = 0; site_param = {}; b_param = {}
	for b in button_list:
		if count == 0 and b.find('network') > -1:
			##Network and Site Name
			site_param = re.findall(r':\'([\w\d\+\.\s/-]+)',b) 
		else:
			##Button Parameters
			name = b[:b.index(';')] #Button Name
			b = b[b.index(';')+1:].strip() #substring of images
			b_param[name] = [b[:b.index(';')].strip(), b[b.index(';')+1:].strip()]
			if image_px(b_param[name][1]):
				img = image_px(b_param[name][1])
				b_param[name].append(img)
				#print b_param[name], name, b_param[name][2][0]
	return site_param, b_param

##Determine image dimensions
def image_px(pic):
	im = Image.open(pic)
	px = im.size
	return px

##Generate Demo Script
def generate(site_param,b_param):
	embed1 = open('embed1.txt','rU').read().replace(' ','').replace('\n','')
	embed = embed1 + site_param[0]+'\"});'

	mb_id = map(chr, range(97,123)); mb_index = 0
	for button in b_param.iterkeys():
	






def main():
	args = sys.argv[1:]
	for filename in args:
		button_list = open_file(filename)
		[site_param, b_param] = value_extract(button_list)
		generate(site_param, b_param)

if __name__ == '__main__':
	main()