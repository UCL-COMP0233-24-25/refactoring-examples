import numpy as np
def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        data = []
        for line in lines:
            row_items = line.split(',')
            row = [float(item.strip()) for item in row_items]
            data.append(row)
    return np.array(data)

def sum_weighted_diffs(data1, data2, w):
    results = []
    for i in range(len(data1)):
        row1 = data1[i]
        row2 = data2[i]
        diffs = np.abs(row1-row2)
        sum_weighted_diffs = np.sum(diffs*w)
        results.append(sum_weighted_diffs)
    return results