## Demo Wizard
## 10/18/11

##Notes:
# Have every name of the button be able to input from command line
#designate file path, button names

import os, sys, re, urllib, array
from PIL import Image
from jb_iframe import *

##Generate Demo Script
def generate(network,button_list):
	filename = 'demo_template.js'
	embed_read = open(filename,'rU').read()#.replace('\n','')

	button_text = embed_read[embed_read.index('Meebo(\'addButton'):] #button code
	header = embed_read[:embed_read.index('Meebo(\'addButton')].replace('<>network<>',network) #replace network variable
	button_dict = {}

	mb_id_list = map(chr, range(97,123)); mb_index = 0 ##list of letters
	for button in button_list:
		new_button_text = button_text

		mb_id = mb_id_list[mb_index]
		new_button_text1 = new_button_text.replace('<>id<>',mb_id)
		new_button_text2 = new_button_text1.replace('<>label<>', button)	

		name = button.lower().replace(' ','').strip().replace('\'','').replace(',','').replace('.','')
		new_button_text3 = new_button_text2.replace('<>icon<>', network + '/' + 'icon_' + name + '.png')
		new_button_text4 = new_button_text3.replace('<>image<>', network + '/' + name + '.png')

		files = os.listdir('../'+network)
		if name+'.png' in files:
			new_button_text5 = new_button_text4.replace('<>px_w<>', str(image_px('../'+network+'/'+name+'.png')[0] + 2))
			new_button_text6 = new_button_text5.replace('<>px_h<>', str(image_px('../'+network+'/'+name+'.png')[1] + 2))
		else:
			print 'Couldn\'t locate image files' + name
			sys.exit(1)	
		button_dict[button] = new_button_text6; new_button_text = ''
		mb_index += 1
	
	t = header
	for item in button_dict.keys():
		t+= button_dict[item]
	t+='Meebo(\'domReady\'); '
	return t
		
		

def save_file(network,button_list):
	script = generate(network,button_list)
	n_file = open('../'+network+'/'+network+'.js','w')
	n_file.write(script)
	n_file.close()

##Determine image dimensions
def image_px(pic):
	im = Image.open(pic)
	px = im.size
	return px

def main():
	args = sys.argv[1:]
	network = args[0]
	url = args[1]
	button_list = []
	for button in args[2:]:
		button_list.append(button)
	save_file(network,button_list)
	iframe_web(network,url)
if __name__ == '__main__':
	main()