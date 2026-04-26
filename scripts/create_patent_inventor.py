import pandas as pd

# File paths
input_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\data\g_inventor_disambiguated.tsv"
output_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\cleaned_data\patent_inventor.csv"

# Read in chunks
chunks = pd.read_csv(input_path, sep='\t', chunksize=10000)

cleaned_chunks = []

for chunk in chunks:
    # Select needed columns
    chunk = chunk[['patent_id', 'inventor_id']]

    # Drop missing values
    chunk = chunk.dropna()

    cleaned_chunks.append(chunk)

# Combine all chunks
df = pd.concat(cleaned_chunks)

# Remove duplicates
df = df.drop_duplicates()

# Save to CSV
df.to_csv(output_path, index=False)

print("✅ Patent-Inventor relationship created!")