CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    traits TEXT,
    onboarded_date TEXT
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT,
    task_date TEXT,
    task TEXT,
    is_done INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS reflections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT,
    reflection_date TEXT,
    soul TEXT,
    mind TEXT,
    body TEXT,
    trust TEXT,
    value TEXT
);

