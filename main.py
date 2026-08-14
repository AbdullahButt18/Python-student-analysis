import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PYTHON STUDENT ANALYSIS
# Pandas Reference and Practice File
# ============================================================

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

# Path to the dataset
DATA_FILE = "data/students.csv"

# Load CSV file into a DataFrame
df = pd.read_csv(DATA_FILE)

print("\n========== ORIGINAL DATA ==========\n")
print(df)


# ------------------------------------------------------------
# 2. BASIC DATA INSPECTION
# ------------------------------------------------------------

# Display first 5 rows
print("\n========== HEAD ==========\n")
print(df.head())

# Display last 5 rows
print("\n========== TAIL ==========\n")
print(df.tail())

# Display random row(s)
print("\n========== SAMPLE ==========\n")
print(df.sample())

# Display column names
print("\n========== COLUMNS ==========\n")
print(df.columns)

# Display DataFrame index
print("\n========== INDEX ==========\n")
print(df.index)

# Display statistical summary of numerical columns
print("\n========== DESCRIBE ==========\n")
print(df.describe())

# Display number of rows and columns
print("\n========== SHAPE ==========\n")
print(df.shape)

# Display information about columns, data types and missing values
print("\n========== INFO ==========\n")
df.info()

# Display data types of every column
print("\n========== DATA TYPES ==========\n")
print(df.dtypes)


# ------------------------------------------------------------
# 3. SELECTING COLUMNS
# ------------------------------------------------------------

# Select one column
print("\n========== ONE COLUMN ==========\n")
print(df["CGPA"])

# Select multiple columns
print("\n========== MULTIPLE COLUMNS ==========\n")
print(df[["Name", "Department", "CGPA"]])


# ------------------------------------------------------------
# 4. LOC AND ILOC
# ------------------------------------------------------------

# loc[] selects data using labels
print("\n========== LOC ==========\n")
print(df.loc[0, "Name"])

# Select multiple rows and columns using loc
print("\n========== LOC MULTIPLE ==========\n")
print(df.loc[0:4, ["Name", "CGPA"]])

# iloc[] selects data using integer positions
print("\n========== ILOC ==========\n")
print(df.iloc[0, 4])

# Select rows using iloc
print("\n========== ILOC MULTIPLE ==========\n")
print(df.iloc[0:5, 0:5])


# ------------------------------------------------------------
# 5. BOOLEAN FILTERING
# ------------------------------------------------------------

# Students whose CGPA is greater than 3.50
print("\n========== CGPA > 3.50 ==========\n")
print(df[df["CGPA"] > 3.50])

# Students from Lahore
print("\n========== CITY = LAHORE ==========\n")
print(df[df["City"] == "Lahore"])

# Multiple conditions using AND &
print("\n========== LAHORE AND CGPA > 3.00 ==========\n")
print(
    df[
        (df["City"] == "Lahore")
        & (df["CGPA"] > 3.00)
    ]
)

# Multiple conditions using OR |
print("\n========== CS OR CGPA < 3.00 ==========\n")
print(
    df[
        (df["Department"] == "CS")
        | (df["CGPA"] < 3.00)
    ]
)

# NOT condition using ~
print("\n========== NOT CS ==========\n")
print(
    df[
        ~(df["Department"] == "CS")
    ]
)


# ------------------------------------------------------------
# 6. MISSING VALUES
# ------------------------------------------------------------

# Check every cell for missing values
print("\n========== ISNULL ==========\n")
print(df.isnull())

# Count missing values in every column
print("\n========== MISSING VALUE COUNT ==========\n")
print(df.isnull().sum())

# Check whether there are any missing values
print("\n========== ANY MISSING VALUES ==========\n")
print(df.isnull().any())


# ------------------------------------------------------------
# 7. DUPLICATES
# ------------------------------------------------------------

# Check duplicated rows
print("\n========== DUPLICATES ==========\n")
print(df.duplicated())

# Count duplicate rows
print("\n========== DUPLICATE COUNT ==========\n")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\n========== DUPLICATES AFTER REMOVAL ==========\n")
print(df.duplicated().sum())


# ------------------------------------------------------------
# 8. DATA TYPE CONVERSION
# ------------------------------------------------------------

# Convert CGPA to numeric
# errors="coerce" changes invalid values into NaN
df["CGPA"] = pd.to_numeric(
    df["CGPA"],
    errors="coerce"
)

# Convert Age to numeric
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)


