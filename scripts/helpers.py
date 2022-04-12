import numpy as np
import pandas as pd

def fill_interpolate_temporal(date_sorted_data):
    for i in range(len(date_sorted_data)):
        prev_val = date_sorted_data[i]
        j = i
        while date_sorted_data[j] is np.nan:
            j = j+1
        next_val = date_sorted_data[j]
        if prev_val is np.nan:
            for k in range(i, j):
                date_sorted_data[k] = next_val
        else:
            delta = (next_val - prev_val) / (j - i)
            for k in range(i, j):
                date_sorted_data[k] = prev_val + (k-i)*delta
        i = j

    return date_sorted_data
    