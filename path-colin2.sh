#!/bin/bash

## COLIN2 Path Planning

# Wrapper for COLIN2 Path Planning.
#

# Usage: ./path-colin2.sh problem-dir map-file
#

# Directory Cleanup
rm $1/* > /dev/null 2>&1

# Map file setup
if [ $2 ]; then
	map=$2
else
	map=map0.csv
fi

# Copying files
cp ${map} $1/map.csv
cp domain.pddl $1/

# Generating problem file
python gen-problem.py $1

# Planning
~/dev/colin2/plan $1/domain.pddl $1/problem.pddl $1/solution $1/timing > /dev/null 2>&1

# VAL PDF
${TOOLS}val-report.sh $1

# Generating Graphics
python plot-plan.py $1

# Viewing Graphics
evince $1/graphics.eps &

