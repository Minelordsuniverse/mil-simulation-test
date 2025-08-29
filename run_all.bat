@echo off
REM Run all missile analysis modules

python missile_master.py --mode trajectory --thrust-csv inputs\thrust.csv
python missile_master.py --mode nez
python missile_master.py --mode radar
python missile_master.py --mode report

pause
