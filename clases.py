import logging

class Tarea:
    def __init__(self, id, nombre, descripcion, prioridad, categoria):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.categoria = categoria

    def mostrar_info(self):
        print("\n--- TAREA ---")
        logging.debug(f"ID: {self.id}")
        logging.debug(f"Nombre: {self.nombre}")
        logging.debug(f"Descripción: {self.descripcion}")
        logging.debug(f"Prioridad: {self.prioridad}")
        logging.debug(f"Categoría: {self.categoria}")
        print("------------------------\n")

def cargar_tareas():
    tareas = []
    try:
        with open("tareas.txt", "r", encoding="utf-8") as fichero:
            for linea in fichero:
                partes = linea.strip().split(";")
                tareas.append(Tarea(partes[0], partes[1], partes[2], partes[3], partes[4]))
    except FileNotFoundError:
        logging.error("No existe el archivo de tareas")
    return tareas

