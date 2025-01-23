class Rama:
    def __init__(self, nombre, commit_inicial=None):
        self.nombre = nombre
        self.commit_reciente = commit_inicial

    def __str__(self):
        return f"Rama {self.nombre}, último commit: {self.commit_reciente}"