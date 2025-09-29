from db import load_habits
from analytics.progress import get_all_habit_names, get_habits_by_periodicity, get_longest_streak_all_habits

# Get default habits
habits = load_habits()  

# Test 1: Get all habit names
print('\n✅ All Habit Tracked:')
print(get_all_habit_names(habits))

# Test 2: Get habits by periodicity
print('\n✅ Weekly Habit:')
weekly_habits = get_habits_by_periodicity(habits, 'weekly')
for habit in weekly_habits:
    print(f'- {habit.name} ({habit.periodicity}) | Progress: {habit.progress} | Completions: {len(habit.completions)}')

# Test 3: Get longest streak for all habits

print('\n✅ Longest Streak for All Habits:')
print(get_longest_streak_all_habits(habits))

