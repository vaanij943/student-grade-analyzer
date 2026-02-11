# Student Grade Analyzer

A Python-based data analysis tool that processes student grade data from CSV files, computes statistical metrics, and exports structured results for visualization. MATLAB is used to generate graphical representations of grade distributions and summary statistics.

This project demonstrates file I/O, data processing, statistical analysis, and cross-tool integration between Python and MATLAB.

---

## Features

- Reads student grade data from CSV files
- Computes key statistical metrics:
  - Average
  - Median
  - Standard deviation
- Generates letter grade distributions (A–F)
- Automatically exports results to CSV files
- Visualizes results using MATLAB bar charts
- Modular, reproducible data pipeline

---

## Project Overview

The Student Grade Analyzer processes numerical grade data stored in a CSV file and applies statistical analysis using Python. The processed results are written to structured output files, which are then read by MATLAB to generate visual plots.

This workflow mirrors real-world data analysis pipelines where computation and visualization are handled by different tools.

---

## Data Pipeline

1. Input grades are stored in a CSV file
2. Python reads and processes the data
3. Statistical results are calculated
4. Output CSV files are generated
5. MATLAB reads the output files
6. Graphs are produced for visualization

---

## Python Processing

The Python component performs the following tasks:

- Reads raw grade data using CSV parsing
- Computes statistical metrics using built-in libraries
- Categorizes grades into letter distributions
- Automatically creates output directories if missing
- Exports results to CSV files for downstream analysis

Generated output files:
- `summary.csv`
- `grade_distribution.csv`

---

## MATLAB Visualization

<img width="989" height="641" alt="image" src="https://github.com/user-attachments/assets/40309a0c-f1ed-4020-9174-ae2981bb37b8" />

<img width="1015" height="631" alt="image" src="https://github.com/user-attachments/assets/e50d62a6-57f5-4e8c-b21d-28762ef3cf89" />

MATLAB is used to visualize the processed data by reading the generated CSV files.

### Visualizations include:
- Letter grade distribution bar chart
- Summary statistics bar chart

These plots verify the correctness of the Python processing and provide an intuitive representation of class performance.

---

## Repository Structure

```
student-grade-analyzer/
├── analyzer/
│ └── main.py
├── data/
│ └── grades.csv
├── outputs/
│ ├── summary.csv
│ └── grade_distribution.csv
├── matlab/
│ └── plot_grades.m
└── README.md
```
---

## Technologies Used

- Python
- MATLAB
- CSV data formats
- File input/output operations
- Statistical analysis

---

## Learning Outcomes

- Practical experience with CSV data processing
- Implementation of statistical computations in Python
- Automated file and directory handling
- Cross-platform data analysis workflow
- MATLAB-based data visualization
- Structuring reproducible analysis pipelines

---

## Notes

This project was developed for educational purposes and demonstrates foundational data analysis techniques applicable to engineering and computer science workflows.