# ------------------------------------------------------------
# 9. MISSING VALUE HANDLING
# ------------------------------------------------------------

# Replace missing CGPA with the average CGPA
df["CGPA"] = df["CGPA"].fillna(
    df["CGPA"].mean()
)

# Replace missing Age with average Age
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

print("\n========== DATA AFTER FILLING MISSING VALUES ==========\n")
print(df)


# ------------------------------------------------------------
# 10. CONDITIONAL UPDATE USING LOC
# ------------------------------------------------------------

# Change department to "High CGPA" for students
# whose CGPA is greater than or equal to 3.80
df.loc[
    df["CGPA"] >= 3.80,
    "CGPA_Category"
] = "High"

# Students below 3.80
df.loc[
    df["CGPA"] < 3.80,
    "CGPA_Category"
] = "Normal"

print("\n========== CGPA CATEGORY ==========\n")
print(
    df[
        ["Name", "CGPA", "CGPA_Category"]
    ]
)


# ------------------------------------------------------------
# 11. SORTING
# ------------------------------------------------------------

# Sort CGPA from highest to lowest
df_sorted = df.sort_values(
    by="CGPA",
    ascending=False
)

print("\n========== SORTED BY CGPA ==========\n")
print(
    df_sorted[
        ["Name", "CGPA"]
    ]
)

# Sort Age from lowest to highest
df_age_sorted = df.sort_values(
    by="Age",
    ascending=True
)

print("\n========== SORTED BY AGE ==========\n")
print(
    df_age_sorted[
        ["Name", "Age"]
    ]
)


# ------------------------------------------------------------
# 12. VALUE COUNTS
# ------------------------------------------------------------

# Count students in each department
print("\n========== DEPARTMENT COUNTS ==========\n")
print(df["Department"].value_counts())

# Count students in each city
print("\n========== CITY COUNTS ==========\n")
print(df["City"].value_counts())


# ------------------------------------------------------------
# 13. GROUPBY
# ------------------------------------------------------------

# Average CGPA by department
print("\n========== AVERAGE CGPA BY DEPARTMENT ==========\n")
department_cgpa = (
    df.groupby("Department")["CGPA"]
    .mean()
)

print(department_cgpa)

# Count students by department
print("\n========== STUDENT COUNT BY DEPARTMENT ==========\n")
department_count = (
    df.groupby("Department")["Student_ID"]
    .count()
)

print(department_count)

# Total CGPA by department
print("\n========== TOTAL CGPA BY DEPARTMENT ==========\n")
department_total = (
    df.groupby("Department")["CGPA"]
    .sum()
)

print(department_total)


# ------------------------------------------------------------
# 14. GROUPBY WITH MULTIPLE AGGREGATIONS
# ------------------------------------------------------------

print("\n========== MULTIPLE AGGREGATIONS ==========\n")

department_analysis = df.groupby("Department").agg(
    {
        "CGPA": ["mean", "max", "min"],
        "Age": ["mean", "max"],
        "Student_ID": "count"
    }
)

print(department_analysis)


# ------------------------------------------------------------
# 15. IDMAX AND IDMIN
# ------------------------------------------------------------

# Find the department with the highest average CGPA
highest_department = (
    df.groupby("Department")["CGPA"]
    .mean()
    .idxmax()
)

print(
    "\nDepartment with highest average CGPA:",
    highest_department
)

# Find the department with the lowest average CGPA
lowest_department = (
    df.groupby("Department")["CGPA"]
    .mean()
    .idxmin()
)

print(
    "Department with lowest average CGPA:",
    lowest_department
)


# ------------------------------------------------------------
# 16. CALCULATED COLUMNS
# ------------------------------------------------------------

# Create a new column based on existing columns
df["Age_Next_Year"] = df["Age"] + 1

print("\n========== CALCULATED COLUMN ==========\n")
print(
    df[
        ["Name", "Age", "Age_Next_Year"]
    ]
)


# ------------------------------------------------------------
# 17. APPLY()
# ------------------------------------------------------------

# Custom function
def cgpa_status(cgpa):
    if cgpa >= 3.50:
        return "Good"
    else:
        return "Needs Improvement"


# Apply the function to the CGPA column
df["CGPA_Status"] = df["CGPA"].apply(
    cgpa_status
)

print("\n========== APPLY() ==========\n")
print(
    df[
        ["Name", "CGPA", "CGPA_Status"]
    ]
)


# ------------------------------------------------------------
# 18. MAP()
# ------------------------------------------------------------

