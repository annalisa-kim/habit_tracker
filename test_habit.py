import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from habits.habit import Habit
from db import init_db, save_habit, load_habits
from datetime import date
from pprint import pprint
from fixtures import get_default_habits

# 1: Initialize the database
init_db()

# 2: Create a new Habit instance
habits = get_default_habits()


# 3: Simulate completions
for habit in habits:
    habit.complete()
    habit.complete()
    habit.complete()

# 4: Save the habit to the database
for habit in habits:
    save_habit(habit)

# 5: Load all habits from the database
loaded_habits = load_habits()

# 6: Print loaded habits
print('\n✅ Loaded habits from database:')
for h in loaded_habits:
    print(f'- {h.name} ({h.periodicity}) | Progress: {h.progress} | Completions: {len(h.completions)}')
    pprint(h.to_dict())

