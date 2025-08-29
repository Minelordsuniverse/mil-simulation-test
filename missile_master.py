import argparse
import os

# Imports each module from the respective files
import trajectory_simulation 
import radar_coverage
import interception_simulation
import comparative_analysis

def ensure_folders():
    os.makedirs("inputs", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

def main():
    print("Missile Simulation Suite")
    ensure_folders()

    print("\n[1] Running trajectory simulation...")
    trajectory_simulation.run()

    print("\n[2] Running radar coverage analysis...")
    radar_coverage.run()

    print("\n[3] Running interception simulation...")
    interception_simulation.run()

    print("\n[4] Running comparative analysis...")
    comparative_analysis.run()

    print("All simulations complete!")
    print("Generated files:")
    print("  - Inputs (CSV): stored in ./inputs/")
    print("  - Outputs (plots): stored in ./outputs/")

if __name__ == "__main__":
    main()
