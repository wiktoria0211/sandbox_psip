from bs4 import BeautifulSoup
import requests
import re
import  folium


nazwy_miejscowosci = ['Gdańsk', 'Warszawa', 'Wrocław']
def get_coordinates_of(city:str)->list[float,float]:

    #pobranie strony internetowej

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    #pobranie wspolrzednych z tresci strony internetowej
    response_html_latitude = response_html.select('.latitude')[1].text
    response_html_latitude = float(response_html_latitude.replace(',', '.'))

    response_html_longitude = response_html.select('.longitude')[1].text
    response_html_longitude = float(response_html_longitude.replace(',', '.'))
    return [response_html_latitude, response_html_longitude]
#for item in nazwy_miejscowosci:
    #print(get_coordinates_of(item))

#zwrocic mape z pineska odnszaca sie do nazwy uzytkownika podanego z klawiatury
#zwrocic mape z wszytskimi uzytkownikami z danej listy(znajomymi)
### rysowanie mapy
city= get_coordinates_of(city='Zamość')
map = folium.Map(
    location=[52.3, 21.0], #gdzie mapa ma byc wycentrowana
    tiles="OpenStreetMap",
    zoom_start=7,
    )
for item in nazwy_miejscowosci:
    folium.Marker(
        location=get_coordinates_of(city=item),
        popup='GEOINFORMATYKA RZĄDZI OU YEEEEAH!'
    ).add_to(map)
map.save('mapka.html')