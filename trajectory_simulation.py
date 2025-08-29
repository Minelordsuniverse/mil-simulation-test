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

def save_thrust_csv(folder="inputs"): # Will generate input CSV values, can be edited later to determine your desired outcomes/can save a test CSV file for reference
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, "thrust.csv")
    df = generate_thrust_profile()
    df.to_csv(filepath, index=False)
    print(f"[INFO] Generated thrust profile: {filepath}")
    return filepath

def run_trajectory_simulation():
    csv_path = save_thrust_csv()
    df = pd.read_csv(csv_path)

    plt.figure()
    plt.plot(df["time_s"], df["thrust_N"], label="Thrust (N)")
    plt.xlabel("Time (s)")
    plt.ylabel("Thrust (N)")
    plt.title("Missile Thrust Profile")
    plt.legend()
    plt.savefig("outputs/thrust_profile.png")
    plt.close()
    print("Saved thrust profile plot(s) in outputs/thrust_profile.png")

def run():
    run_trajectory_simulation()