# Create a dictionary for category mapping
department_names = {
    "CS": "Computer Science",
    "IT": "Information Technology",
    "SE": "Software Engineering"
}

# Map short department names to full names
df["Department_Full_Name"] = (
    df["Department"].map(department_names)
)

print("\n========== MAP() ==========\n")
print(
    df[
        ["Department", "Department_Full_Name"]
    ]
)


# ------------------------------------------------------------
# 19. STRING OPERATIONS
# ------------------------------------------------------------

# Remove extra spaces
df["Name_Clean"] = df["Name"].str.strip()

# Convert names to uppercase
df["Name_Upper"] = df["Name"].str.upper()

# Convert names to lowercase
df["Name_Lower"] = df["Name"].str.lower()

# Count characters in each name
df["Name_Length"] = df["Name"].str.len()

# Check whether city contains "Lahore"
lahore_students = df[
    df["City"].str.contains(
        "Lahore",
        case=False,
        na=False
    )
]

print("\n========== STRING OPERATIONS ==========\n")
print(
    df[
        [
            "Name",
            "Name_Upper",
            "Name_Lower",
            "Name_Length"
        ]
    ]
)

print("\n========== STUDENTS FROM LAHORE ==========\n")
print(lahore_students)


# ------------------------------------------------------------
# 20. DATE AND TIME
# ------------------------------------------------------------

# Create an example date column
df["Admission_Date"] = pd.to_datetime(
    "2026-01-01"
)

# Extract year
df["Admission_Year"] = (
    df["Admission_Date"].dt.year
)

# Extract month
df["Admission_Month"] = (
    df["Admission_Date"].dt.month
)

# Extract day
df["Admission_Day"] = (
    df["Admission_Date"].dt.day
)

print("\n========== DATE OPERATIONS ==========\n")
print(
    df[
        [
            "Name",
            "Admission_Date",
            "Admission_Year",
            "Admission_Month",
            "Admission_Day"
        ]
    ]
)


# ------------------------------------------------------------
# 21. BASIC STATISTICS
# ------------------------------------------------------------

print("\n========== BASIC STATISTICS ==========\n")

print("Average CGPA:", df["CGPA"].mean())
print("Median CGPA:", df["CGPA"].median())
print("Total CGPA:", df["CGPA"].sum())
print("Highest CGPA:", df["CGPA"].max())
print("Lowest CGPA:", df["CGPA"].min())
print("Number of students:", df["Student_ID"].count())


# ------------------------------------------------------------
# 22. BASIC PANDAS PLOTTING
# ------------------------------------------------------------

# -------- BAR CHART --------

average_cgpa = (
    df.groupby("Department")["CGPA"]
    .mean()
)

average_cgpa.plot(
    kind="bar",
    title="Average CGPA by Department",
    xlabel="Department",
    ylabel="Average CGPA",
    rot=0,
    figsize=(8, 5)
)

plt.tight_layout()
plt.savefig(
    "output/average_cgpa_by_department.png",
    dpi=150
)

plt.show()
plt.close()


# -------- PIE CHART --------

department_counts = (
    df["Department"].value_counts()
)

department_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    ylabel="",
    title="Student Proportion by Department",
    figsize=(7, 7)
)

plt.tight_layout()
plt.savefig(
    "output/department_proportion.png",
    dpi=150
)

plt.show()
plt.close()


# -------- LINE CHART --------

df_sorted = df.sort_values(
    by="Student_ID"
)

df_sorted.plot(
    x="Student_ID",
    y="CGPA",
    kind="line",
    title="CGPA by Student ID",
    xlabel="Student ID",
    ylabel="CGPA",
    figsize=(8, 5)
)

plt.tight_layout()
plt.savefig(
    "output/cgpa_line_chart.png",
    dpi=150
)

plt.show()
plt.close()


# -------- SCATTER PLOT --------

df.plot(
    x="Age",
    y="CGPA",
    kind="scatter",
    title="Age vs CGPA",
    xlabel="Age",
    ylabel="CGPA",
    figsize=(8, 5)
)

plt.tight_layout()
plt.savefig(
    "output/age_vs_cgpa.png",
    dpi=150
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 23. EXPORT DATA
# ------------------------------------------------------------

# Save the cleaned and processed DataFrame
df.to_csv(
    "output/cleaned_students.csv",
    index=False
)

print("\n========== PROJECT COMPLETE ==========\n")
print("Cleaned dataset saved to output/cleaned_students.csv")
print("Charts saved to output/")
