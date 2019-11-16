import json
import os
import sys


FILE_BANK_ACCOUNT_FOLD = os.path.join('./','bank_account_folder')
FILE_BANK_ACCOUNT_NAME = os.path.join(FILE_BANK_ACCOUNT_FOLD, 'bankAccount.json')


def enter_money(question, error):

    inp_str = input(question,).strip()
    if not inp_str.isnumeric():
        print(error)
    return float(inp_str) if inp_str.isnumeric() else 0.0 # ТЕРНАРНЫЙ ОПЕРАТОР


def add_profitable_operation(account, sum):
    account['total'] += sum

def add_expense_operation(account, sum_purchase, name_purchase):
    account['total'] -= sum_purchase
    account['purchases'].append({'sum': sum_purchase, 'name': name_purchase})



def add_funds(account):

    entered_sum = enter_money('Введите сумму пополнения счета: ', 'Ошибка пополнения счета')
    add_profitable_operation(account, entered_sum)

def add_purchase(account):

    sum_purchase = enter_money('Введите сумму покупки: ', 'Ошибка ввода суммы покупки')
    if sum_purchase != 0.0:
        if sum_purchase > account['total']:
            print('Недостаточно средств на счете')
            return
        else:
            name_purchase = ''
            while name_purchase == '':
                name_purchase = input('Введите название покупки: ').strip()
                if name_purchase == '':
                    print('Название покупки не может быть пустым')
            add_expense_operation(account, sum_purchase, name_purchase)


def list_purchases(account):
    print('Ваши покупки:')
    for purchase in account['purchases']:
        print(f'покупка {purchase["name"]:20} на сумму {purchase["sum"]:10.2f}')


def get_default_account():
    return {'total': 0.0, 'purchases': []}


def get_account():
    """
    Получаем начальное состояние счета, зачитываем из файла json, если файл отсутствует возвращаем пустой инициализированный счет
    :return: dict - объект банковский счет
    """
    try:  # ОБРАБОТКА ИСКЛЮЧЕНИЙ
        if os.path.exists(FILE_BANK_ACCOUNT_NAME):
            with open(FILE_BANK_ACCOUNT_NAME, "r", encoding='UTF-8') as f:
                return json.load(f)
        else:
            return get_default_account()
    except:
        print('Проблемы с чтением', sys.exc_info()[0])
        raise


def save_account(account):
    """
    Сохранение состояния банковского счета при выходе из програииы
    :param account: Банковский счет
    :return:
    """
    try: # ОБРАБОТКА ИСКЛЮЧЕНИЙ
        os.makedirs(FILE_BANK_ACCOUNT_FOLD, exist_ok=True)
        with open(FILE_BANK_ACCOUNT_NAME, "w", encoding='UTF-8') as f:
            return json.dump(account, f, ensure_ascii=False)  # Для создания нормального русского джейсона
    except:
        print('Проблемы с записью', sys.exc_info()[0])


def start_account():

    account = get_account()

    while True:
        print(f'У вас с счету {account["total"]: .2f}')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            add_funds(account)
            print()
        elif choice == '2':
            add_purchase(account)
            print()
        elif choice == '3':
            list_purchases(account)
            print()
        elif choice == '4':
            save_account(account)
            return
        else:
            print('Неверный пункт меню')