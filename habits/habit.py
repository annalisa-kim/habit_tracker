from datetime import datetime

class Habit:
    def __init__(self, name, periodicity, category=None, target=None, start_date=None):
        self.name = name
        self.periodicity = periodicity
        self.category = category
        self.target = target
        self.start_date = start_date if start_date else datetime.now() .date()
        self.created_at = datetime.now()
        self.completions = []
        self.progress = 0
        self.completed_today = False
        self.badges = []
        self.mood = {}

    def complete(self):
        now = datetime.now()
        self.completions.append(now)
        self.progress += 1

        if self.target and self.progress >= self.target:
            self.completed_today = True
        elif not self.target:
            self.completed_today = True

    def reset_daily_status (self):
        self.completed_today = False 
        self.progress = 0

    def to_dict(self):
        return {
            'name': self.name,
            'periodicity': self.periodicity,
            'category': self.category,
            'target': self.target,
            'start_date': self.start_date.isoformat(),
            'created_at': self.created_at.isoformat(),
            'completions': [dt.isoformat() for dt in self.completions],
            'progress': self.progress,
            'completed_today': self.completed_today,
            'badges': self.badges,
            'mood': self.mood
        }
        
    @staticmethod
    def from_dict(data):
        habit = Habit(
            name=data['name'],
            periodicity=data['periodicity'],
            category=data.get('category'),
            target=data.get('target'),
            start_date=datetime.fromisoformat(data['start_date']).date()
        )
        habit.created_at = datetime.fromisoformat(data['created_at'])
        habit.completions = [datetime.fromisoformat(dt) for dt in data['completions']]
        habit.progress = data['progress']
        habit.completed_today = data['completed_today']
        habit.badges = data.get('badges', [])
        habit.mood = data.get('mood', {})
        return habit
