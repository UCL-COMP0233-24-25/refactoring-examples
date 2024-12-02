from utils import read_file, sum_weighted_diffs

data1 = read_file("samples1.csv")
data2 = read_file("samples2.csv")
w = read_file("weights.csv")[0]

results = sum_weighted_diffs(data1, data2, w)

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
