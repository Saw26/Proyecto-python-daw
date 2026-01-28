from clases import *

import json
import logging


logging.basicConfig(
    level=logging.DEBUG,
    )
# esto es para cambiar la configuración mínima del loggin porque si no ni info ni debug se muestran Pedro.


def exportar_a_json():
    try:
        with open("tareas.txt","r",encoding="utf-8") as fichero:
            lineas = fichero.readlines()
            
        tareas =[]
        for linea in lineas:
            partes = linea.strip().split(";")
            tareas.append({
                "id": partes[0],
                "nombre": partes[1],
                "descripcion": partes[2],
                "prioridad": partes[3],
                "categoria": partes[4]
            })
            
        with open("tareas.json", "w", encoding="utf-8") as fichero:
            json.dump(tareas,fichero,indent=4)
        
        logging.info("Exportado a tareas.json")
        logging.debug("Hemos creado la tarea por partes y la hemos añadido a su ficherito correspondiente")
    except FileNotFoundError:
        logging.error("No existe el fichero de Tareas.txt!")
        
        
def importar_json():
    try:
        with open("tareas.json","r",encoding="utf-8") as fichero:
            tareas = json.load(fichero)
        
        with open("tareas.txt","w",encoding="utf-8") as fichero:
            for tarea in tareas:
                linea = f"{tarea['id']};{tarea['nombre']};{tarea['descripcion']};{tarea['prioridad']};{tarea['categoria']}\n"
                fichero.write(linea)
        
        logging.info("Importado desde tareas.json!")
    except FileNotFoundError:
        logging.error("No existe el fichero de Tareas.json!")
        
        
    
def añadir_tareas():
    """
    Esta función le pide datos al usuario y añade una nueva tarea al fichero que tenemos de tareas.txt (y he añadido un control de errores)
    """
    try:
        id = int(input("ID de la tarea (número): "))
    except ValueError:
        logging.error("El ID debe ser un número entero ")
        return # para que slaga del programa si no es un número

    nombre = input("Nombre de la tarea: ")
    if nombre == "":
        logging.warning("El nombre no puede estar vacío ")
        return 

    descripcion = input("Descripción de la tarea: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    categoria = input("Categoría (personal/laboral/social): ")
    
    # Una vez que le metemos los datos (la id, el nombre...) vamos a comprobar si todo está en su sitio y lo metemos al fichero

    if categoria != "personal" and categoria != "laboral" and categoria != "social":
        logging.warning("Categoría inválida. Debe ser 'personal', 'laboral' o 'social' ")

    tarea = Tarea(id, nombre, descripcion, prioridad, categoria)
    tareaFinal = f"{tarea.id};{tarea.nombre};{tarea.descripcion};{tarea.prioridad};{tarea.categoria}\n"

    with open("tareas.txt", "a", encoding="utf-8") as fichero:
    #aquí abro el archivo en formato append con su codificación para evitar rollos de tildes, la ñ.., escribo sobre el y se cierra solo (por el with open) (y así con las demás funciones que haré)
        fichero.write(tareaFinal)
    logging.info("Tarea añadida correctamente y guardada en tareas.txt")


def listar_tareas():
    """
    Esta función muestra todas las tareas guardadas en el fichero tareas.txt (con su control de errores como pides Pedro)
    """
    tareas = cargar_tareas()
    if not tareas:
        logging.warning("No hay tareas guardadas.")
    else:
        print("\n-----LISTA DE TAREAS -----")
        for tarea in tareas:
            tarea.mostrar_info()
        print("------------------------------")
        
        
        # aquí llamamos al fichero con todo lo que tenga, lee cada línea (y las separa claro) y si no encuentra nada le he metido un control de errores
        
def buscar_tarea():
    """
    Esta función busca una tarea en el fichero de tareas.txt (que le pasamos desde la función cargar_tareas de su propio objeto)
    """
    try:
        id_buscar = int(input("ID de la tarea: "))
    except ValueError:
        logging.error("El ID debe ser un número entero")
        return

    tareas = cargar_tareas()
    encontrado = False
    for tarea in tareas:
        if str(tarea.id) == str(id_buscar):
            encontrado = True
            print("\n--- TAREA ENCONTRADA!! ---")
            tarea.mostrar_info()
            print("------------------------\n")
    if not encontrado:
        logging.warning("No se encuentra la tarea con ese ID")



def eliminar_tareas():
    """
    Esta función elimina una tarea (por ID) del fichero tareas.txt (misma jugada, tirando del objeto)
    """
    id_borrar = input("Introduce el ID de la tarea a eliminar: ")
    
    tareas = cargar_tareas()
    with open("tareas.txt", "w", encoding="utf-8") as fichero:
        for tarea in tareas:
            if str(tarea.id) !=str(id_borrar):
                linea = f"{tarea.id};{tarea.nombre};{tarea.descripcion};{tarea.prioridad};{tarea.categoria}\n"
                fichero.write(linea)
                
    logging.info("Tarea eliminada correctamente")


def modificar_tareas():
    """
    Esta función modifica una tarea (por la ID que le metamos) del fichero tareas.txt (misma jugada, tirando del objeto y sus métodos)
    """
    id_modificar = input("Introduce el ID de la tarea a modificar: ")

    tareas = cargar_tareas() 
    encontrado = False

    for tarea in tareas:
        if str(tarea.id) == str(id_modificar):
            encontrado = True
            logging.info("Datos actuales de la tarea:")
            logging.info(f"ID: {tarea.id}, Nombre: {tarea.nombre}, Descripción: {tarea.descripcion}, Prioridad: {tarea.prioridad}, Categoría: {tarea.categoria}")
            logging.info("¿Qué quieres modificar?")
            logging.info("1. Nombre")
            logging.info("2. Descripción")
            logging.info("3. Prioridad")
            logging.info("4. Categoría")
            opcion = input("Elige una opción (1-4): ")

            if opcion == "1":
                tarea.nombre = input("Nuevo nombre: ")
            elif opcion == "2":
                tarea.descripcion = input("Nueva descripción: ")
            elif opcion == "3":
                tarea.prioridad = input("Nueva prioridad: ")
            elif opcion == "4":
                tarea.categoria = input("Nueva categoría: ")

    # Ahora reescribo el fichero con todas las tareas (modificada incluida)
    with open("tareas.txt", "w", encoding="utf-8") as fichero:
        for tarea in tareas:
            linea = f"{tarea.id};{tarea.nombre};{tarea.descripcion};{tarea.prioridad};{tarea.categoria}\n"
            fichero.write(linea)

    if encontrado:
        logging.info("Tarea modificada correctamente ")
    else:
        logging.warning("No se encontró ninguna tarea con ese ID ")





def menu():
    # Muestra el menú para que el usuario decida qué hacer (seleccionando un número)
    respuesta = int(input("¿qué quieres hacer?\n"
                          "1. Añadir tarea\n"
                          "2. Buscar una tarea\n"
                          "3. Listar mis tareas\n"
                          "4. Modificar una tarea\n"
                          "5. borrar una tarea\n"
                          "6.Exportar a JSON\n"
                          "7.Importar desde JSON\n"
                          "8.salir del programa\n"))
    return respuesta
            
            
            
            


    
