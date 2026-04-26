import pandas as pd

# File paths
input_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\data\g_patent.tsv"
output_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\cleaned_data\clean_patents.csv"

# Read data (use chunking for large file)
chunks = pd.read_csv(input_path, sep='\t', chunksize=10000)

cleaned_chunks = []

for chunk in chunks:
    # Select needed columns
    chunk = chunk[['patent_id', 'patent_title', 'patent_date']]

    # Rename columns
    chunk = chunk.rename(columns={
        'patent_title': 'title',
        'patent_date': 'filing_date'
    })

    # Convert date to year
    chunk['year'] = pd.to_datetime(chunk['filing_date'], errors='coerce').dt.year

    cleaned_chunks.append(chunk)

# Combine all chunks
df = pd.concat(cleaned_chunks)

# Save to CSV
df.to_csv(output_path, index=False)

print("✅ Patents data processed and saved!")