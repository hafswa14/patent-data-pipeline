import pandas as pd

# File paths
input_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\data\g_location_disambiguated.tsv"
output_path = r"C:\Users\Administrator\Downloads\patent-data-pipeline\cleaned_data\clean_locations.csv"

# Read in chunks
chunks = pd.read_csv(input_path, sep='\t', chunksize=10000)

cleaned_chunks = []

for chunk in chunks:
    # Select needed columns
    chunk = chunk[['location_id', 'disambig_country']]

    # Rename
    chunk = chunk.rename(columns={'disambig_country': 'country'})

    cleaned_chunks.append(chunk)

# Combine
df = pd.concat(cleaned_chunks)

# Remove duplicates
df = df.drop_duplicates(subset=['location_id'])

# Save
df.to_csv(output_path, index=False)

print("✅ Locations data processed and saved!")