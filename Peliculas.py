class Pelicula:
    def __init__(self, titulo):
        self._titulo = titulo
        self._fecha_lanzamiento = None
        self._genero = None
        self._sinopsis = None
        self._director = None
        self._reparto = None

    def __str__(self):
        return f"Título: {self._titulo}\n" \
               f"Fecha de lanzamiento: {self._fecha_lanzamiento}\n" \
               f"Género: {self._genero}\n" \
               f"Sinopsis: {self._sinopsis}\n" \
               f"Director: {self._director}\n" \
               f"Reparto: {self._reparto}\n" \
               f"Puntuación: {self._puntuacion}"


    # Getters
    def get_titulo(self):
        return self._titulo

    def get_fecha_lanzamiento(self):
        return self._fecha_lanzamiento

    def get_genero(self):
        return self._genero

    def get_sinopsis(self):
        return self._sinopsis

    def get_director(self):
        return self._director

    def get_reparto(self):
        return self._reparto

    def get_puntuacion(self):
        return self._puntuacion

    # Setters
    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_fecha_lanzamiento(self, fecha_lanzamiento):
        self._fecha_lanzamiento = fecha_lanzamiento

    def set_genero(self, genero):
        self._genero = genero

    def set_sinopsis(self, sinopsis):
        self._sinopsis = sinopsis

    def set_director(self, director):
        self._director = director

    def set_reparto(self, reparto):
        self._reparto = reparto

    def set_puntuacion(self, puntuacion):
        self._puntuacion = puntuacion