#!/usr/bin/env python3
import csv
import sys
import re
from pyx import *

# Checking input args
if len(sys.argv) < 2:
	print "Missing args.\nUsage:\n./gen-prob.py problem-dir"
	exit(0)

# File paths
file_map = sys.argv[1]+"/map.csv"
file_sol = sys.argv[1]+"/solution"
file_gra = sys.argv[1]+"/graphics.eps"

# Prefix
c = canvas.canvas()

def draw_block( i, j, col=color.rgb.black, label=r"" ):
	c.draw(path.rect(j, i, 1, 1), [deco.filled([col])])
	c.text(j+0.5, i+0.5, label,[text.halign.center,text.valign.middle,text.size.Large])

# Map file reading loop
print "Reading map file %s" % file_map
with open(file_map, 'rb') as csvfile:
	csv_data = csv.reader(csvfile)
	for i, row in enumerate(csv_data):
		for j, cell in enumerate(row):

			# Walls
			if cell=='#':
				draw_block(i,j)

			# Start position
			elif cell=='S':
				draw_block(i,j,color.rgb.green, r"")

			# Final position
			elif cell=='F':
				draw_block(i,j,color.rgb.blue, r"")

# Plan file reading loop
print "Reading plan file %s" % file_sol
with open(file_sol, 'rb') as f:
	for line in f:
		pos = re.findall('p_\d+_\d+', line)
		if len(pos) > 0:
			[p0i,p0j] = re.findall('\d+', pos[0])
			[p1i,p1j] = re.findall('\d+', pos[1])
			[p0i,p0j] = [int(p0i)+0.5,int(p0j)+0.5]
			[p1i,p1j] = [int(p1i)+0.5,int(p1j)+0.5]
			c.stroke(path.line(p0j,p0i,p1j,p1i),[deco.earrow(angle=45)])

#  Writing to file
print "Writting graphics file %s" % file_gra
c.writeEPSfile(file_gra)
