from dane import users_list
from bs4 import BeautifulSoup
import requests
import folium
import sqlalchemy.orm
from dotenv import load_dotenv
from geoalchemy2 import Geometry
import os
from sqlalchemy import Column, Integer, String
from dml import db_params

load_dotenv()
engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base = sqlalchemy.orm.declarative_base()


def GUI(users_list):
    while True:
        print('\nWelcome facebook\n'
              f'0: Goodbay facebook\n'
              f'1: wyswietl uytkownikow\n'
              f'2: dodaj uzytkownika\n'
              f'3: usun uzytkownika\n'
              f'4. modyfikuj uzytkownika\n'
              f'5. mapa jednego uzytkownika\n'
              f'6. mapka wszystkich uzytkownikow\n'
              f'7. utwórz tabele\n'
              f'8. wyczyść tabele z danych\n'
              f'9. utworz tabele z przykladowymi danymi\n')
        wyb = int(input('podaj docelowa funkcje '))
        print('wybrano', wyb)

        match wyb:
            case 0:
                print('\ngoodbay')
                session.flush()
                connection.close()
                engine.dispose()
                break
            case 1:
                print('wyswietl uzytkownikow')
                show_sql(db_params)
            case 2:
                print('dodawanie uzytkownika')
                add_sql(users_list, db_params)
            case 3:
                print('usuwanie uzytkownika')
                remove_sql(users_list, db_params)
            case 4:
                print('modyfikacja uzytkownika')
                updage_sql(users_list, db_params)
            case 5:
                print('rysuj mape uzytkownika:')
                user = input('podaj jego imie: ')
                for item in users_list:
                    if item['name'] == user:
                        get_map_of_single(item)
            case 6:
                print('wyswietlenie mapy wszytskich uzytkownikow')
                get_map_of(users_list)
            case 7:
                print('utworzono tabele')
                tworzenie(db_params)
            case 8:
                print('usunieto dane z tabeli')
                zamkniecie(db_params)
            case 9:
                print('dodano tabele wraz z danymi')
                zmiana_tabeli(db_params)


def get_map_of_single(user: str):
    xy = get_coords(user['city'])
    mapa = folium.Map(location=xy, tiles='OpenStreetMap', zoom_start=14)
    folium.Marker(location=xy, popup=f"tu jestes\n{user['name']}").add_to(mapa)

    mapa.save(f'map_{user["name"]}.html')
    print('\nwykonano')


def get_map_of(users):
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)

    for user in users:
        aa = get_coords(city=user['city'])
        folium.Marker(location=aa, popup=f"you are here\n{user['name']}").add_to(mapa)
    print('\nwykonano')
    mapa.save(f'mapa19.html')


def get_coords(city: str) -> list[float, float]:
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_htlm = BeautifulSoup(response.text, 'html.parser')

    res_h_lat = response_htlm.select('.latitude')[1].text  # . bo class
    res_h_lat = float(res_h_lat.replace(',', '.'))

    res_h_lon = response_htlm.select('.longitude')[1].text  # . bo class
    res_h_lon = float(res_h_lon.replace(',', '.'))

    return [res_h_lat, res_h_lon]



### SQL

class User(Base):
    __tablename__ = 'tab_users'

    id = Column(Integer(), primary_key=True)
    posts = Column(Integer(), nullable=True)
    name = Column(String(100), nullable=True)
    nick = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)



