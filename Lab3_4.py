from datetime import datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%y.%m.%d %H:%M')

sentence = input("Введите предложение на английском: ")
print("Длина предложения:", len(sentence))
lower_sentence = sentence.lower()
print("Предложение в нижнем регистре:", lower_sentence)
vowels_count = sum(1 for char in lower_sentence if char in 'aeiou')
print("Количество гласных в предложении:", vowels_count)
beautified_sentence = lower_sentence.replace("ugly", "beauty")
print("Предложение после замены 'ugly' на 'beauty':", beautified_sentence)
starts_with_the = sentence.startswith("The")
ends_with_end = sentence.endswith("end")
print("Начинается ли предложение с 'The'?", starts_with_the)
print("Заканчивается ли предложение на 'end'?", ends_with_end)

print(formatted_datetime)