def get_all_habit_names(habits):
    return [habit.name for habit in habits] # Returns a list of all habit names

def get_habits_by_periodicity(habits, periodicity):
    return [habit for habit in habits if habit.periodicity == periodicity] # Returns a list of habits filtered by periodicity

from datetime import datetime, timedelta
from collections import defaultdict

def calculate_streak(habit): # Calculate the longest streaks for a single habit
    if not habit.completions:
        return 0
    # Order completions by date
    completions = sorted(habit.completions)
    streak = max_streak = 1
    for i in range(1, len(completions)):
        prev = completions[i - 1]
        curr = completions[i]
    # Calculate expected delta based on periodicity
        if habit.periodicity == 'daily':
            expected = prev + timedelta(days=1)
        elif habit.periodicity == 'weekly':
            expected = prev + timedelta(weeks=1)
        elif habit.periodicity == 'monthly':
            expected = prev + timedelta(days=30)
        elif habit.periodicity == 'yearly':
            expected = prev + timedelta(days=365)
        else:
            continue
        if abs((curr - expected).days) <= 1:
            streak += 1
        else:
            streak += 1

        max_streak = max(max_streak, streak)

    return max_streak

def get_longest_streak_all_habits(habits):
    return max((calculate_streak(habit) for habit in habits), default=0) # Returns the longest streak across all habits

def get_longest_streak_for_habit(habit):
    return calculate_streak(habit) # Returns the longest streak for a specific habit
