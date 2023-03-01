"""
Модули могут точно управлять набором имен, импортируемых командой from модуль import *,
для чего определяют список __all__:
"""

__all__ = ['func', 'MyClass']

number = 35  # Не экспортируется


def func():  # Экспортируется
    print('Hello')


class MyClass:  # Экспортируется
    pass