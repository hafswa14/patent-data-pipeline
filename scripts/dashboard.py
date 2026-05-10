import os
import sqlite3
import pandas as pd
import streamlit as st

# ---------- SETUP ----------
st.set_page_config(page_title="Patent Dashboard", layout="wide")

st.title("📊 Patent Data Dashboard")

base_dir = os.path.dirname(__file__)
#db_path = os.path.join(base_dir, "..", "patents.db")
# Use demo DB for testing
db_path = os.path.join(base_dir, "..", "patents_demo.db")  

conn = sqlite3.connect(db_path)

# ---------- LOAD DATA ----------

@st.cache_data(show_spinner=False)
def load_data():

    total_patents = pd.read_sql_query(
        "SELECT COUNT(*) as total FROM patents", conn
    ).iloc[0]["total"]

    total_inventors = pd.read_sql_query(
        "SELECT COUNT(DISTINCT inventor_id) as total FROM inventors", conn
    ).iloc[0]["total"]

    total_countries = pd.read_sql_query(
        "SELECT COUNT(DISTINCT country) as total FROM locations", conn
    ).iloc[0]["total"]

    total_companies = pd.read_sql_query(
        "SELECT COUNT(DISTINCT name) as total FROM companies", conn
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

    return (
        total_patents,
        total_inventors,
        total_countries,
        total_companies,
        top_inventors,
        top_countries,
        trends
    )


with st.spinner("Loading data... please wait ⏳"):

    (
        total_patents,
        total_inventors,
        total_countries,
        total_companies,
        top_inventors,
        top_countries,
        trends
    ) = load_data()

st.success("Data loaded successfully!")


# ---------- DASHBOARD ----------    

# Metric
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patents", f"{total_patents:,}")
col2.metric("Total Inventors", f"{total_inventors:,}")
col3.metric("Total Countries", f"{total_countries:,}")
col4.metric("Total Companies", f"{total_companies:,}")

st.divider()

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

st.divider()

#Top Inventors Chart
st.subheader("Top Inventors (Visualization)")
st.bar_chart(top_inventors.set_index("name"))

#Top Countries Chart
st.subheader("Top Countries (Visualization)")
st.bar_chart(top_countries.set_index("country"))

# Trends Chart
st.subheader("Patent Trends Over Time")
st.line_chart(trends.set_index("year"))

conn.close()

#streamlit run scripts/dashboard.py