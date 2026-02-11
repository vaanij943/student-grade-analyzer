import csv
import statistics

def load_grades(csv_path):
    scores = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            scores.append(float(row["score"]))
    return scores

def compute_statistics(scores):
    return {
        "average": round(sum(scores) / len(scores), 2),
        "median": statistics.median(scores),
        "std_dev": round(statistics.stdev(scores), 2)
    }

def letter_distribution(scores):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in scores:
        if s >= 90:
            dist["A"] += 1
        elif s >= 80:
            dist["B"] += 1
        elif s >= 70:
            dist["C"] += 1
        elif s >= 60:
            dist["D"] += 1
        else:
            dist["F"] += 1
    return dist

def export_summary(stats, path):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["metric", "value"])
        for key, value in stats.items():
            writer.writerow([key, value])

def export_distribution(dist, path):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["grade", "count"])
        for grade, count in dist.items():
            writer.writerow([grade, count])

def main():
    input_csv = "data/grades.csv"
    summary_csv = "outputs/summary.csv"
    dist_csv = "outputs/grade_distribution.csv"

    scores = load_grades(input_csv)
    stats = compute_statistics(scores)
    dist = letter_distribution(scores)

    export_summary(stats, summary_csv)
    export_distribution(dist, dist_csv)

    print("Grade Analysis Results")
    print("----------------------")
    print(f"Average: {stats['average']}")
    print(f"Median: {stats['median']}")
    print(f"Standard Deviation: {stats['std_dev']}")
    print("\nGrade Distribution:")
    for grade, count in dist.items():
        print(f"{grade}: {count}")

    print("\nCSV files generated in outputs/")

if __name__ == "__main__":
    main()
