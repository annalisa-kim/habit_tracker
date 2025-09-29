import sqlite3
from datetime import datetime
from habits.habit import Habit
import json

DB_NAME = 'habits.db'

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                name TEXT PRIMARY KEY,
                periodicity TEXT NOT NULL,
                category TEXT,
                target INTEGER,
                start_date DATE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                completions TEXT,
                progress INTEGER DEFAULT 0,
                completed_today BOOLEAN DEFAULT FALSE,
                badges TEXT,
                mood TEXT
            )
        ''')
        conn.commit()

def save_habit(habit):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO habits (name, periodicity, category, target, start_date, created_at, completions, progress, completed_today, badges, mood)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            habit.name,
            habit.periodicity,
            habit.category,
            habit.target,
            habit.start_date.isoformat(),
            habit.created_at.isoformat(),
            json.dumps([dt.isoformat() for dt in habit.completions]),
            habit.progress,
            int(habit.completed_today),
            json.dumps(habit.badges),
            json.dumps(habit.mood)
        ))
        conn.commit()

def load_habits():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM habits')
        rows = cursor.fetchall()
        habits = []
        for row in rows:
            data = {
                'name': row[0],
                'periodicity': row[1],
                'category': row[2],
                'target': row[3],
                'start_date': row[4],
                'created_at': row[5],
                'completions': json.loads(row[6]),
                'progress': row[7],
                'completed_today': bool (row[8]),
                'badges': json.loads(row[9]) if row[9] else [],
                'mood': json.loads(row[10]) if row[10] else {},
            }
            habits.append(Habit.from_dict(data))
        return habits