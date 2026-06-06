# 📊 Data Cleaning and Visualization Project
<img width="990" height="665" alt="Screenshot 2026-06-06 170526" src="https://github.com/user-attachments/assets/ef09f0b7-3af0-4d91-ab99-a3bd249e43f9" />



## Introduction

This project was developed as part of my Data Science learning journey to understand the importance of data preprocessing and visualization.

Real-world datasets often contain missing values, duplicate records, and outliers that can affect analysis and decision-making. In this project, I performed data cleaning on a sales dataset and created visualizations to gain meaningful insights from the data.

The project demonstrates how raw data can be transformed into a clean and structured format before performing analysis and visualization.



## Project Objectives

The main objectives of this project are:

* Clean and preprocess raw sales data
* Remove duplicate records
* Handle missing values effectively
* Detect and remove outliers
* Perform basic data analysis
* Visualize sales performance across different regions



## Features

✅ Dataset loading using Pandas

✅ Duplicate record removal

✅ Missing value handling using mean imputation

✅ Outlier detection and removal using the IQR method

✅ Calculation of total sales and average sales

✅ Regional sales analysis

✅ Data visualization using bar charts



## Technologies Used

* Python
* Pandas
* Matplotlib



## Dataset Processing Steps

### 1. Data Loading

The sales dataset is loaded using Pandas for further analysis.

### 2. Duplicate Removal

Duplicate records are identified and removed to ensure data consistency.

### 3. Missing Value Treatment

Missing values in the Sales column are replaced with the average sales value.

### 4. Outlier Detection

The Interquartile Range (IQR) method is used to identify and remove outliers.

### 5. Data Analysis

After cleaning, the following metrics are calculated:

* Total Sales
* Average Sales

### 6. Data Visualization

A bar chart is generated to display total sales across different regions.


## Project Structure


Data-Cleaning-and-Visualization/
│
├── sales_data.csv
├── data_cleaning_visualization.py
└── README.md




## Sample Output


Original Dataset


  Region  Sales

  
0  North   1000

1  South   1500

2   East   1200

3   West   1800

4  North   1300

Cleaned Dataset


  Region  Sales
  
0  North   1000

1  South   1500

2   East   1200

3   West   1800

4  North   1300


Total Sales: 14600
Average Sales: 1460.00



## Visualization Output

The program generates a bar chart showing the total sales for each region, making it easier to compare sales performance and identify trends.



## Learning Outcomes

Through this project, I learned:

* Data preprocessing techniques
* Handling missing values
* Removing duplicate records
* Outlier detection using IQR
* Exploratory Data Analysis (EDA)
* Data visualization using Matplotlib
* Working with real-world datasets using Pandas



## Future Enhancements

Some possible improvements include:

* Interactive dashboards using Power BI or Tableau
* Advanced data visualizations
* Automated data cleaning pipeline
* Integration with larger datasets
* Statistical analysis and reporting



## Author

**Bittu Kumar**

This project helped me strengthen my understanding of data cleaning, exploratory data analysis, and visualization, which are essential skills in Data Science and Analytics.
