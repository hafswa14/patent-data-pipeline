-- Query 1: Top 10 Inventors by Patent Count
SELECT i.name, COUNT(pi.patent_id) AS patent_count
FROM inventors i
JOIN patent_inventor pi ON i.inventor_id = pi.inventor_id
GROUP BY i.inventor_id
ORDER BY patent_count DESC
LIMIT 10;

-- Query 2: Top 10 Countries by Patent Count
SELECT l.country, COUNT(pi.patent_id) AS total_patents
FROM locations l
JOIN inventors i ON l.location_id = i.location_id
JOIN patent_inventor pi ON i.inventor_id = pi.inventor_id
GROUP BY l.country
ORDER BY total_patents DESC
LIMIT 10;

-- Query 3: Patent Trends Over Time
SELECT year, COUNT(*) AS total_patents
FROM patents
GROUP BY year
ORDER BY year;

-- Query 4: Top Companies (by frequency in dataset)
SELECT name, COUNT(*) AS total_records
FROM companies
GROUP BY name
ORDER BY total_records DESC
LIMIT 10;

-- Query 5: Average Number of Inventors per Patent
SELECT AVG(inventor_count) AS avg_inventors_per_patent
FROM (
    SELECT patent_id, COUNT(inventor_id) AS inventor_count
    FROM patent_inventor
    GROUP BY patent_id
);