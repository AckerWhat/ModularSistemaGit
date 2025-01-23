from archivo import Archivo
from commit import Commit
from rama import Rama

class Repositorio:
    def __init__(self):
        self.ramas = {}
        self.archivos = []
        self.rama_actual = None

        # Crear la rama principal
        rama_principal = Rama("main")
        self.ramas["main"] = rama_principal
        self.rama_actual = rama_principal

    def hacer_commit(self, mensaje):
        nuevo_commit = Commit(mensaje, self.archivos, self.rama_actual.commit_reciente)
        self.rama_actual.commit_reciente = nuevo_commit
        print(f"Commit realizado: {nuevo_commit}")

    def crear_rama(self, nombre):
        if nombre in self.ramas:
            raise ValueError(f"La rama {nombre} ya existe.")
        nueva_rama = Rama(nombre, self.rama_actual.commit_reciente)
        self.ramas[nombre] = nueva_rama
        print(f"Rama {nombre} creada.")

    def cambiar_rama(self, nombre):
        if nombre not in self.ramas:
            print(f"La rama {nombre} no existe.")
            return
        self.rama_actual = self.ramas[nombre]
        print(f"Cambiado a la rama {nombre}.")

    def merge(self, nombre_rama_origen):
        if nombre_rama_origen not in self.ramas:
            print(f"La rama {nombre_rama_origen} no existe.")
            return

        rama_origen = self.ramas[nombre_rama_origen]
        if not rama_origen.commit_reciente:
            print(f"La rama {nombre_rama_origen} no tiene commits.")
            return

        self.rama_actual.commit_reciente = rama_origen.commit_reciente
        print(f"Rama {nombre_rama_origen} fusionada en {self.rama_actual.nombre}.")

    def mostrar_historial(self):
        print(f"Historial de commits para la rama {self.rama_actual.nombre}:")
        commit = self.rama_actual.commit_reciente
        while commit:
            print(commit)
            commit = commit.anterior

    def deshacer_commit(self):
        if not self.rama_actual.commit_reciente:
            print("No hay commits para deshacer.")
            return
        self.rama_actual.commit_reciente = self.rama_actual.commit_reciente.anterior
        print("Último commit deshecho.")
        
    def listar_ramas(self):
        print("Ramas disponibles:")
        for nombre, rama in self.ramas.items():
            print(f"  - {nombre} (último commit: {rama.commit_reciente})")

