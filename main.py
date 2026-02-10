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

def main():
    csv_path = "data/grades.csv"

    scores = load_grades(csv_path)
    stats = compute_statistics(scores)
    dist = letter_distribution(scores)

    print("Grade Analysis Results")
    print("----------------------")
    print(f"Average: {stats['average']}")
    print(f"Median: {stats['median']}")
    print(f"Standard Deviation: {stats['std_dev']}")
    print("\nGrade Distribution:")
    for grade, count in dist.items():
        print(f"{grade}: {count}")

if __name__ == "__main__":
    main()
