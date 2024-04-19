from datetime import datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%y.%m.%d %H:%M')

x = 1
for _ in range(2):
    x *= 5
    x += 1
print(x)

print(formatted_datetime)