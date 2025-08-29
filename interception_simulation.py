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

