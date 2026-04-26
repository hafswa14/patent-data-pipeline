import pandas as pd
import sqlite3
import os

# Base directory (scripts folder)
base_dir = os.path.dirname(__file__)

# Build paths safely
schema_path = os.path.join(base_dir, "..", "sql", "schema.sql")
data_dir = os.path.join(base_dir, "..", "cleaned_data")

# Connect to database
db_path = os.path.join(base_dir, "..", "patents.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON;")

# Load schema
with open(schema_path, "r") as f:
    cursor.executescript(f.read())

# Load CSVs using safe paths
patents = pd.read_csv(os.path.join(data_dir, "clean_patents.csv"))
inventors = pd.read_csv(os.path.join(data_dir, "clean_inventors.csv"))
locations = pd.read_csv(os.path.join(data_dir, "clean_locations.csv"))
companies = pd.read_csv(os.path.join(data_dir, "clean_companies.csv"))
patent_inventor = pd.read_csv(os.path.join(data_dir, "patent_inventor.csv"))

# Insert data
patents.to_sql("patents", conn, if_exists="append", index=False)
locations.to_sql("locations", conn, if_exists="append", index=False)
inventors.to_sql("inventors", conn, if_exists="append", index=False)
companies.to_sql("companies", conn, if_exists="append", index=False)
patent_inventor.to_sql("patent_inventor", conn, if_exists="append", index=False)

print("✅ Database created with schema and data inserted!")

conn.commit()
conn.close()