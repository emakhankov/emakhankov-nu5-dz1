import os
import shutil
import platform
import webbrowser


def create_folder():

    fold_name = input('Введите имя создаваемой директории: ')
    if os.path.exists(fold_name):
        print(f'Директория {fold_name} уже существует')
        return False
    os.mkdir(fold_name)
    print(f'Директория {fold_name} успешно создана')
    return True


def delete_folder_or_file():

    file_name = input('Введите удаляемого файла или директории: ')
    if not os.path.exists(file_name):
        print(f'Файл или директория  {file_name} не существует')
        return False
    if os.path.isdir(file_name):
        os.rmdir(file_name)
        print(f'Директоия {file_name} успешно удалена')
    elif os.path.isfile(file_name):
        os.remove(file_name)
        print(f'Файл {file_name} успешно удален')


def copy_folder_or_file():

    file_name = input('Введите копируемого файла или директории: ')
    destination_file_name = input('Введите новое имя: ')
    if not os.path.exists(file_name):
        print(f'Файл или директория  {file_name} не существует')
        return False
    if os.path.exists(destination_file_name):
        print(f'Директория или файл назначения {destination_file_name} уже существует')
        return False
    if os.path.isdir(file_name):
        shutil.copytree(file_name, destination_file_name)
        print(f'Директория {file_name} успешно скопирована')
    elif os.path.isfile(file_name):
        shutil.copyfile(file_name, destination_file_name)
        print(f'Файл {file_name} успешно скопирован')


def show_working_folder():

    print(f'\n'.join(os.listdir(os.getcwd())))


def show_working_folder_only_folders():

    print(f'\n'.join([f for f in os.listdir(os.getcwd()) if os.path.isdir(f)]))


def show_working_folder_only_files():

    print(f'\n'.join([f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]))


def show_os():

    print(platform.system(), platform.release())


def show_autor():

    print('(C) Evgeny Makhankov')


def change_working_folder():

    folder_name = input('Введите новое имя рабочей директории: ')
    if not os.path.exists(folder_name):
        print(f'Данной директории {folder_name} не существует')
        return
    if not os.path.isdir(folder_name):
        print(f'"Это не директория {folder_name}')
        return
    os.chdir(folder_name)


def open_website():

    webbrowser.open('https://neural-university.ru/python-developer')

