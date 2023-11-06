
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

add_user_to(users_list)
add_user_to(users_list)
add_user_to(users_list)


for users in users_list:
    print(f'Twój znajomy {users["nick"]} dodał {users["posts"]}!!')












