import numpy as np

# read sample files

def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        data = []
        for line in lines:
            row_items = line.split(',')
            row = [float(item.strip()) for item in row_items]
            data.append(row)
    return data


if __name__ == "__main__":
    data1 = read_file("data1.csv")
    data2 = read_file("data2.csv")
    w = read_file("weights.csv")[0]

    results = []
    for i in range(len(data1)):
        row1 = data1[i]
        row2 = data2[i]
        diffs = np.abs(row1-row2)
        sum_weighted_diffs = np.sum(diffs*w)
        results.append(sum_weighted_diffs)

    critical = 0
    for i in range(len(results)):  # for all i
        if results[i] > 5:
            critical = critical + 1  # increase by 1
    if critical == 1:
        print("criticality: 1 result above 5")
    else:
        print("criticality:", critical, "results above 5")
