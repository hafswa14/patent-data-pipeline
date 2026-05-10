GLOBAL PATENT INTELLIGENCE DATA PIPELINE

Student Name: NASSIWA HAFSWA
REG NO. : 23/U/23750
Course: BSSE
Date: 10/5/2026

GitHub Repository: https://github.com/hafswa14/patent-data-pipeline


Dashboard Link: https://patent-data-pipeline-qdb5zwid8yn5efwrex8zyo.streamlit.app/

Project Description:
This project implements a patent data pipeline that processes large patent datasets,
stores them in a relational database, performs SQL analytics, generates reports,
and visualizes insights using a Streamlit dashboard.

Features:
- Data preprocessing pipeline
- SQLite database integration
- SQL analytical queries
- CSV and JSON reports
- Streamlit dashboard
- Patent trend visualizations


Why I Used Streamlit for deployment:
Streamlit was chosen because it provides a fast and simple way to build interactive data dashboards using Python only.
 Since the project already used Python for data processing, cleaning, database loading, and analytics,
 Streamlit allowed the dashboard to integrate directly with the existing pipeline without requiring additional frontend technologies such as HTML, CSS, or JavaScript.

Why a Demo Database Was Created:

The original database (patents.db) was extremely large and unsuitable for deployment on Streamlit Cloud because:
Large databases increase deployment size
Queries become slower online
Cloud platforms have storage and resource limitations
Deployment becomes unstable with massive datasets

To solve this, i Created a smaller representative database called (patents_demo.db)

This database contains a random sample of the original data while preserving:

patent relationships
inventor data
company data
country data
analytical trends

This allowed the dashboard to remain fast, lightweight, and deployable while still demonstrating the full functionality of the system.


Why i Used Random Sampling:

Initially, records were selected using: LIMIT
However, this produced biased results because the first records mostly belonged to a single year.

To improve representativeness, i used random sampling using:
ORDER BY RANDOM()

This ensured:

better trend visualization
more realistic analytics
balanced data across years and categories


Key Challenges Encountered

Some major challenges included:

Managing a very large patent dataset
Long-running SQL queries
Deployment limitations on Streamlit Cloud
Database path issues
Sampling bias during demo DB creation
Dependency conflicts during deployment

These challenges were solved through:

indexing
query optimization
random sampling
minimal deployment dependencies
lightweight demo database design


Conclusion
The project successfully demonstrates:

data cleaning
ETL pipeline design
relational database management
SQL analytics
report generation
dashboard development
cloud deployment

The final system provides an interactive platform for exploring global patent intelligence data efficiently and visually.



