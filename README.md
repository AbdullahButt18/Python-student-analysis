# Python Student Analysis

A practical Pandas study and data analysis project created as a long-term Python learning and revision resource.

## About This Project

This repository contains the Pandas concepts learned during my Python and AI/ML preparation.

The main purpose of this project is to provide a personal reference that I can return to whenever I forget a Pandas command, syntax, or data-analysis technique.

The project uses a small student dataset to demonstrate practical Pandas operations instead of keeping the concepts only as isolated examples.

The code is heavily commented and organized so that individual concepts can be easily reviewed in the future.

## Project Structure

```text
Python-student-analysis/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── main.py
│
├── data/
│   └── students.csv
│
└── output/
    ├── age_vs_cgpa.png
    ├── cgpa_line_chart.png
    ├── department_proportion.png
    └── average_cgpa_by_department.png
```

## Topics Covered

### 1. Pandas Fundamentals
- Importing Pandas
- Series
- DataFrames
- Reading CSV files
- Creating DataFrames

### 2. Data Inspection
- `head()`
- `tail()`
- `sample()`
- `columns`
- `index`
- `shape`
- `describe()`
- `info()`
- `dtypes`

### 3. Selecting Data
- Selecting a single column
- Selecting multiple columns
- `loc[]`
- `iloc[]`

### 4. Filtering
- Boolean filtering
- Filtering numerical data
- Filtering categorical data
- Multiple conditions
- AND operator `&`
- OR operator `|`
- NOT operator `~`

### 5. Missing Values
- Detecting missing values
- Counting missing values
- `isnull()`
- `isna()`
- `notnull()`
- `notna()`
- `fillna()`
- Filling numerical missing values with the mean

### 6. Duplicate Data
- Detecting duplicates
- `duplicated()`
- Counting duplicates
- Removing duplicates
- `drop_duplicates()`

### 7. Data Type Conversion
- `pd.to_numeric()`
- `pd.to_datetime()`
- `errors="coerce"`

### 8. Updating Data
- Conditional updates
- Updating values using `loc[]`

### 9. Sorting and Counting
- `sort_values()`
- Ascending sorting
- Descending sorting
- `value_counts()`

### 10. Grouping Data
- `groupby()`
- Grouping by categorical columns
- Calculating group averages
- Calculating group totals
- Counting values inside groups

### 11. Aggregation
- `mean()`
- `sum()`
- `count()`
- `min()`
- `max()`
- `agg()`
- Multiple aggregations
- Dictionary-based aggregation
- Named aggregation

### 12. Finding Maximum and Minimum Groups
- `idxmax()`
- `idxmin()`
- Finding which group has the highest value
- Finding which group has the lowest value

### 13. Creating New Columns
- Creating calculated columns
- Creating derived columns
- Performing calculations between columns

### 14. Functions with Pandas
- Creating custom functions
- `apply()`
- `map()`
- Applying a function to a column
- Mapping categorical values using dictionaries

### 15. String Operations
- `str.strip()`
- `str.upper()`
- `str.lower()`
- `str.contains()`
- `str.len()`
- `str.replace()`

### 16. Date and Time Operations
- Converting strings to dates
- `pd.to_datetime()`
- `.dt.year`
- `.dt.month`
- `.dt.day`

### 17. Basic Statistics
- Mean
- Median
- Sum
- Minimum
- Maximum
- Count
- Descriptive statistics

### 18. Pandas Plotting
- Bar charts
- Pie charts
- Line charts
- Scatter plots
- Plotting grouped data
- Adding titles
- Adding axis labels
- Rotating labels
- Displaying percentages in pie charts

### 19. Exporting Data
- `to_csv()`
- Saving cleaned data
- Saving CSV files without the DataFrame index

## Dataset

The project uses a student dataset containing the following columns:

- Student_ID
- Name
- Department
- Age
- CGPA
- City

The dataset contains 20 student records. A missing CGPA value is intentionally included so that missing-data handling can be practiced using Pandas.

## Installation

Make sure Python is installed on your computer, then install the required libraries:

```bash
pip install -r requirements.txt
```

## Running the Project

1. Clone or download this repository.
2. Open a terminal inside the project directory and run:

```bash
python main.py
```

The script reads the student dataset from `data/students.csv`. Generated output files and charts are stored inside the `output/` folder.

## Learning Purpose

This repository is primarily a personal learning and revision resource. The purpose is not to create a production-level application. Instead, the project focuses on understanding Pandas syntax, data manipulation, data cleaning, grouping, aggregation, functions, and basic visualization.

The Python file contains comments and practical examples so that individual concepts can be quickly reviewed whenever they are forgotten. The dataset is intentionally small so that the results can be easily understood and manually verified.

## Project Goals

- Build a strong foundation in Pandas
- Practice real-world data-cleaning techniques
- Understand DataFrame operations
- Become comfortable with filtering and grouping
- Learn how to create calculated columns
- Practice `apply()` and `map()`
- Understand basic Pandas plotting
- Build a reusable Pandas reference file
- Maintain a professional GitHub learning repository

## Future Learning Path

After completing the Pandas section, the planned learning path is:

- Matplotlib
- NumPy revision
- Statistics and Probability
- Scikit-learn
- Classical Machine Learning
- Model Evaluation
- Feature Engineering
- Modern AI and Generative AI
- AI Automation
- Machine Learning Projects

## Repository Philosophy

This repository is designed to grow along with the learning journey. New concepts, examples, datasets, and projects can be added as new topics are learned. The goal is to maintain a clean and organized reference that can be revisited in the future instead of relying only on memory.

## Author

**Abdullah**
Bachelor of Information Technology
University of Gujrat, Pakistan

*Learning by building, practicing, and revising.*
