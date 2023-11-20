def add_user_to(users_list:list) -> None:
    """
    add objcet to list
    :param users_list: lista  - user list
    :return: None
    """

    name = input('podaj imie ?')
    posts = input('podaj liczbe postow ?')
    users_list.append({'name':name,'posts':posts})

def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: user list
    :return: None
    """
    tmp_list = []
    name = input('podaj imie uzytkownika do usuniecia: ')
    for user in users_list:
        if user["name"] == name:
            print(f'znaleziono uzytkownika {user}')
            tmp_list.append(user)
    print('znaleziono uzytkownikow:')
    print('0: Usun wszytskich znalezionych uzytkownikow')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek + 1}. {user_to_be_removed}')
    numer = int(input(f'wybierz numer uzytkownika do usuniecia: '))
    if numer == 0:
        for user in users_list:
            if user['name'] == name:
                users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer - 1])

def show_users_from(users_list:list)->None:
    for user in users_list:
        print(f'twoj znajomy {user["name"]} dodal {user["posts"]}')

def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input('podaj nick użytkownika do modyfikacji')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono!!!!')
            user['name'] = input('podaj nowe imie: ')
            user['nick'] = input('podaj nowa ksywke: ')
            user['posts'] = int(input('podaj liczbę postów: '))
def gui(users_list) -> None:
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
                        update_user(users_list)

