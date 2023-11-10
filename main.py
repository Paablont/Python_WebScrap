from Peliculas import Pelicula
import bs4
import requests
import datetime
import sys
import os
import json

def imprimirOpcionJSON():
    print("Que quieres hacer con los datos? (1. Mostrarlos en consola, 0. Guardarlos en un JSON)")

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
                peli = Pelicula(titulo)
                peli.puntuacion = puntuacionNumber
                listaPelis.append(peli)
        listaPelis = sorted(listaPelis, key=lambda pelicula: pelicula.puntuacion, reverse=True)


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
        director = a.select_one('.top-movie .movie-card .mc-right .mc-right-content .mc-data .director .credits .nb a').text
        reparto = a.select_one('.top-movie .movie-card .mc-right .mc-right-content .mc-data .cast .credits .nb a').text

        peli = Pelicula(titulo)
        peli.lanzamiento = fechaEstreno
        peli.genero = genero
        peli.sinopsis =sinopsis
        peli.director = director
        peli.reparto = reparto

        listaPelis.append(peli)
    if ordenarPor == 1: #Ordena segun genero
        listaPelis = sorted(listaPelis, key=lambda pelicula: pelicula.genero)
    else:#Ordena segun fecha
        listaPelis = sorted(listaPelis, key=lambda pelicula: pelicula.lanzamiento,reverse=True)

    return listaPelis

def rankingPeliculas(urlRanking):
    # lista de pelis para despues ordenarlas
    listaRanking = []
    # Solicitud a la pagina y soup
    result = requests.get(urlRanking)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    # Saco las pelis de la pagina
    rankingPelis = soup.select('.z-top-movies ul')
    for a in rankingPelis:
        # Saco el titulo
        titulo = a.select_one('li .content .movie-card .mc-info-container .mc-title a').text
        puntuacion = a.select_one('.data .avg-rating').text
        if puntuacion != '--':
            puntuacionNumber = float(puntuacion.replace(",", "."))

        peli = Pelicula(titulo)
        peli.puntuacion = puntuacionNumber

        listaRanking.append(peli)

    return listaRanking

# Menu app:
fecha = datetime.date.today()
meses_espanol = {
    'January': 'enero',
    'February': 'febrero',
    'March': 'marzo',
    'April': 'abril',
    'May': 'mayo',
    'June': 'junio',
    'July': 'julio',
    'August': 'agosto',
    'September': 'septiembre',
    'October': 'octubre',
    'November': 'noviembre',
    'December': 'diciembre'
}
nombre_mes = meses_espanol[fecha.strftime('%B')]
fechaActual = fecha.strftime(f'%d de {nombre_mes} de %Y')
urlDiarias = "https://www.filmaffinity.com/es/rdcat.php?id=new_th_es"
urlProxEstrenos = "https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es"
urlRanking = "https://www.filmaffinity.com/es/ranking.php?rn=ranking_2023_topmovies"

salir = False


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
            imprimirOpcionJSON()
            opcionJsonString = input("Elige una opción: ")
            opcionJson = int(opcionJsonString)

            if opcionJson == 1:
                for a in listaPelisDiarias:
                    print("---------------------------------------")
                    print(f"Titulo: {a.titulo}")
                    print(f"Puntuación: {a.puntuacion}")
                    print("---------------------------------------")
            else:
                fichero = open("pelisDiarias.json", "a")
                dicPelisDiarias = {"PeliculasDIARIAS": {a.titulo: {"Titulo": a.titulo, "Puntuación": a.puntuacion} for a in
                                                 listaPelisDiarias}}
                json.dump(dicPelisDiarias, fichero, indent=2)
                fichero.close()
                print("Datos guardados en pelisDiarias.json")


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
                imprimirOpcionJSON()
                opcionJsonString = input("Elige una opción: ")
                opcionJson = int(opcionJsonString)
                if opcionJson == 1:
                    for a in listaProxEstrenos:
                        print("---------------------------------------")
                        print(f"Titulo: {a.titulo}")
                        print(f"Fecha: {a.lanzamiento}")
                        print(f"Genero: {a.genero}")
                        print(f"Sinopsis: {a.sinopsis}")
                        print(f"Director: {a.director}")
                        print(f"Reparto: {a.reparto}")
                        print("---------------------------------------")
                else:
                    fichero = open("proximosEstrenos.json", "a")
                    dicProxEstrenos = {
                        "ProximosESTRENOS": {a.titulo: {"Titulo": a.titulo, "Fecha": a.lanzamiento, "Genero": a.genero,
                                                 "Sinopsis": a.sinopsis, "Director": a.director, "Reparto": a.reparto}
                                      for a in listaProxEstrenos}}
                    json.dump(dicProxEstrenos, fichero, indent=2)
                    fichero.close()
                    print("Datos guardados en proximosEstrenos.json")
        input("Pulsa una tecla para volver al menu")
        os.system('cls')

    elif opcion == 3:
        listaRanking = rankingPeliculas(urlRanking)
        if not listaRanking:
            print("Esta vacia")
        else:
            imprimirOpcionJSON()
            opcionJsonString = input("Elige una opción: ")
            opcionJson = int(opcionJsonString)
            if opcionJson == 1:
                for a in listaRanking:
                    print("---------------------------------------")
                    print(f"Titulo: {a.titulo}")
                    print(f"Puntuación: {a.puntuacion}")
                    print("---------------------------------------")
            else:
                fichero = open("rankingAnual.json", "a")
                dicRanking = {
                    "rankingANUAL": {a.titulo: {"Titulo": a.titulo, "Puntuación": a.puntuacion} for a in listaRanking}}
                json.dump(dicRanking, fichero, indent=2)
                fichero.close()
                print("Datos guardados en rankingAnual.json")
        input("Pulsa una tecla para volver al menu")
        os.system('cls')

    elif opcion == 4:
        print("Hasta pronto")
        sys.exit()
    else:
        print("Opcion invalida")
