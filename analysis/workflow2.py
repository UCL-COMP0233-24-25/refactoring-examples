import numpy as np
from utils import read_file, sum_weighted_diffs

if __name__ == "__main__":
    data1 = read_file("samples1.csv")
    data2 = read_file("samples2.csv")
    w = read_file("weights.csv")[0]
    results = sum_weighted_diffs(data1, data2, w)
    dsum = np.sum(results)
    print("d-index:", dsum/len(results))
