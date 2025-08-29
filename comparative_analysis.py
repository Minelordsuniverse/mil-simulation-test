import os
import pandas as pd
import matplotlib.pyplot as plt

# using predetermined value inputs
def generate_comparison_data():
    data = {
        "system": ["Blue SAM (Patriot)", "Red SAM (S-400)", "Blue Fighter (AMRAAM)", "Red Fighter (R-37)"],
        "range_km": [70, 250, 100, 300],
        "speed_mach": [4.0, 5.0, 4.0, 6.0]
    }
    return pd.DataFrame(data)
