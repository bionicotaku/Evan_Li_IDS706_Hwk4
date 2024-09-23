# Data Analysis Results

## Statistical Analysis

```
shape: (9, 7)
┌────────────┬─────────────┬──────────────┬──────────────┬─────────────┬─────────────┬─────────────┐
│ statistic  ┆ work_year   ┆ experience_l ┆ job_title    ┆ salary_in_u ┆ remote_rati ┆ company_siz │
│ ---        ┆ ---         ┆ evel         ┆ ---          ┆ sd          ┆ o           ┆ e           │
│ str        ┆ f64         ┆ ---          ┆ str          ┆ ---         ┆ ---         ┆ ---         │
│            ┆             ┆ str          ┆              ┆ f64         ┆ f64         ┆ str         │
╞════════════╪═════════════╪══════════════╪══════════════╪═════════════╪═════════════╪═════════════╡
│ count      ┆ 16534.0     ┆ 16534        ┆ 16534        ┆ 16534.0     ┆ 16534.0     ┆ 16534       │
│ null_count ┆ 0.0         ┆ 0            ┆ 0            ┆ 0.0         ┆ 0.0         ┆ 0           │
│ mean       ┆ 2023.226866 ┆ null         ┆ null         ┆ 149686.7779 ┆ 32.00375    ┆ null        │
│            ┆             ┆              ┆              ┆ 73          ┆             ┆             │
│ std        ┆ 0.713558    ┆ null         ┆ null         ┆ 68505.29315 ┆ 46.245158   ┆ null        │
│            ┆             ┆              ┆              ┆ 6           ┆             ┆             │
│ min        ┆ 2020.0      ┆ EN           ┆ AI Architect ┆ 15000.0     ┆ 0.0         ┆ L           │
│ 25%        ┆ 2023.0      ┆ null         ┆ null         ┆ 101100.0    ┆ 0.0         ┆ null        │
│ 50%        ┆ 2023.0      ┆ null         ┆ null         ┆ 141300.0    ┆ 0.0         ┆ null        │
│ 75%        ┆ 2024.0      ┆ null         ┆ null         ┆ 185900.0    ┆ 100.0       ┆ null        │
│ max        ┆ 2024.0      ┆ SE           ┆ Staff        ┆ 800000.0    ┆ 100.0       ┆ S           │
│            ┆             ┆              ┆ Machine      ┆             ┆             ┆             │
│            ┆             ┆              ┆ Learning     ┆             ┆             ┆             │
│            ┆             ┆              ┆ Enginee…     ┆             ┆             ┆             │
└────────────┴─────────────┴──────────────┴──────────────┴─────────────┴─────────────┴─────────────┘

Top 20 Job Titles Distribution:
shape: (20, 2)
┌───────────────────────────┬───────┐
│ job_title                 ┆ count │
│ ---                       ┆ ---   │
│ str                       ┆ u32   │
╞═══════════════════════════╪═══════╡
│ Data Engineer             ┆ 3464  │
│ Data Scientist            ┆ 3314  │
│ Data Analyst              ┆ 2440  │
│ Machine Learning Engineer ┆ 1705  │
│ Research Scientist        ┆ 531   │
│ …                         ┆ …     │
│ Research Analyst          ┆ 123   │
│ Data Science Manager      ┆ 122   │
│ AI Engineer               ┆ 120   │
│ Business Intelligence     ┆ 98    │
│ BI Developer              ┆ 90    │
└───────────────────────────┴───────┘

Experience Level Distribution:
shape: (4, 2)
┌──────────────────┬───────┐
│ experience_level ┆ count │
│ ---              ┆ ---   │
│ str              ┆ u32   │
╞══════════════════╪═══════╡
│ SE               ┆ 10670 │
│ MI               ┆ 4038  │
│ EN               ┆ 1325  │
│ EX               ┆ 501   │
└──────────────────┴───────┘

Salary Statistics by Experience Level:
shape: (4, 6)
┌──────────────────┬───────┬───────────────┬──────────┬───────┬────────┐
│ experience_level ┆ count ┆ mean          ┆ median   ┆ min   ┆ max    │
│ ---              ┆ ---   ┆ ---           ┆ ---      ┆ ---   ┆ ---    │
│ str              ┆ u32   ┆ f64           ┆ f64      ┆ i64   ┆ i64    │
╞══════════════════╪═══════╪═══════════════╪══════════╪═══════╪════════╡
│ EX               ┆ 501   ┆ 195264.281437 ┆ 192000.0 ┆ 15000 ┆ 465000 │
│ EN               ┆ 1325  ┆ 92327.413585  ┆ 83000.0  ┆ 15000 ┆ 774000 │
│ MI               ┆ 4038  ┆ 125923.131253 ┆ 115000.0 ┆ 15000 ┆ 800000 │
│ SE               ┆ 10670 ┆ 163662.826148 ┆ 155000.0 ┆ 15809 ┆ 750000 │
└──────────────────┴───────┴───────────────┴──────────┴───────┴────────┘
```

![Salary Distribution](output/salary_distribution.png)

![Job Title Distribution](output/job_title_distribution.png)

![Experience Level Distribution](output/experience_level_distribution.png)

![Average Salary By Job](output/average_salary_by_job.png)

![Salary Vs Experience](output/salary_vs_experience.png)

