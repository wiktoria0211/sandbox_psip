
from dane import users_list
from utils.my_functions import add_user_to, remove_user_from
def gui()->None:
    while True:
        print(f'MENU: \n'
              F'0: Zakoncz program \n'
              F'1: Wyswietl uzytkownikow \n'
              F'2: dodaj uzytkownikow \n'
              F'3: Usun uzytkownika \n'
              F'4: Modyfikuj uzytkownika'
              )
        menu_option = input('Podaj funkcje do wywolania')
        print(f' Wybrano funkcje {menu_option}')

        match menu_option:
            case '0':
                print('koncze prace')
                break
            case '1':
                print('lista uzytkownikow: ')
                show_users_from(users_list)
            case '2':
                print('dodaje uzytkownika: ')
                add_user_to(users_list)
            case '3':
                print('usun uzytkownika: ')
                remove_user_from(users_list)
            case '4':
                print('modyfikuj uzytkownika')
                print('to bedzie zrobione') # TODO add this function to my_functions
gui(users_list)










