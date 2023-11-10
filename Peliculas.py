class Pelicula :
    def __init__(self, titulo):
        self._titulo = titulo
        self.puntuacion = None
        self._fecha_lanzamiento = None
        self._genero = None
        self._sinopsis = None
        self._director = None
        self._reparto = None

    @property
    def titulo(self):
        return self._titulo

    @property
    def lanzamiento(self):
        return self._fecha_lanzamiento

    @property
    def genero(self):
        return self._genero

    @property
    def sinopsis(self):
        return self._sinopsis

    @property
    def director(self):
        return self._director

    @property
    def reparto(self):
        return self._reparto

    @property
    def puntuacion(self):
        return self._puntuacion

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, puntuacion):
        self._puntuacion = puntuacion

    # Setters
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    @lanzamiento.setter
    def lanzamiento(self, fecha_lanzamiento):
        self._fecha_lanzamiento = fecha_lanzamiento
    @genero.setter
    def genero(self, genero):
        self._genero = genero
    @sinopsis.setter
    def sinopsis(self, sinopsis):
        self._sinopsis = sinopsis
    @director.setter
    def director(self, director):
        self._director = director
    @reparto.setter
    def reparto(self, reparto):
        self._reparto = reparto
    @puntuacion.setter
    def puntuacion(self, puntuacion):
        self._puntuacion = puntuacion

    def __str__(self):
        return f"Título: {self._titulo}\n" \
               f"Fecha de lanzamiento: {self._fecha_lanzamiento}\n" \
               f"Género: {self._genero}\n" \
               f"Sinopsis: {self._sinopsis}\n" \
               f"Director: {self._director}\n" \
               f"Reparto: {self._reparto}\n" \
               f"Puntuación: {self._puntuacion}"


