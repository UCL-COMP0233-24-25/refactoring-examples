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
    return np.array(data)


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

    critical_results = [result for result in results if result>5]
    print(f"Criticality: {len(critical_results)} result(s) above 5.")
