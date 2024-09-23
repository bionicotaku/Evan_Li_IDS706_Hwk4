# Evan_Li_IDS706_Hwk4

[![CI](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk4/actions/workflows/cicd.yml/badge.svg)](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk4/actions/workflows/cicd.yml)

## Dataset Overview

The data is sourced from [Kaggle's Data Engineer Salary in 2024 dataset](https://www.kaggle.com/datasets/chopper53/data-engineer-salary-in-2024). This dataset provides insights into data engineer salaries and employment attributes for the year 2024. It includes information such as:
   - Salary
   - Job title
   - Experience level
   - Employment type
   - Employee residence
   - Remote work ratio
   - Company location
   - Company size

## Data Analysis
Analyzed the following:
- Statistical data and distribution of all salaries
- Job Title Distribution
- Experience Level Distribution
- Average Salary By Job
- Salary Statistics by Experience Level

## Project Features
1. Python script using Polars library to read the dataset and generate descriptive statistics with data visualization, finally summarize and create an analysis_results.md file. (All Polars library calls, analysis, and plotting are done in the mylib/calculate_stat.py file)
2. Creating test_script.py to test the script, test_lib.py to test the library, and finally using the nbval plugin for pytest to test all files includng ipynb.
3. Generated a badge linked to GitHub actions.