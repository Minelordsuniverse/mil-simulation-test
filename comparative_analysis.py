import os
import pandas as pd
import matplotlib.pyplot as plt

# sample/example, using predetermined value inputs
def generate_comparison_data():
    data = {
        "system": ["Blue SAM (Patriot)", "Red SAM (S-400)", "Blue Fighter (AMRAAM)", "Red Fighter (R-37)"],
        "range_km": [70, 250, 100, 300],
        "speed_mach": [4.0, 5.0, 4.0, 6.0]
    }
    return pd.DataFrame(data)

def save_comparison_csv(folder="inputs"):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, "comparison_data.csv")
    df = generate_comparison_data()
    df.to_csv(filepath, index=False)
    print(f"Generated comparison data: {filepath}")
    return filepath

def run_comparison():
    csv_path = save_comparison_csv()
    df = pd.read_csv(csv_path)

    plt.figure()
    plt.bar(df["system"], df["range_km"])
    plt.ylabel("Range (km)")
    plt.title("Blue vs Red Systems: Range")
    plt.xticks(rotation=15)
    plt.savefig("outputs/comparison_range.png")
    plt.close()

    plt.figure()
    plt.bar(df["system"], df["speed_mach"])
    plt.ylabel("Speed (Mach)")
    plt.title("Blue vs Red Systems: Speed")
    plt.xticks(rotation=15)
    plt.savefig("outputs/comparison_speed.png")
    plt.close()
    print("Saved comparison plots.")

def run():
    run_comparison()
