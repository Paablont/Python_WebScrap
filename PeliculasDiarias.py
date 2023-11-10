import bs4
import requests
import datetime
from Peliculas import Pelicula


fecha = datetime.date.today()
fechaActual = fecha.strftime('%d de %m de %Y')
urlDiarias = "https://www.filmaffinity.com/es/rdcat.php?id=new_th_es"

def peliculasDiarias(urlDiarias, fechaActual):
    # lista de pelis para despues ordenarlas
    listaPelis = []
    # Solicitud a la pagina y soup
    result = requests.get(urlDiarias)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    # Saco la fecha de las pelis (para despues compararla con la actual)
    fechaPelis = soup.find('div', class_='rdate-cat rdate-cat-first').text.strip()

    # Comprobamos fechas
    if (fechaPelis == fechaActual):

        tituloPeli = soup.select('.movie-card .mc-right')
        for a in tituloPeli:
            # saco el titulo
            titulo = a.select_one('h3 a').text
            # saco la puntuacion (la paso a float porque si no no la puedo ordenar)
            puntuacion = a.select_one('.mc-right-content .stats .avg-rating').text
            if puntuacion != '--':
                puntuacionNumber = float(puntuacion.replace(",", "."))
                peli = Pelicula(titulo)
                peli.set_puntuacion(puntuacionNumber)
                listaPelis.append(peli)
        listaPelis = sorted(listaPelis, key=lambda pelicula: pelicula.get_puntuacion())

    return listaPelis