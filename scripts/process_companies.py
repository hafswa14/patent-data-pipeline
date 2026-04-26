import pandas as pd

# File paths
input_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\data\g_assignee_disambiguated.tsv"
output_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\cleaned_data\clean_companies.csv"

# Read in chunks
chunks = pd.read_csv(input_path, sep='\t', chunksize=10000)

cleaned_chunks = []

for chunk in chunks:
    # Keep only organization names
    chunk = chunk[['assignee_id', 'disambig_assignee_organization']]

    # Drop rows without company name
    chunk = chunk.dropna(subset=['disambig_assignee_organization'])

    # Rename
    chunk = chunk.rename(columns={
        'assignee_id': 'company_id',
        'disambig_assignee_organization': 'name'
    })

    cleaned_chunks.append(chunk)

# Combine
df = pd.concat(cleaned_chunks)

# Remove duplicates
df = df.drop_duplicates(subset=['company_id'])

# Save
df.to_csv(output_path, index=False)

print("✅ Companies data processed and saved!")