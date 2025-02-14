questions = [
    "Как вас зовут?",
    "Сколько вам лет?",
    "Какой ваш любимый цвет?",
    "Где вы живете?",
    "Какой ваш любимый фильм?",
    "Какое ваше хобби?",
    "Какую книгу вы недавно прочитали?",
    "Какую музыку вы предпочитаете?",
    "Какова ваша любимая еда?",
    "Какова ваша мечта?"
]

answers_list = []
count = 0


while count < len(questions):
    answer = input(questions[count] + " ") # Простая подсказка, 1) обращение к списку 2) Обращение к индексу
    answers_list.append(answer)
    count += 1

# print() можно сделать таким образом
print("\nРезультат:")

index = 0
for answer in answers_list:
    print(f'{index + 1}. {questions[index]} - {answer}')
    index += 1

# for i, answer in enumerate(answers_list):
#     print(f"{i + 1}. {questions[i]} - {answer}")