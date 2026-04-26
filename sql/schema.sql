CREATE TABLE patents (
    patent_id TEXT PRIMARY KEY,
    title TEXT,
    filing_date DATE,
    year INTEGER
);

CREATE TABLE locations (
    location_id TEXT PRIMARY KEY,
    country TEXT
);

CREATE TABLE inventors (
    inventor_id TEXT PRIMARY KEY,
    name TEXT,
    location_id TEXT,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

CREATE TABLE companies (
    company_id TEXT PRIMARY KEY,
    name TEXT
);

CREATE TABLE patent_inventor (
    patent_id TEXT,
    inventor_id TEXT,
    PRIMARY KEY (patent_id, inventor_id),
    FOREIGN KEY (patent_id) REFERENCES patents(patent_id),
    FOREIGN KEY (inventor_id) REFERENCES inventors(inventor_id)
);