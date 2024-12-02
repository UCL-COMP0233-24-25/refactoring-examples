from math import *

# read sample files


def read_file(csv):
    with open(csv) as file:
        lines = file.readlines()
        data = []
        for line in lines:
            row = []
            for n in line.split(","):
                row.append(float(n.strip()))
            data.append(row)
    return data


data1 = read_file("analysis/data1.csv")
data2 = read_file("analysis/data2.csv")

with open("analysis/weights.csv") as filew:
    linew = filew.read()
    w = []
    for n in linew.split(","):
        w.append(float(n.strip()))

results = []
for row1, row2 in zip(data1, data2):
    s = 0
    for item in range(len(row1)):
        d = row1[item] - row2[item]
        s += w[item] * abs(d)
    results.append(s)


critical = 0
for item in results:  # for all i
    if item > 5:
        critical = critical + 1  # increase by 1
if critical == 1:
    print("criticality: 1 result above 5")
else:
    print("criticality:", critical, "results above 5")
