#!/usr/bin/env python
import csv
import sys



# Checking input args
if len(sys.argv) < 2:
	print "Missing args.\nUsage:\n./gen-prob.py problem-dir"
	exit(0)

# Buffers
start_pos	=""
final_pos	=""
cells 		= ""
empty 		= ""
conn 		= ""

# File paths
file_map = sys.argv[1]+"/map.csv"
file_pro = sys.argv[1]+"/problem.pddl"

# Map file reading loop
print "Reading map file %s" % file_map
with open(file_map, 'rb') as csvfile:
	csv_data = list(csv.reader(csvfile))
	num_rows = len(csv_data)
	for i, row in enumerate(csv_data):
		num_cols = len(row)
		for j, cell in enumerate(row):

			# All cells
			cells+='		p_%02d_%02d - pos\n' % (i,j)

			# Empty cells
			if cell!='#':
				empty+='		(empty p_%02d_%02d)\n' % (i,j)

			# Start position
			if cell=='S':
				start_pos='p_%02d_%02d' % (i,j)

			# Final position
			if cell=='F':
				final_pos='p_%02d_%02d' % (i,j)

			# Horizontal connections
			if j+1 < num_cols:
				conn+='		(next p_%02d_%02d p_%02d_%02d)\n' % (i,j,i,j+1)
				conn+='		(next p_%02d_%02d p_%02d_%02d)\n' % (i,j+1,i,j)

			# Vertical connections
			if i+1 < num_rows:
				conn+='		(next p_%02d_%02d p_%02d_%02d)\n' % (i+1,j,i,j)
				conn+='		(next p_%02d_%02d p_%02d_%02d)\n' % (i,j,i+1,j)

out = "(define (problem rovers_prob) (:domain rovers)\n	(:objects \n		r - rover\n"
out+=cells
out+="		)\n\n	(:init\n		(idle r)\n		(at r %s)\n" % start_pos
out+=empty
out+=conn
out+="		)\n	(:goal (and\n		(at r %s)\n		)\n	)\n	(:metric minimize total-time)\n	)\n" % final_pos

# Writting output problem file
print "Writting problem file %s" % file_pro
with open(file_pro, 'w') as f:
	f.write(out)

