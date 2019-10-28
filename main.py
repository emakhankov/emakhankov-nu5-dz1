import console_menu as cm
import file_actions as fa
import victory as vict
import bank_account as ba


while True:
    choosed_item = cm.show_menu()
    if choosed_item == 0:
        break
    elif choosed_item == 1:
        fa.create_folder()
    elif choosed_item == 2:
        fa.delete_folder_or_file()
    elif choosed_item == 3:
        fa.copy_folder_or_file()
    elif choosed_item == 4:
        fa.show_working_folder()
    elif choosed_item == 5:
        fa.show_working_folder_only_folders()
    elif choosed_item == 6:
        fa.show_working_folder_only_files()
    elif choosed_item == 7:
        fa.show_os()
    elif choosed_item == 8:
        fa.show_autor()
    elif choosed_item == 9:
        vict.start_victory()
    elif choosed_item == 10:
        ba.start_account()
    elif choosed_item == 11:
        fa.create_folder()
    elif choosed_item == 12:
        fa.open_website()
