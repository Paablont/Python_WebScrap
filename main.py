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

def peliculasDiarias(urlDiarias,fechaActual):
    #lista de pelis para despues ordenarlas
    listaPelis = []
    #Solicitud a la pagina y soup
    result = requests.get(urlDiarias)
    soup = bs4.BeautifulSoup(result.text,'lxml')
    #Saco la fecha de las pelis (para despues compararla con la actual)
    fechaPelis = soup.find('div',class_='rdate-cat rdate-cat-first').text.strip()

    #Comprobamos fechas
    if(fechaPelis == fechaActual):

        tituloPeli = soup.select('.movie-card .mc-right')
        for a in tituloPeli:
            #saco el titulo
            titulo = a.select_one('h3 a').text
            #saco la puntuacion (la paso a float porque si no no la puedo ordenar)
            puntuacion = a.select_one('.mc-right-content .stats .avg-rating').text
            if puntuacion != '--':
                puntuacionNumber = float(puntuacion.replace(",","."))
                peli = Pelicula(titulo, puntuacionNumber)
                listaPelis.append(peli)

    return listaPelis


#Menu app:
fecha = datetime.date.today()
fechaActual = fecha.strftime('%d de %m de %Y')
urlDiarias = "https://www.filmaffinity.com/es/rdcat.php?id=new_th_es"
salir = False
while not salir:
    imprimirMenu()
    opcionString = input("Elige una opcion: ")
    opcion = int(opcionString)
    if opcion == 1:
        print(f"Peliculas a {fechaActual}")
        pelisDiarias = peliculasDiarias(urlDiarias, fechaActual)
        # Si la lista esta vacia no hay pelis nuevas
        if not pelisDiarias:
            print("Hoy no hay ninguna película nueva")
        else:
            for a in pelisDiarias:
                print(f"Titulo: {a.get_titulo()}, Puntuación: {a.get_puntuacion()}")

        input("Pulsa una tecla para volver al menu")
        os.system('cls')

    elif opcion == 2:
        print("Opcion 2")

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




