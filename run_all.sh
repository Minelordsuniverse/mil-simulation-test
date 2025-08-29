#!/bin/bash
# Run all missile analysis modules

python3 missile_master.py --mode trajectory --thrust-csv inputs/thrust.csv
python3 missile_master.py --mode nez
python3 missile_master.py --mode radar
python3 missile_master.py --mode report
