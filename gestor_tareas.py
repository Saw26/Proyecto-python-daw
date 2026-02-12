from clases import *
from datetime import date
from datetime import datetime

import json
import logging


logging.basicConfig(
    level=logging.DEBUG,
    )
# esto es para cambiar la configuración mínima del loggin porque si no ni info ni debug se muestran Pedro.



def exportar_a_json():
    """
    Esta función coge el objeto tarea (que a su vez viene de tareas.txt) y lo convierte a una lista de objetos en JSON
    EXAMEN: en lugar de llamar directamente al fichero tareas.txt y recorrerlo y trabajar sobre el, trabajo con el objeto tarea (con sus 2 claves)
    """
    try:
        tareas = cargar_tareas()
        arrayTareas =[]
        for tarea in tareas:
            arrayTareas.append({
                "items":{
                "id": tarea.id,
                "nombre": tarea.nombre,
                "descripcion": tarea.descripcion,
                "prioridad": tarea.prioridad,
                "categoria": tarea.categoria,
                "Fecha": tarea.fecha
            },
                "fecha_ultimo_guardado": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                })
            
        with open("tareas.json", "w", encoding="utf-8") as fichero:
            json.dump(arrayTareas,fichero,indent=4)
        
        logging.info("Exportado a tareas.json")
        logging.debug("Hemos creado la tarea por partes y la hemos añadido a su ficherito correspondiente")
    except FileNotFoundError:
        logging.error("No existe el fichero de Tareas.txt!")
        
        
def importar_json():
    """
    Esta función funciona justo al revés que exportar_a_json, coge el ficherito tareas.json, lo reconvierte al formato de tareas.txt y lo sobreescribe.
    """
    
    try:
        #abro el fichero para leer el json
        with open("tareas.json","r",encoding="utf-8") as fichero:
           datos = json.loads(fichero)
           
        tareas = []
        #convierto cada dato en un objeto
        for tarea in datos:
            tarea = Tarea(
                tarea["id"],
                tarea["nombre"],
                tarea["descripcion"],
                tarea["prioridad"],
                tarea["categoria"]
            )
            tareas.append(tarea)
        #ahora abro el fichero de tareas.txt para sobreescribirlo con las de json

        with open("tareas.txt","w",encoding="utf-8") as fichero:
            for tarea in tareas:
                linea = f"{tarea.id};{tarea.nombre};{tarea.descripcion};{tarea.prioridad};{tarea.categoria}\n"
                fichero.write(linea)
        logging.info("Tareas importadas desde json a txt! ")
        
    except FileNotFoundError:
        logging.error("No existe el fichero Tareas.json..")
        
        
    
def añadir_tareas():
    """
    Esta función le pide datos al usuario y añade una nueva tarea al fichero tareas.txt.
    Ahora pregunta si la tarea es NORMAL o COMPLETA (herencia).
    """

    try:
        id = int(input("ID de la tarea (número): "))
    except ValueError:
        logging.error("El ID debe ser un número entero ")
        return

    nombre = input("Nombre de la tarea: ")
    if nombre == "":
        logging.warning("El nombre no puede estar vacío ")
        return 

    descripcion = input("Descripción de la tarea: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    categoria = input("Categoría (personal/laboral/social): ")

    tipo = input("¿Qué tipo de tarea quieres crear? (normal/completa): ").strip().lower()

    if tipo == "normal":
        tarea = Tarea(id, nombre, descripcion, prioridad, categoria)
        tareaFinal = f"{tarea.id};{tarea.nombre};{tarea.descripcion};{tarea.prioridad};{tarea.categoria}\n"
    elif tipo == "completa":
        fecha = date.today().isoformat()
        tarea = TareaCompleta(id, nombre, descripcion, prioridad, categoria, fecha)
        tareaFinal = f"{tarea.id};{tarea.nombre};{tarea.descripcion};{tarea.prioridad};{tarea.categoria};{tarea.fecha}\n"
    else:
        logging.error("Tipo inválido. Debe ser 'normal' o 'completa'.")
        return
    
    with open("tareas.txt", "a", encoding="utf-8") as fichero:
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
        
        
    
        
def buscar_tarea():
    """
    Esta función busca una tarea en el fichero de tareas.txt (que le pasamos desde la función cargar_tareas de su propio objeto)
    EXAMEN: MODIFICO LA FUNCIÓN PARA QUE ME BUSQUE DENTRO DE CUALQUIER CRITERIO UNA PALABRA CLAVE)
    """
    # MUY IMPORTANTE, a la hora de buscar la tarea como he puesto el .lower HAY que escribir la palabra en mayuscula
    # por ejemplo yo tengo 2 tareas que llevan la palabra "Aprobar",
    #  si escribes "Aprobar" NO te las sacará, hay que escribir "aprobar"
    palabra = input("Introduce una palabra ( o ID) para buscar (clave): ")
    tareas = cargar_tareas()
    encontradas = []
    for tarea in tareas:
        id = str(tarea.id).lower()
        nombre = tarea.nombre.lower()
        descripcion = tarea.descripcion.lower()
        prioridad = tarea.prioridad.lower()
        categoria = tarea.categoria.lower()
        fecha = tarea.fecha
        
        if (palabra in id or
            palabra in nombre or
            palabra in descripcion or
            palabra in prioridad or
            palabra in categoria or
            palabra in fecha):
            encontradas.append(tarea)
            
    if not encontradas:
        logging.warning("No se ha encontrado la tarea con esa palabra.." )
        return
    else:
        logging.info("LISTA DE TAREAS CON BÚSQUEDA: ")
        for tarea in encontradas:
            tarea.mostrar_info()
            logging.info("-------------------------")



def buscar_categoria():
    """
    EXAMEN: vamos a modificar la función para que podamos buscar tareas de una categoria concreta
    (HE HECHO ESTA FUNCIÓN POR SI LA DE ARRIBA NO TE SIRVE COMO BÚSQUEDA)
    """
    categoria = input("Escribe la categoría que quieras (laboral, personal o social) ")
    tareas = cargar_tareas()
    encontradas = []
    for tarea in tareas:
        if tarea.categoria == categoria.lower():
            encontradas.append(tarea)
            
    if not encontradas:
        logging.warning("No existe la tarea con esta categoría (o no has introducido bien la categoría..)")
        return
    else:
        logging.info(f"TAREAS ENCONTRADAS DE LA CATEGORÍA: {categoria}---")
        for tarea in encontradas:
            tarea.mostrar_info()
            logging.info("-----------------------------------")
            

def generar_reporte():
    """
    EXAMEN
    Esta función muestra todas las tareas guardadas en el fichero tareas.txt (con su control de errores como pides Pedro)
    """
    personal = 0
    laboral = 0
    social = 0
    tareas = cargar_tareas()
    if not tareas:
        logging.warning("No hay tareas guardadas.")
    else:
        print("\n-----LISTA DE TAREAS -----")
        for tarea in tareas:
            tarea.mostrar_info()
            if tarea.categoria == "personal":
                personal +=1
            if tarea.categoria == "laboral":
                laboral +=1
            if tarea.categoria == "social":
                social +=1
        total = laboral + personal + social
        print("CONTADOR DE TAREAS: ")
        print(f"PERSONALES:       {personal} --")
        print(f"LABORALES:       {laboral} --")
        print(f"SOCIALES:       {social} --")
        print("-----------------------------------")
        print(f"TOTALES:        {total} ------------")
        print("-----------------------------------")
        

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
                          "8.Generar Reporte\n"
                          "9.buscar por Categoria\n"
                          "10.salir del programa\n"))
    return respuesta
            
            
            
            


    
