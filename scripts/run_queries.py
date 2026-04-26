import os
import sqlite3

base_dir = os.path.dirname(__file__)
db_path = os.path.join(base_dir, "..", "patents.db")

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Create indexes (run once)
cursor.executescript("""
CREATE INDEX IF NOT EXISTS idx_inventor_id ON inventors(inventor_id);
CREATE INDEX IF NOT EXISTS idx_patent_inventor_inv ON patent_inventor(inventor_id);
CREATE INDEX IF NOT EXISTS idx_patent_inventor_pat ON patent_inventor(patent_id);
CREATE INDEX IF NOT EXISTS idx_location_id ON locations(location_id);
""")

print("✅ Indexes created!\n")

# Run query
query = """SELECT AVG(inventor_count) AS avg_inventors_per_patent
FROM (
    SELECT patent_id, COUNT(inventor_id) AS inventor_count
    FROM patent_inventor
    GROUP BY patent_id
);

"""

cursor.execute(query)

results = cursor.fetchall()

print("Average Number of Inventors per Patent:\n")
for row in results:
    print(row)

conn.close()