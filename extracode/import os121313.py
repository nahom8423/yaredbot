from datetime import datetime

# Getting the current week number using isocalendar method
current_week_number = datetime.now().isocalendar()[1]
print(current_week_number)
