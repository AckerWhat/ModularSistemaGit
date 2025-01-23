class Commit:
    contador_id = 0  # Contador global para asignar IDs únicos

    def __init__(self, mensaje, archivos, anterior=None):
        self.id = Commit.contador_id
        Commit.contador_id += 1
        self.mensaje = mensaje
        self.archivos = archivos[:]  # Copia de los archivos
        self.anterior = anterior

    def __str__(self):
        return f"Commit {self.id}: {self.mensaje}"