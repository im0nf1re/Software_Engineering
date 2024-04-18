from datetime import datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%y.%m.%d %H:%M')

day, month, year = 18, 'апрель', 2024
print(f"Сегодня {day} {month} {year}.", end=" Всего хорошего!")

print()
print(formatted_datetime)
