#!/usr/bin/python

import csv, sys

# file, col, write, delim, quote


print "\n file, col, write=w, delim, quote  \n"


if 1 < len(sys.argv):
	file = str(sys.argv[1])
else:
	exit('No filename given.') 

if 2 < len(sys.argv):
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

if write:
	new_file = open(file+'_EMAILS', "w")

for row in reader:
	if not write:
		print row[col]
	else:
		new_file.write(row[col] + "\n")


if write:
	new_file.close()
	print file+'_EMAILS written'

print "\n"
