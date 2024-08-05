"""
Упражнение 90. Двенадцать дней Рождества.
Напишите программу, которая будет сама строить куплеты этой песенки.
В программе должна присутствовать функция для отображения одного куплета.
В качестве входного параметра она должна принимать порядковый номер дня,
а в качестве результата возвращать готовый куплет.
Далее в основной программе эта функция должна быть вызвана 12 раз подряд.
Каждая строка с очередным подарком должна присутствовать в вашей программе лишь раз,
за исключением строки «A partridge in a pear tree».
В этом случае вы можете отдельно хранить такой вид строки для первого куплета и слегка измененный
(«And a partridge in a pear tree») – для всех последующих.
Импортируйте свою функцию из упражнения 89 для выполнения этого задания.
"""
#from файл import функция

def displayVerse(n):
    print("On the first day of Christmas")
    print("my true love sent to me:")
    if n >= 12:
        print("Twelve drummers drumming,")
        if n >= 11:
            print("Eleven pipers piping,")
        if n >= 10:
            print("Ten lords a–leaping,")
        if n >= 9:
            print("Nine ladies dancing,")
        if n >= 8:
            print("Eight maids a–milking,")
        if n >= 7:
            print("Seven swans a–swimming,")
        if n >= 6:
            print("Six geese a–laying,")
        if n >= 5:
            print("Five golden rings,")
        if n >= 4:
            print("Four calling birds,")
        if n >= 3:
            print("Three French hens,")
        if n >= 2:
            print("Two turtle doves,")
        if n == 1:
            print("A", end=" ")
        else:
            print("And a", end=" ")
        print("partridge in a pear tree.")
        print()
# Отображаем все 12 куплетов песни
def go():
    for verse in range(1, 13):
        displayVerse(verse)
# Вызываем основную функцию main()
