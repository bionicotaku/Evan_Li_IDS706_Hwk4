import polars as pl
import matplotlib.pyplot as plt

def read_data(file_path):
    # Read the data from the CSV file
    columns_to_keep = [
        "work_year",
        "experience_level",
        "job_title",
        "salary_in_usd",
        "remote_ratio",
        "company_size",
    ]
    return pl.read_csv(file_path).select(columns_to_keep)

def calculate_stat(data):
    # Calculate descriptive statistics of the data.
    return data.describe()

def plot_salary_distribution(data):
    # Plot the distribution of salaries.
    plt.figure(figsize=(10, 6))
    salary_data = data.select(pl.col("salary_in_usd")).to_numpy().flatten()
    plt.hist(salary_data, bins=50)
    plt.title("Distribution of Salaries")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.savefig('output/salary_distribution.png')
    plt.show()
    plt.close()

def plot_job_title_distribution(data):
    # Plot the distribution of top 20 job titles.
    plt.figure(figsize=(12, 6))
    job_title_counts = (data.group_by('job_title')
                        .agg(pl.len().alias('count'))
                        .sort('count', descending=True)
                        .head(20))
    
    plt.bar(job_title_counts['job_title'], job_title_counts['count'])
    plt.title('Top 20 Job Titles Distribution')
    plt.xlabel('Job Title')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('output/job_title_distribution.png')
    plt.show()
    plt.close()
    return job_title_counts

def plot_experience_level_distribution(data):
    # Plot the distribution of experience levels.
    plt.figure(figsize=(8, 6))
    experience_level_counts = (data.group_by('experience_level')
                               .agg(pl.len().alias('count'))
                               .sort('count', descending=True))
    
    plt.bar(experience_level_counts['experience_level'],
            experience_level_counts['count'])
    plt.title('Experience Level Distribution')
    plt.xlabel('Experience Level')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('output/experience_level_distribution.png')
    plt.show()
    plt.close()
    return experience_level_counts

def plot_average_salary_by_job(data):
    # Plot average salary for top 15 job titles.
    average_salary_by_job = (data
        .group_by('job_title')
        .agg(pl.col('salary_in_usd').mean().alias('average_salary'))
        .sort('average_salary', descending=True)
        .head(15))
    
    plt.figure(figsize=(12, 8))
    plt.bar(average_salary_by_job['job_title'], average_salary_by_job['average_salary'])
    plt.title('Average Salary by Job Title (Top 15)', fontsize=16)
    plt.xlabel('Job Title', fontsize=12)
    plt.ylabel('Average Salary (USD)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    for i, v in enumerate(average_salary_by_job['average_salary']):
        plt.text(i, v, f'${int(v):,}', ha='center', va='bottom')
    
    plt.savefig('output/average_salary_by_job.png')
    plt.show()
    plt.close()

def plot_salary_vs_experience(data):
    # Plot salary vs experience level.
    experience_map = {
        'EN': 0,  # Entry-level
        'MI': 1,  # Mid-level
        'SE': 2,  # Senior
        'EX': 3   # Executive
    }
    
    data_with_numeric_exp = data.with_columns(
        pl.col('experience_level')
          .map_elements(lambda x: experience_map.get(x, -1), return_dtype=pl.Int64)
          .alias('experience_numeric')
    )
    
    plt.figure(figsize=(12, 8))
    plt.scatter(data_with_numeric_exp['experience_numeric'], 
                data_with_numeric_exp['salary_in_usd'], alpha=0.5)
    plt.title('Relationship between Experience Level and Salary', fontsize=16)
    plt.xlabel('Experience Level', fontsize=12)
    plt.ylabel('Salary (USD)', fontsize=12)
    plt.xticks([0, 1, 2, 3], ['Entry', 'Mid', 'Senior', 'Executive'])
    plt.grid(True, linestyle='--', alpha=0.7)
    
    average_salary = (data_with_numeric_exp.group_by('experience_level')
                      .agg(pl.col('salary_in_usd').mean()))
    for i, exp in enumerate(['EN', 'MI', 'SE', 'EX']):
        avg = average_salary.filter(pl
                                    .col('experience_level') == exp)['salary_in_usd'][0]
        plt.text(i, avg, f'${int(avg):,}', ha='center', va='bottom')
    
    plt.savefig('output/salary_vs_experience.png')
    plt.show()
    plt.close()

def calculate_salary_stats_by_experience(data):
    # Calculate salary statistics by experience level.
    return data.group_by('experience_level').agg([
        pl.col('salary_in_usd').count().alias('count'),
        pl.col('salary_in_usd').mean().alias('mean'),
        pl.col('salary_in_usd').median().alias('median'),
        pl.col('salary_in_usd').min().alias('min'),
        pl.col('salary_in_usd').max().alias('max')
    ])