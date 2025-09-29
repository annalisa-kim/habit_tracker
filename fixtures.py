from datetime import date
from habits.habit import Habit

def get_default_habits():
    return [
        Habit(name="Drink water", periodicity="daily", category="Health", target=8, start_date=date.today()),
        Habit(name="Read a book", periodicity="daily", category="Study", target=1, start_date=date.today()),
        Habit(name="Workout", periodicity="weekly", category="Fitness", target=3, start_date=date.today()),
        Habit(name="Review goals", periodicity="weekly", category="Personal", target=1, start_date=date.today()),
        Habit(name="Budget review", periodicity="monthly", category="Finance", target=1, start_date=date.today()),
        Habit(name="Dentist", periodicity="yearly", category="Health", target=1, start_date=date.today()),
    ]

