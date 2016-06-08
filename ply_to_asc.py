#!/usr/bin/python

import sys
import re

if (len(sys.argv) != 3):
	print 'please give exactly 2 arguments'
	print 'usage: python ply_to_asc.py [input filename] [output filename]'
	exit(0)
regex = re.compile('^([\-\.0-9]+) ([\-\.0-9]+) ([\-\.0-9]+).*$')

w = open(sys.argv[2], "w+")

with open(sys.argv[1]) as f:
	for line in f:
		m = regex.match(line)
		if m:
			w.write("%s %s %s\n" % (m.group(1), m.group(2), m.group(3)))


