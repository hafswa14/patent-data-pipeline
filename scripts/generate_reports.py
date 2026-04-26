import os
import sqlite3
import pandas as pd
import json

# ---------- SETUP ----------
base_dir = os.path.dirname(__file__)
db_path = os.path.join(base_dir, "..", "patents.db")

conn = sqlite3.connect(db_path)

# ---------- QUERY DATA ----------

# Total patents
total_patents = pd.read_sql_query(
    "SELECT COUNT(*) as total FROM patents", conn
).iloc[0]["total"]

# Top inventors
top_inventors = pd.read_sql_query("""
SELECT i.name, COUNT(pi.patent_id) AS patent_count
FROM inventors i
JOIN patent_inventor pi ON i.inventor_id = pi.inventor_id
GROUP BY i.inventor_id
ORDER BY patent_count DESC
LIMIT 10;
""", conn)

# Top companies (based on dataset frequency)
top_companies = pd.read_sql_query("""
SELECT name, COUNT(*) AS total_records
FROM companies
GROUP BY name
ORDER BY total_records DESC
LIMIT 10;
""", conn)

# Top countries
top_countries = pd.read_sql_query("""
SELECT l.country, COUNT(pi.patent_id) AS total_patents
FROM locations l
JOIN inventors i ON l.location_id = i.location_id
JOIN patent_inventor pi ON i.inventor_id = pi.inventor_id
GROUP BY l.country
ORDER BY total_patents DESC
LIMIT 10;
""", conn)

# Trends
country_trends = pd.read_sql_query("""
SELECT year, COUNT(*) AS total_patents
FROM patents
GROUP BY year
ORDER BY year;
""", conn)

# ---------- A. CONSOLE REPORT ----------
print("\n================== PATENT REPORT ===================")
print(f"Total Patents: {total_patents}\n")

print("Top Inventors:")
for i, row in top_inventors.iterrows():
    print(f"{i+1}. {row['name']} - {row['patent_count']}")

print("\nTop Companies:")
for i, row in top_companies.iterrows():
    print(f"{i+1}. {row['name']} - {row['total_records']}")

print("\nTop Countries:")
for i, row in top_countries.iterrows():
    print(f"{i+1}. {row['country']} - {row['total_patents']}")

print("====================================================\n")

# ---------- B. EXPORT CSV FILES ----------
output_dir = os.path.join(base_dir, "..", "reports")
os.makedirs(output_dir, exist_ok=True)

top_inventors.to_csv(os.path.join(output_dir, "top_inventors.csv"), index=False)
top_companies.to_csv(os.path.join(output_dir, "top_companies.csv"), index=False)
country_trends.to_csv(os.path.join(output_dir, "country_trends.csv"), index=False)

print("✅ CSV reports saved!")

# ---------- C. JSON REPORT ----------
report_json = {
    "total_patents": int(total_patents),
    "top_inventors": top_inventors.to_dict(orient="records"),
    "top_companies": top_companies.to_dict(orient="records"),
    "top_countries": top_countries.to_dict(orient="records")
}

with open(os.path.join(output_dir, "report.json"), "w") as f:
    json.dump(report_json, f, indent=4)

print("✅ JSON report saved!")

conn.close()