import os
import sqlite3
import pandas as pd
import streamlit as st

# ---------- SETUP ----------
st.set_page_config(page_title="Patent Dashboard", layout="wide")

st.title("📊 Patent Data Dashboard")

base_dir = os.path.dirname(__file__)
db_path = os.path.join(base_dir, "..", "patents.db")

conn = sqlite3.connect(db_path)

# ---------- LOAD DATA ----------

with st.spinner("Loading data... please wait ⏳"):

    total_patents = pd.read_sql_query(
        "SELECT COUNT(*) as total FROM patents", conn
    ).iloc[0]["total"]

    top_inventors = pd.read_sql_query("""
    SELECT i.name, COUNT(pi.patent_id) AS patent_count
    FROM inventors i
    JOIN patent_inventor pi ON i.inventor_id = pi.inventor_id
    GROUP BY i.inventor_id
    ORDER BY patent_count DESC
    LIMIT 10;
    """, conn)

    top_countries = pd.read_sql_query("""
    SELECT l.country, COUNT(pi.patent_id) AS total_patents
    FROM locations l
    JOIN inventors i ON l.location_id = i.location_id
    JOIN patent_inventor pi ON i.inventor_id = pi.inventor_id
    GROUP BY l.country
    ORDER BY total_patents DESC
    LIMIT 10;
    """, conn)

    trends = pd.read_sql_query("""
    SELECT year, COUNT(*) AS total_patents
    FROM patents
    GROUP BY year
    ORDER BY year;
    """, conn)

st.success("Data loaded successfully!")

@st.cache_data
def load_data():
    total_patents = pd.read_sql_query(
        "SELECT COUNT(*) as total FROM patents", conn
    ).iloc[0]["total"]

    top_inventors = pd.read_sql_query("""
    SELECT i.name, COUNT(pi.patent_id) AS patent_count
    FROM inventors i
    JOIN patent_inventor pi ON i.inventor_id = pi.inventor_id
    GROUP BY i.inventor_id
    LIMIT 10;
    """, conn)

    top_countries = pd.read_sql_query("""
    SELECT l.country, COUNT(pi.patent_id) AS total_patents
    FROM locations l
    JOIN inventors i ON l.location_id = i.location_id
    JOIN patent_inventor pi ON i.inventor_id = pi.inventor_id
    GROUP BY l.country
    LIMIT 10;
    """, conn)

    trends = pd.read_sql_query("""
    SELECT year, COUNT(*) AS total_patents
    FROM patents
    GROUP BY year
    ORDER BY year;
    """, conn)

    return total_patents, top_inventors, top_countries, trends

# ---------- DASHBOARD ----------    

# Metric
st.metric("Total Patents", f"{total_patents:,}")

# Layout
col1, col2 = st.columns(2)

# Top Inventors
with col1:
    st.subheader("Top Inventors")
    st.dataframe(top_inventors)

# Top Countries
with col2:
    st.subheader("Top Countries")
    st.dataframe(top_countries)

# Trends Chart
st.subheader("Patent Trends Over Time")
st.line_chart(trends.set_index("year"))

conn.close()