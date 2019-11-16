import sys
"""
Модуль описывающий вывод на экран консольного меню
"""

MENU_ITEMS = [['1', 'создать папку'], ['2', 'удалить(файл / папку)'], ['3', 'копировать(файл / папку)'],
              ['4', 'просмотр содержимого рабочей директории'],
              ['41', 'сохранение содержимого рабочей директории в файл'],
              ['5', 'посмотреть только папки'], ['6', 'посмотреть только файлы'],
              ['7', 'просмотр информации об операционной системе'],
              ['8', 'создатель программы'], ['9', 'играть в викторину'], ['10', 'мой банковский счет'],
              ['11', 'создать папку'],  ['12', 'открыть интернет сайт курса']]


def decorator_beautiful_menu(f_menu): # ДЕКОРАТОР

    def inner(*args, **kwargs):
        print()
        print('*' * 5, 'Супер программа слушателя курса Pytnon', '*' * 5)
        result = f_menu(*args, **kwargs)
        return result

    return inner


@decorator_beautiful_menu # ДЕКОРАТОР
def show_menu():

    print('Выберите действие:')

    for item in [f'{item[0]}. {item[1]}' for item in MENU_ITEMS]:
        print(item)
    print('0. выход')
    print('-'*10)

    n_text = ''
    items_n = [item[0] for item in MENU_ITEMS] # ГЕНЕРАТОР
    while not (items_n == '0') and not (n_text in items_n):
        n_text = input('Введите число: ')
        try: # ОБРАБОТКА ИСКЛЮЧЕНИЙ
            return int(n_text)
        except ValueError:
            print('Введено не число')
        except:
            print('Чета Вы наделали', sys.exc_info()[0])


