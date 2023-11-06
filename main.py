
from dane import users_list

def add_user_to(users_list:list) -> None:
    """
    add objcet to list
    :param users_list: lista  - user list
    :return: None
    """

    name = input('podaj imie ?')
    posts = input('podaj liczbe postow ?')
    users_list.append({'nick':name,'posts':posts})

def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: user list
    :return: None
    """
    tmp_list = []
    name = input('podaj imie uzytkownika do usuniecia: ')
    for user in users_list:
        if user["name"]== name:
            print(f'znaleziono uzytkownika {user}')
            tmp_list.append(user)
    print('znaleziono uzytkownikow:')
    print('0: Usun wszytskich znalezionych uzytkownikow')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}. {user_to_be_removed}')
    numer = int(input(f'wybierz numer uzytkownika do usuniecia: '))
    if numer == 0:
        for user in users_list:
            if user['name'] == name:
                users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer-1])

    print(numer)
    print(tmp_list[numer-1])
    users_list.remove(tmp_list[numer-1])

remove_user_from(users_list)

#print(users_list)
for users in users_list:
    print(f'Twój znajomy {users["nick"]} dodał {users["posts"]}!!')












