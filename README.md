# mil-simulation-test
NOTE: THIS IS JUST A TEST/SAMPLE USING PLACEHOLDER VALUES, AND THIS PROJECT IS ONLY MEANT FOR REFERENCE/EDUCATIONAL PURPOSES.

# Missile Simulation & Analysis Project

This project simulates missile trajectories, **No Escape Zone (NEZ)** sensitivity, and **radar detection/coverage analysis** for both sides (attacker and defender), taking into account missile statistics.
It also generates a consolidated report with plots and tables.

## Project Structure
mil-simulation-test/
├── inputs/ # CSV inputs (comparison data, interception, radar, thrust values)
├── outputs/ # Auto-generated plots (range comparisons, speed comparisons, thrust profiles, interception sims)
├── plots/ # Auto-generated plots for nez+radar+trajectory
├── tables/ # Auto-generated tables
├── trajectory_simulation.py # Simulates missile kinematics
├── radar_coverage.py # Radar detection vs RCS/altitude
├── comparative_analysis.py # Merges results into summary report
├── missile_master.py # Master CLI script (main entry point)
├── run_all.sh # Unix shell runner
└── run_all.bat # Windows batch runner
