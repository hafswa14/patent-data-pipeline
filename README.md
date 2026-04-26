# Patent Data Pipeline & Analysis

#  Project Overview
This project implements a complete data pipeline for processing, storing, and analyzing patent data. The system cleans raw data, loads it into a relational database, and generates analytical reports.

---

#  Technologies Used
- Python (Pandas, SQLite3)
- SQL (Joins, Aggregations, Subqueries)
- SQLite Database


#  Project Structure

patent-data-pipeline/
│
├── scripts/
│ ├── process_patents.py
│ ├── process_inventors.py
│ ├── process_locations.py
│ ├── process_companies.py
│ ├── load_to_db.py
│ └── generate_reports.py
│
├── sql/
│ ├── schema.sql
│ └── queries.sql
│
├── cleaned_data/
├── reports/
│ ├── top_inventors.csv
│ ├── top_companies.csv
│ ├── country_trends.csv
│ └── report.json
│
├── patents.db
└── README.md


#  How to Run the Project

# Step 1: Process Data
Run all processing scripts:
python scripts/process_*.py

# Step 2: Load Data into Database
python scripts/load_to_db.py


# Step 3: Generate Reports
python scripts/generate_reports.py


#  Reports Generated

# Console Report
Displays:
- Total patents
- Top inventors
- Top companies
- Top countries

# CSV Files
- `top_inventors.csv`
- `top_companies.csv`
- `country_trends.csv`

# JSON Report
 `report.json`


# Key SQL Analysis

 -Top inventors by patent count
 -Top countries contributing to patents
 -Patent trends over time
 -Average inventors per patent
 -Company frequency analysis


# Limitations

 -Company-to-patent relationships are not directly linked in the dataset.
 -Company analysis reflects frequency, not exact patent ownership.


## Reproducibility

Due to the large size of the dataset, raw data and the database file are not included.

To reproduce results:

1. Download the dataset from the original source
2. Place files in the `data/` folder
3. Run processing scripts:
   python scripts/process_*.py
4. Load database:
   python scripts/load_to_db.py
5. Generate reports:
   python scripts/generate_reports.py



# Conclusion

This project demonstrates strong skills in:
 -Data preprocessing
 -Relational database design
 -SQL analysis
 -Data reporting

