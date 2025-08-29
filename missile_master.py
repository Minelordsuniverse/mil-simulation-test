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

