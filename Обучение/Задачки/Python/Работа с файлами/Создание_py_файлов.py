# Программа использовалась для создания .py файлов, для удобства,
# чтобы не тратить много времени на создание их вручную
# можно изменить параметры
count = 173
for a in range(13):
    count += 1
    filename = 'Ex' + str(count) + '.py'
    with open(filename, 'w') as file:
        content = '""""""'
        file.write(content)