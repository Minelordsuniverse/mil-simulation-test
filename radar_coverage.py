import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_radar_specs():
    data = {
        "system": ["Fighter AESA", "AWACS", "SAM Radar", "Naval Radar"],
        "range_km": [180, 420, 320, 400],
        "frequency": ["X-band", "L-band", "S-band", "C-band"]
    }
    return pd.DataFrame(data)

def save_radar_csv(folder="inputs"):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, "radar_specs.csv")
    df = generate_radar_specs()
    df.to_csv(filepath, index=False)
    print(f"Generated radar specs: {filepath}")
    return filepath

def run_radar_coverage():
    csv_path = save_radar_csv()
    df = pd.read_csv(csv_path)

    plt.figure()
    plt.bar(df["system"], df["range_km"])
    plt.ylabel("Range (km)")
    plt.title("Radar Coverage Comparison")
    plt.savefig("outputs/radar_coverage.png")
    plt.close()
    print("Saved radar coverage plot(s) in outputs/radar_coverage.png")

def run():
    run_radar_coverage()
