


def enter_money(question, error):

    inp_str = input(question,).strip()
    if inp_str.isnumeric():
        return float(inp_str)
    else:
        print(error)
        return 0.0




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


def start_account():

    account = get_default_account

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
            return
        else:
            print('Неверный пункт меню')