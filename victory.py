import random

MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

FAMOUS_PEOPLE = [
    {'Name': 'Путин В.В.',      'DateOfBirth': '07.10.1952'},
    {'Name': 'Ленин В.И.',      'DateOfBirth': '22.04.1870'},
    {'Name': 'Сталин И.В.',     'DateOfBirth': '18.12.1878'},
    {'Name': 'Рузвельт Ф.Д.',   'DateOfBirth': '30.01.1882'},
    {'Name': 'Черчель У.',      'DateOfBirth': '30.11.1874'},
    {'Name': 'Гагарин Ю.А.',    'DateOfBirth': '09.03.1934'},
    {'Name': 'Трамп Д.',        'DateOfBirth': '14.06.1946'},
    {'Name': 'Леонардо Д.В.',   'DateOfBirth': '15.04.1452'},
    {'Name': 'Де Голь Ш.',      'DateOfBirth': '22.11.1890'},
    {'Name': 'Кастро Ф.',       'DateOfBirth': '13.08.1926'}
    ]
AMOUNT_OF_QUESTIONS = 5
amount_of_famous_people = len(FAMOUS_PEOPLE)


def start_victory():

    while True:
        dices_of_question = random.sample(list(range(amount_of_famous_people)), AMOUNT_OF_QUESTIONS)

        correct_answers = 0
        for dice in dices_of_question:
            question = FAMOUS_PEOPLE[dice]
            birthday = input(f'Введите дату рождения {question["Name"]} в формате dd.mm.yyyy: ').strip()
            if birthday == question['DateOfBirth']:
                print('правильно')
                correct_answers += 1
            else:
                birthday_array = question['DateOfBirth'].split('.')
                print('неверно, но правильный ответ {} {} {} года.'.format(int(birthday_array[1]),MONTHS[int(birthday_array[1])-1],int(birthday_array[2])))

        print('Количество правильных ответов:', correct_answers)
        print('Количество неверных ответов:', AMOUNT_OF_QUESTIONS - correct_answers)

        if input('Сыграем еще: (да/нет)?:').lower().strip() != 'да':
            return