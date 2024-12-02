from math import *

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

data1 = read_file("data1.csv")
data2 = read_file("data2.csv")
w = read_file("weights.csv")[0]

results = []
for i in range(len(data1)):
    s = 0
    for j in range(len(w)):
        d = data1[i][j] - data2[i][j]
        s += w[j] * abs(d)
    results.append(s)

critical = 0
for i in range(len(results)):  # for all i
    if results[i] > 5:
        critical = critical + 1  # increase by 1
if critical == 1:
    print("criticality: 1 result above 5")
else:
    print("criticality:", critical, "results above 5")
