from Peliculas import Pelicula
import bs4
import requests
import datetime
import sys
import os


def imprimirMenu():
    print("******************************")
    print("1. Peliculas diarias")
    print("2. Proximos lanzamientos")
    print("3. Ranking de mejores peliculas 2023")
    print("4. Salir de la aplicación")
    print("******************************")


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
                peli = Pelicula(titulo, puntuacionNumber)
                listaPelis.append(peli)
        listaPelis = sorted(listaPelis, key=lambda pelicula: pelicula.get_puntuacion())

    return listaPelis


def proximosEstrenos(urlProxEstrenos,ordenarPor):
    # lista de pelis para despues ordenarlas
    listaPelis = []
    # Solicitud a la pagina y soup
    result = requests.get(urlProxEstrenos)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    # Saco las pelis de la pagina
    peliculas = soup.select('#main-wrapper-rdcat')
    for a in peliculas:
        # Saco el titulo
        titulo = a.select_one('.top-movie .movie-card .mc-right h3 a').text
        fechaEstreno = a.select_one('.rdate-cat').text
        genero = a.select_one('.top-movie .movie-card .mc-right .mc-right-content .mc-data .synop .genre').text
        sinopsis = a.select_one('.top-movie .movie-card .mc-right .mc-right-content .mc-data .synop .synop-text').text
        director = a.select_one(
            '.top-movie .movie-card .mc-right .mc-right-content .mc-data .director .credits .nb a').text
        reparto = a.select_one('.top-movie .movie-card .mc-right .mc-right-content .mc-data .cast .credits .nb a').text

        peli = Pelicula(titulo, fechaEstreno, genero, sinopsis, director, reparto)
        listaPelis.append(peli)
    if ordenarPor == 1: #Ordena segun genero
        listaPelis = sorted(listaPelis, key=lambda pelicula: pelicula.get_genero())
    else:#Ordena segun fecha
        listaPelis = sorted(listaPelis, key=lambda pelicula: pelicula.get_fecha_lanzamiento(),reverse=True)

    return listaPelis


# Menu app:
fecha = datetime.date.today()
fechaActual = fecha.strftime('%d de %m de %Y')
urlDiarias = "https://www.filmaffinity.com/es/rdcat.php?id=new_th_es"
urlProxEstrenos = "https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es"
salir = False

# listas
listaPelisDiarias = []
listaProxEstrenos = []

while not salir:
    imprimirMenu()
    opcionString = input("Elige una opcion: ")
    opcion = int(opcionString)

    if opcion == 1:

        print(f"Peliculas a {fechaActual}")
        listaPelisDiarias = peliculasDiarias(urlDiarias, fechaActual)
        # Si la lista esta vacia no hay pelis nuevas
        if not listaPelisDiarias:
            print("Hoy no hay ninguna película nueva")
        else:
            for a in listaPelisDiarias:
                print(f"Titulo: {a.get_titulo()}, Puntuación: {a.get_puntuacion()}")

        input("Pulsa una tecla para volver al menu")
        os.system('cls')

    elif opcion == 2:

        ordenar = input("Como quieres ordenar las peliculas? (por fecha: 0, por género: 1): ")
        ordenarNumber = int(ordenar)
        if ordenarNumber != 0 and ordenarNumber != 1:
            print("La opcion de ordenar que has elegido no es correcta")
        else:
            listaProxEstrenos = proximosEstrenos(urlProxEstrenos,ordenarNumber)
            if not listaProxEstrenos:
                print("Esta vacia")
            else:
                for a in listaProxEstrenos:
                    print("---------------------------------------")
                    print(f"Titulo: {a.get_titulo()}")
                    print(f"Fecha: {a.get_fecha_lanzamiento()}")
                    print(f"Genero: {a.get_genero()}")
                    print(f"Sinopsis: {a.get_sinopsis()}")
                    print(f"Director: {a.get_director()}")
                    print(f"Reparto: {a.get_reparto()}")
                    print("---------------------------------------")

        input("Pulsa una tecla para volver al menu")
        os.system('cls')
    elif opcion == 3:
        print("Opcion 3")

        input("Pulsa una tecla para volver al menu")
        os.system('cls')
    elif opcion == 4:
        print("Hasta pronto")
        sys.exit()
    else:
        print("Opcion invalida")
