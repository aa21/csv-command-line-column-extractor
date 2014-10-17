#!/usr/bin/python

import csv, sys
from collections import defaultdict

# file, col, write, delim, quote


print "\n file, col, write=w, delim, quote  \n"


if 1 < len(sys.argv):
	file = str(sys.argv[1])
else:
	exit('No filename given.') 

if 2 < len(sys.argv):
	arg2 = str(sys.argv[2])
	if arg2.startswith('t'):
		sample = True
		if arg2.find(",") != -1:
			bits = arg2[1:].split(",")
			scols = int(bits[0])
			ssize = int(bits[1])
		elif len(arg2[1:]) >0 :
			scols = int(arg2[1:])
			ssize = 5
		else:
			scols = 5
			ssize = 5

	else:
		col = int(sys.argv[2])
else:
	exit('No Column number.') 

if 3 < len(sys.argv):
	if(str(sys.argv[3]) == 'w'):
		write = True
else:
	write = False 

if 4 < len(sys.argv):
	delim = str(sys.argv[4])
else:
	delim = ','

if 5 < len(sys.argv):
	quote = str(sys.argv[5])	
else:
	quote = '"'



reader = csv.reader(open(file, "rU"), delimiter=delim, quotechar=quote) 


if sample:
	columns = defaultdict(list)
	reader.next()

	s = 0

	for row in reader:
		c = 0
		for (i,v) in enumerate(row):
			columns[i].append(v)
			c += 1
			if c>=scols:
				break;
		s += 1
		if s>= ssize:
			break;

	for d in columns: 
		print str(d) + ": " + str(columns[d]) 

	exit()

if write:
	new_file = open(file+'_EMAILS', "w")

for row in reader:
	if not write:
		if col < len(row):
			print row[col]
	else:
		new_file.write(row[col] + "\n")


if write:
	new_file.close()
	print file+'_EMAILS written'

print "\n"
