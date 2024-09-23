from mylib import calculate_stat
from mylib import generate_markdown
import io
from contextlib import redirect_stdout


def main():
    # Read data
    filteredData = calculate_stat.read_data("Dataset-salary-2024.csv")

    # Calculate and print statistics
    print(calculate_stat.calculate_stat(filteredData))
    print("")
    # Plot salary distribution
    calculate_stat.plot_salary_distribution(filteredData)

    # Plot and print job title distribution
    job_title_counts = calculate_stat.plot_job_title_distribution(filteredData)
    print("Top 20 Job Titles Distribution:")
    print(job_title_counts)

    # Plot and print experience level distribution
    experience_level_counts = calculate_stat.plot_experience_level_distribution(
        filteredData
    )
    print("\nExperience Level Distribution:")
    print(experience_level_counts)

    # Plot average salary by job title
    calculate_stat.plot_average_salary_by_job(filteredData)

    # Plot salary vs experience level
    calculate_stat.plot_salary_vs_experience(filteredData)

    # Calculate and print salary statistics by experience level
    salary_stats = calculate_stat.calculate_salary_stats_by_experience(filteredData)
    print("\nSalary Statistics by Experience Level:")
    print(salary_stats)


if __name__ == "__main__":
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        main()
    output = captured_output.getvalue()

    generate_markdown.generate_markdown(output)
