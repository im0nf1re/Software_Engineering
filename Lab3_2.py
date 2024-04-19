from datetime import datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%y.%m.%d %H:%M')

for char in "Hello World"[::-1]:
    print(char)

print(formatted_datetime)