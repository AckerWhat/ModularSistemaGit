class Archivo:
    def __init__(self, nombre, contenido=""):
        self.nombre = nombre
        self.contenido = contenido

    def __str__(self):
        return f"{self.nombre}: {self.contenido}"