import pandas as pd

# File paths
input_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\data\g_inventor_disambiguated.tsv"
output_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\cleaned_data\clean_inventors.csv"

# Read in chunks
chunks = pd.read_csv(input_path, sep='\t', chunksize=10000)

cleaned_chunks = []

for chunk in chunks:
    # Select relevant columns
    chunk = chunk[['inventor_id', 'disambig_inventor_name_first', 'disambig_inventor_name_last', 'location_id']]

    # Create full name
    chunk['name'] = chunk['disambig_inventor_name_first'].fillna('') + ' ' + chunk['disambig_inventor_name_last'].fillna('')

    # Keep required columns
    chunk = chunk[['inventor_id', 'name', 'location_id']]

    cleaned_chunks.append(chunk)

# Combine all chunks
df = pd.concat(cleaned_chunks)

# Remove duplicates
df = df.drop_duplicates(subset=['inventor_id'])

# Save to CSV
df.to_csv(output_path, index=False)

print("✅ Inventors data processed and saved!")