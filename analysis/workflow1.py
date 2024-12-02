from utils import read_file, sum_weighted_diffs

if __name__ == "__main__":
    data1 = read_file("data1.csv")
    data2 = read_file("data2.csv")
    w = read_file("weights.csv")[0]
    results = sum_weighted_diffs(data1, data2, w)
    critical_results = [result for result in results if result>5]
    print(f"Criticality: {len(critical_results)} result(s) above 5.")