def dodanie_tabeli(db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()

    Base = sqlalchemy.orm.declarative_base()

    class User(Base):
        __tablename__ = 'tab_users'

        id = Column(Integer(), primary_key=True)
        posts = Column(Integer(), nullable=True)
        name = Column(String(100), nullable=True)
        nick = Column(String(100), nullable=True)
        city = Column(String(100), nullable=True)
        location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

    Base.metadata.create_all(engine)

    aa_list: list = []

    for user in users_list:
        xy = get_coords(user['city'])
        aa_list.append(
            User(
                name=user['name'],
                posts=user['posts'],
                nick=user['nick'],
                city=user['city'],
                location=f'POINT({xy[1]} {xy[0]})'
            )
        )
    session.add_all(aa_list)
    session.commit()


def add_sql(listaa, db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()

    name = input('Podaj imię: ')
    nick = input('Podaj nick: ')
    post = int(input('liczba wstawionych postow: '))
    place = input('Podaj miejsce: ')
    listaa.append({"name": name, "nick": nick, "posts": post, 'city': place})
    loc = get_coords(place)
    sql_query = sqlalchemy.text(f"INSERT INTO public.tab_users(name, nick, city, posts, geom) VALUES ('{name}', '{nick}', '{place}', '{post}', 'POINT({loc[1]} {loc[0]})');")

    connection.execute(sql_query)
    connection.commit()


def remove_sql(list, db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()

    tp_list = []
    name = input('kogo chcesz usunac :')
    for user in list:
        if user['name'] == name:
            tp_list.append(user)
    print('znaleziono nastepujacych uzytkownikow:')
    print('0 usuniecie wszystkich')
    for numer, user_to_be_removed in enumerate(tp_list):
        print(numer + 1, user_to_be_removed)
    numer = int(input('wybierz uzytkownika do usuniecia: '))
    if numer == 0:
        for user in tp_list:
            list.remove(user)
            print(user)
            print(type(user))
            sql_query = sqlalchemy.text(f"DELETE FROM public.list_of_users WHERE name = '{user['name']}';")
    else:
        aa = tp_list[numer - 1]
        list.remove(aa)
        print(type(aa))
        print(aa['city'])
        sql_query = sqlalchemy.text(f"DELETE FROM public.list_of_users WHERE nick = '{aa['nick']}';")

    connection.execute(sql_query)
    connection.commit()


def updage_sql(list, db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()

    nick_of_user = input('Podaj nick użytkownika do modyfikacji ')
    print(f'Wpisano {nick_of_user}')
    for user in list:
        if user['nick'] == nick_of_user:
            print('znaleziono')
            new_name = input('Podaj nowe imię użytkownika ')
            user['name'] = new_name
            new_nick = input('Podaj nowy nick użytkownika ')
            user['nick'] = new_nick
            new_posts = input('Podaj nową ilość postów ')
            user['posts'] = new_posts
            new_citi = input('Podaj nowe miejsce spotkania ')
            user['city'] = new_citi
            loc = get_coords(new_citi)

    sql_query = sqlalchemy.text(
        f"UPDATE public.list_of_users SET name='{new_name}', posts='{new_posts}', nick='{new_nick}', city='{new_citi}', geom='POINT({loc[1]} {loc[0]})' WHERE nick='{nick_of_user}';")

    connection.execute(sql_query)
    connection.commit()


def zamkniecie(db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()

    sql_query = sqlalchemy.text(f"DELETE FROM public.list_of_users WHERE name != 'AAAA';")

    connection.execute(sql_query)
    connection.commit()


def tworzenie(db_params):
    engine = sqlalchemy.create_engine(db_params)
    Base = sqlalchemy.orm.declarative_base()

    class User(Base):
        __tablename__ = 'tab_users'

        id = Column(Integer(), primary_key=True)
        posts = Column(Integer(), nullable=True)
        name = Column(String(100), nullable=True)
        nick = Column(String(100), nullable=True)
        city = Column(String(100), nullable=True)
        location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

    Base.metadata.create_all(engine)


def show_sql(db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    users_form_db = session.query(User).all()

    for user in users_form_db:
        print(f"Użytkownik {user.name} znajdujacy sie w  {user.city} stworzyl tabele z  {user.posts} wiadomosciami")


def zmiana_tabeli(db_params):
    engine = sqlalchemy.create_engine(db_params)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()

    working_list = []
    users_form_db = session.query(User).all()

    for user in users_form_db:
        name = user.name
        nick = user.nick
        post = user.posts
        city = user.city
        working_list.append({"name": name, "nick": nick, "posts": post, 'city': city})

    return working_list
