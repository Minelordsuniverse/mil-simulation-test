import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_thrust_profile():
    """Generate realistic missile thrust profile (N) over time (s)."""
    time = np.linspace(0, 120, 300)  # 120s flight, 300 points

    thrust = []
    for t in time:
        if t < 5:  # boost phase
            thrust.append(150000 * (1 - t/5))  # decreasing slightly
        elif t < 30:  # sustain
            thrust.append(80000)
        elif t < 60:  # coast/glide
            thrust.append(20000 * np.exp(-(t-30)/10))
        else:  # ballistic tail
            thrust.append(0)

    return pd.DataFrame({"time_s": time, "thrust_N": thrust})

