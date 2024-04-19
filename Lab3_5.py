from datetime import datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%y.%m.%d %H:%M')

string = 'hello'
values = [0, 2, 4, 6, 8, 10]
counter = 0
while counter != 10:
    if counter in values:
        memory = ' world'
    else:
        memory = ''
    print(string + memory)
    counter += 1
print(string + ' world')

print(formatted_datetime)