import os, sys, re, urllib, array

t1 = open('t1.txt','rU').read().replace('\n','')
t2 = open('t2.txt','rU').read().replace('\n','').replace(' ','')

index = 0
for char in t2:
	if char !=t1[index]:
		print index, char
		break
	index+=1