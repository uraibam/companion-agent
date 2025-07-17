-- Users table stores onboarding data
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    traits TEXT,
    onboarded_date TEXT DEFAULT CURRENT_DATE
);

-- Tasks assigned to users, tracked by date and completion
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT NOT NULL,
    task_date TEXT NOT NULL,
    task TEXT NOT NULL,
    is_done INTEGER DEFAULT 0 CHECK (is_done IN (0, 1))
);

-- Daily SMBTV reflections per user
CREATE TABLE IF NOT EXISTS reflections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT NOT NULL,
    reflection_date TEXT DEFAULT CURRENT_DATE,
    soul TEXT,
    mind TEXT,
    body TEXT,
    trust TEXT,
    value TEXT
);
