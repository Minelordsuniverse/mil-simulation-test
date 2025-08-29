import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_interception_cases():
    target_speeds = [0.9, 1.5, 2.0, 2.5, 3.0]  # Mach
    interceptor_speeds = [3.0, 4.0, 5.0]       # Mach
    rows = []

    for v_t in target_speeds:
        for v_i in interceptor_speeds:
            pk = max(0.2, min(0.95, 1 - (v_t / (v_i * 1.5))))  # simple model
            rows.append({"target_speed_mach": v_t,
                         "interceptor_speed_mach": v_i,
                         "p_kill": round(pk, 2)})

    return pd.DataFrame(rows)

def save_interception_csv(folder="inputs"):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, "interception_cases.csv")
    df = generate_interception_cases()
    df.to_csv(filepath, index=False)
    print(f"Generated interception cases: {filepath}")
    return filepath

def run_interception():
    csv_path = save_interception_csv()
    df = pd.read_csv(csv_path)

    plt.figure()
    for v_i in df["interceptor_speed_mach"].unique():
        subset = df[df["interceptor_speed_mach"] == v_i]
        plt.plot(subset["target_speed_mach"], subset["p_kill"], marker="o", label=f"Interceptor Mach {v_i}")

    plt.xlabel("Target Speed (Mach)")
    plt.ylabel("Probability of Kill")
    plt.title("Interception Effectiveness")
    plt.legend()
    plt.savefig("outputs/interception_sim.png")
    plt.close()
    print("Saved interception plot: outputs/interception_sim.png")

def run():
    run_interception()
