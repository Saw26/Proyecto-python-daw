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
            json.dump(tareas,fichero)
        
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

    nombre = input("Nombre de la tarea: ")
    if nombre == "":
        logging.warning("El nombre no puede estar vacío ")

    descripcion = input("Descripción de la tarea: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    categoria = input("Categoría (personal/laboral/social): ")
    
    # Una vez que le metemos los datos (la id, el nombre...) vamos a comprobar si todo está en su sitio y lo metemos al fichero

    if categoria != "personal" and categoria != "laboral" and categoria != "social":
        logging.warning("Categoría inválida. Debe ser 'personal', 'laboral' o 'social' ")

    tarea = f"{id};{nombre};{descripcion};{prioridad};{categoria}\n"

    fichero = open("tareas.txt", "a", encoding="utf-8") # No creo que haga falta explicarlo pero por si acaso,
    #aquí abro el archivo en formato append con su codificación para evitar rollos de tildes, la ñ.., escribo sobre el y lo cierro. (y así con las demás funciones que haré)
    fichero.write(tarea)
    fichero.close()

    logging.info("Tarea añadida correctamente y guardada en tareas.txt")


def listar_tareas():
    """
    Esta función muestra todas las tareas guardadas en el fichero tareas.txt (con su control de errores como pides Pedro)
    """
    try:
        fichero = open("tareas.txt", "r", encoding="utf-8") #aquí en formato "read" porque solo quiero leerlo
        lineas = fichero.readlines()
        fichero.close()

        if len(lineas) == 0:
            logging.warning("No hay tareas guardadas.")
        else:
            print("\n--- LISTA DE TAREAS ---")
            for linea in lineas:
                logging.debug(linea.strip()) # esto quita los espacios y demás al principio y al final (pero no en medio claro)
            print("-----------------------\n")
    except FileNotFoundError:
        logging.error("Todavía no existe el archivo de tareas ")
        
        
        # aquí llamamos al fichero con todo lo que tenga, lee cada línea (y las separa claro) y si no encuentra nada le he metido un control de errores
        
def buscar_tarea():
    """
    Esta función busca una tarea en el fichero de tareas.txt al meterle la ID (misma jugada, con su control de errores)
    """
    id_buscar = input("Introduce el ID de la tarea a buscar: ")

    try:
        fichero = open("tareas.txt", "r", encoding="utf-8") #la misma jugada que para listarlas todas, solo que aquí solo cojo la que yo le diga.
        lineas = fichero.readlines()
        fichero.close()

        encontrado = False
        for linea in lineas:
            partes = linea.strip().split(";")
            if partes[0] == id_buscar:
                encontrado = True
                print("\n--- TAREA ENCONTRADA!! ---")
                logging.debug(f"ID: {partes[0]}")
                logging.debug(f"Nombre: {partes[1]}")
                logging.debug(f"Descripción: {partes[2]}")
                logging.debug(f"Prioridad: {partes[3]}")
                logging.debug(f"Categoría: {partes[4]}")
                print("------------------------\n")
        if not encontrado:
            logging.warning("No se encontró ninguna tarea con ese ID ")
    except FileNotFoundError:
        logging.error("No existe el archivo de tareas ")


def eliminar_tareas():
    """
    Esta función elimina una tarea (por ID) del fichero tareas.txt (misma jugada, con su control de errores)
    """
    id_borrar = input("Introduce el ID de la tarea a eliminar: ")

    try:
        fichero = open("tareas.txt", "r", encoding="utf-8")
        lineas = fichero.readlines()
        fichero.close()

        fichero = open("tareas.txt", "w", encoding="utf-8")
        for linea in lineas:
            partes = linea.strip().split(";")
            if partes[0] != id_borrar:
                fichero.write(linea)
        fichero.close()
        
        # Aquí abro el fichero 2 veces (la primera para que lea todo lo que tiene y se guarde todo en "lineas" y luego en "w" para borrar la que le digamos
        # y si no coincide que vuelva a escribirla claro)

        logging.info("Tarea eliminada correctamente ")
    except FileNotFoundError:
        logging.error("No existe el archivo de tareas ")


def modificar_tareas():
    """
    Esta función modifica una tarea (por la ID que le metamos) del fichero tareas.txt (misma jugada, con su control de errores)
    """
    id_modificar = input("Introduce el ID de la tarea a modificar: ")

    try:
        fichero = open("tareas.txt", "r", encoding="utf-8")
        lineas = fichero.readlines()
        fichero.close()

        fichero = open("tareas.txt", "w", encoding="utf-8") # aquí lo abro en formato "write" para escribir sobre el ya que lo vamos a modificar claro.
        encontrado = False
        for linea in lineas:
            partes = linea.strip().split(";")
            if partes[0] == id_modificar:
                encontrado = True
                logging.info("Datos actuales de la tarea:")
                logging.info(f"ID: {partes[0]}, Nombre: {partes[1]}, Descripción: {partes[2]}, Prioridad: {partes[3]}, Categoría: {partes[4]}")
                logging.info("¿Qué quieres modificar?")
                logging.info("1. Nombre")
                logging.info("2. Descripción")
                logging.info("3. Prioridad")
                logging.info("4. Categoría")
                opcion = input("Elige una opción (1-4): ")

                if opcion == "1":
                    partes[1] = input("Nuevo nombre: ")
                elif opcion == "2":
                    partes[2] = input("Nueva descripción: ")
                elif opcion == "3":
                    partes[3] = input("Nueva prioridad: ")
                elif opcion == "4":
                    partes[4] = input("Nueva categoría: ")

                nueva_linea = f"{partes[0]};{partes[1]};{partes[2]};{partes[3]};{partes[4]}\n"
                fichero.write(nueva_linea)
            else:
                fichero.write(linea)
        fichero.close()

        if encontrado:
            logging.info("Tarea modificada correctamente ")
        else:
            logging.warning("No se encontró ninguna tarea con ese ID ")
    except FileNotFoundError:
        logging.error("No existe el archivo de tareas ")




def menu():
    # Muestra el menú para que el usuario decida qué hacer (seleccionando un número)
    respuesta = int(input("¿qué quieres hacer?\n"
                          "1. Añadir tarea\n"
                          "2. Buscar una tarea\n"
                          "3. Listar mis tareas\n"
                          "4. Modificar una tarea\n"
                          "5. borrar una tarea\n\n"
                          "6.Exportar a JSON\n"
                          "7.Importar desde JSON\n\n"))
    return respuesta
            
            
            
            


    
