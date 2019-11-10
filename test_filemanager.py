import bank_account as ba
import file_actions as fa
import platform
import os

def test_get_default_account():
    assert ba.get_default_account() == {'total': 0.0, 'purchases': []}


def test_add_expense_operation():
    account = ba.get_default_account()
    account['total'] = 100
    ba.add_expense_operation(account, 10, 'underpants')
    ba.add_expense_operation(account, 5, 'socks')
    assert account['total'] == 85
    assert len(account['purchases']) == 2
    assert list(map(lambda x: x['name'], account['purchases'])) == ['underpants', 'socks']


def test_add_profitable_operation():
    account = ba.get_default_account()
    ba.add_profitable_operation(account, 100)
    assert account['total'] == 100

def test_show_os(capsys):
    """
    Тест грядной функции
    :param capsys: Какая то фигня куда передается ссылка на stdout
    :return:
    """
    fa.show_os()
    captured = capsys.readouterr()
    text = captured.out
    assert text.find(platform.system()) != -1


def test_show_autor(capsys):
    """
    Тест грязной функции, на то что какие-то гады не удалили упоминание о главном разработчике прокраммы
    :param capsys:
    :return:
    """
    fa.show_autor()
    captured = capsys.readouterr()
    text = captured.out.lower()
    assert text.find('makhankov') != -1


def test_create_folder(monkeypatch):
    """
    Тест грязной функции. Создания папки с запросом ее имени через input
    :param monkeypatch: какая-то фигня гуда можно закинуть значения для инпута
    :return:
    """
    test_fold_name = 'dir987654321'
    if os.path.exists(test_fold_name):
        os.rmdir(test_fold_name)
    monkeypatch.setattr('builtins.input', lambda x: test_fold_name)
    fa.create_folder()
    assert os.path.exists(test_fold_name)
    os.rmdir(test_fold_name)


def test_get_account():
    if os.path.exists(ba.FILE_BANK_ACCOUNT_NAME):
        os.remove(ba.FILE_BANK_ACCOUNT_NAME)
    assert ba.get_account() == {'total': 0.0, 'purchases': []}


def test_save_account():
    account = ba.get_default_account()
    ba.add_profitable_operation(account, 100)
    ba.save_account(account)
    account2 = ba.get_account()
    assert account['total'] == account2['total']


def test_save_working_folder():
    fa.save_working_folder()
    assert os.path.exists(fa.FILE_LISTDIR)
    with open(fa.FILE_LISTDIR, "r", encoding='UTF-8') as f:
        s = f.read()
        assert s.find('test_filemanager.py') != -1
