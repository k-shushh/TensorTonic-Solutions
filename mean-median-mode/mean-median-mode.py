import numpy as np
from scipy import stats

def mean_median_mode(x):
    np_array = np.array(x)

    mean = float(np.mean(np_array))
    median = float(np.median(np_array))
    mode = float(stats.mode(np_array, keepdims=False).mode)

    return mean, median, mode