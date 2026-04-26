import os

print(" Starting Patent Data Pipeline...\n")

scripts = [
    "process_patents.py",
    "process_inventors.py",
    "process_locations.py",
    "process_companies.py"
]

for script in scripts:
    print(f"Running {script}...")
    os.system(f"python scripts/{script}")

print("\n Pipeline completed successfully!")