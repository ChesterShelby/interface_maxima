"""
Функция read() используется для чтения содержимого файла после открытия его в режиме чтения (r).

file.read(size)


file = объект файла
size = количество символов, которые нужно прочитать. Если не указать, то файл прочитается целиком.

"""
f = open('example_1.txt', 'r')
print(f.read(7))    # чтение 7 символов из example.txt
print(f.read(7))    # чтение следующих 7 символов
