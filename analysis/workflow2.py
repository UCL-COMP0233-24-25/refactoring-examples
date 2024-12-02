from workflow1 import read_file

data1 = read_file("samples1.csv")
data2 = read_file("samples2.csv")
w = read_file("weights.csv")[0]

results = []
for i in range(len(data1)):
    s = 0
    for j in range(len(w)):
        d = data1[i][j] - data2[i][j]
        s += w[j] * abs(d)
    results.append(s)

# critical = 0
# for i in range(len(results)):
#     if results[i] > 5:
#         critical = critical + 1
# if critical == 1:
#     print("criticality: 1 result over 5")
# else:
#     print("criticality:", critical, "results over 5")
dsum =  0
for i in range(len(results)):
    dsum = dsum + results[i]
print("d-index:", dsum/len(results))
