"""
QVariant — может хранить данные любого типа. Создать экземпляр этого класса можно
вызовом конструктора, передав ему нужное значение. А чтобы преобразовать данные,
хранящиеся в экземпляре класса QVariant, в тип данных Python, нужно вызвать метод
value():
"""

from PyQt5 import QtCore
n = QtCore.QVariant(10)
print(n)
print(n.value())

"""
Также можно создать «пустой» экземпляр класса QVariant, вызвав конструктор без параметров:
"""

print(QtCore.QVariant())

"""
Если какой-либо метод ожидает данные типа QVariant, ему можно передать данные любого типа.
Еще этот класс поддерживает метод typeName(), возвращающий наименование типа хранящихся в экземпляре данных:
"""

print(n.typeName())

"""
Кроме того, PyQt 5 поддерживает классы QDate (значение даты), QTime (значение времени),
QDateTime (значение даты и времени), QTextStream (текстовый поток), QUrl (URL-адрес) и
некоторые другие.
"""
