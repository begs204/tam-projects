## Demo Wizard
## 10/18/11

##Notes:
# Have every name of the button be able to input from command line
#designate file path, button names

import os, sys, re, urllib, array, pickle
from PIL import Image


##Determine image dimensions
def image_px(pic):
	im = Image.open(pic)
	px = im.size
	return px

##Generate Demo Script
def generate(f_path, network,button_list):
	embed_read = open('embed1_test.txt','rU').read().replace('\n','')
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
		
		if f_path+ '/' + network+ '/'+name+'.png' in os.listdir('..'):
				print 'heya'
		print os.listdir('..')
		##new_button_text.replace('<>px_w<>',image_px(f_path+ '/' + network+ '/'+name+'.png')[0])
		##new_button_text.replace('<>px_h<>',image_px(f_path+ '/' + network+ '/'+name+'.png')[1])

		button_dict[button] = new_button_text4
		new_button_text = ''; mb_index +=1
	#print button_dict
	
	#embed_final = embed + 'Meebo(\'domReady\');'
	#return embed_final

def save_file(f_path,network,button_list):
	text = generate(f_path,network,button_list)
	#print text
	n_file = open('..' + f_path+'/'+network+ '/' +network+ '.js','w') #create JS file
	pickle.dump(text,n_file)
	n_file.close()


def main():
	args = sys.argv[1:]
	f_path =  args[0].rpartition('/')[0]; network = args[0].rpartition('/')[2]
	button_list = []
	for button in args[1:]:
		button_list.append(button)
	#generate(filepath,network,button_list)
	save_file(f_path,network,button_list)


if __name__ == '__main__':
	main()

# ##Extract Parameter Names
# def value_extract(button_list):
# 	count = 0; site_param = {}; b_param = {}
# 	for b in button_list:
# 		if count == 0 and b.find('network') > -1:
# 			##Network and Site Name
# 			site_param = re.findall(r':\'([\w\d\+\.\s/-]+)',b) 
# 		else:
# 			##Button Parameters
# 			name = b[:b.index(';')] #Button Name
# 			b = b[b.index(';')+1:].strip() #substring of images
# 			b_param[name] = [b[:b.index(';')].strip(), b[b.index(';')+1:].strip()]
# 			if image_px(b_param[name][1]):
# 				img = image_px(b_param[name][1])
# 				b_param[name].append(img)
# 				#print b_param[name], name, b_param[name][2][0]
# 	return site_param, b_param

# def main():
# 	args = sys.argv[1:]
# 	for filename in args:
# 		button_list = open_file(filename)
# 		[site_param, b_param] = value_extract(button_list)
# 		generate(site_param, b_param)


# ##Parse inbound Text file
# def open_file(filename):
# 	button_list = []
# 	f = open(filename, 'rU')
# 	for button in f:
# 		button_list.append(button.rstrip('\n').strip())
# 	f.close()
# 	return button_list

