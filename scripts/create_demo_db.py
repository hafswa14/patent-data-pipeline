import sqlite3
import pandas as pd
import os

base_dir = os.path.dirname(__file__)

full_db = os.path.join(base_dir, "..", "patents.db")
demo_db = os.path.join(base_dir, "..", "patents_demo.db")

conn_full = sqlite3.connect(full_db)
conn_demo = sqlite3.connect(demo_db)

# Sample patents
patents = pd.read_sql_query(
    "SELECT * FROM patents LIMIT 50000",
    conn_full
)

inventors = pd.read_sql_query(
    "SELECT * FROM inventors LIMIT 20000",
    conn_full
)

locations = pd.read_sql_query(
    "SELECT * FROM locations LIMIT 5000",
    conn_full
)

companies = pd.read_sql_query(
    "SELECT * FROM companies LIMIT 10000",
    conn_full
)

patent_inventor = pd.read_sql_query(
    "SELECT * FROM patent_inventor LIMIT 50000",
    conn_full
)

# Save to demo DB
patents.to_sql("patents", conn_demo, if_exists="replace", index=False)
inventors.to_sql("inventors", conn_demo, if_exists="replace", index=False)
locations.to_sql("locations", conn_demo, if_exists="replace", index=False)
companies.to_sql("companies", conn_demo, if_exists="replace", index=False)
patent_inventor.to_sql("patent_inventor", conn_demo, if_exists="replace", index=False)

print("✅ Demo database created!")

conn_full.close()
conn_demo.close()

#python scripts/create_demo_db.py