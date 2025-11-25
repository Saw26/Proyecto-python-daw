def añadir_tareas():
    """
    Esta función le pide datos al usuario y añade una nueva tarea al fichero que tenemos de tareas.txt (y he añadido un control de errores)
    """
    try:
        id = int(input("ID de la tarea (número): "))
    except ValueError:
        print("El ID debe ser un número entero ")

    nombre = input("Nombre de la tarea: ")
    if nombre == "":
        print("El nombre no puede estar vacío ")

    descripcion = input("Descripción de la tarea: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    categoria = input("Categoría (personal/laboral/social): ")
    
    # Una vez que le metemos los datos (la id, el nombre...) vamos a comprobar si todo está en su sitio y lo metemos al fichero

    if categoria != "personal" and categoria != "laboral" and categoria != "social":
        print("Categoría inválida. Debe ser 'personal', 'laboral' o 'social' ")

    tarea = f"{id};{nombre};{descripcion};{prioridad};{categoria}\n"

    fichero = open("tareas.txt", "a", encoding="utf-8") # No creo que haga falta explicarlo pero por si acaso,
    #aquí abro el archivo en formato append con su codificación para evitar rollos de tildes, la ñ.., escribo sobre el y lo cierro. (y así con las demás funciones que haré)
    fichero.write(tarea)
    fichero.close()

    print("Tarea añadida correctamente y guardada en tareas.txt")


def listar_tareas():
    """
    Esta función muestra todas las tareas guardadas en el fichero tareas.txt (con su control de errores como pides Pedro)
    """
    try:
        fichero = open("tareas.txt", "r", encoding="utf-8") #aquí en formato "read" porque solo quiero leerlo
        lineas = fichero.readlines()
        fichero.close()

        if len(lineas) == 0:
            print("No hay tareas guardadas.")
        else:
            print("\n--- LISTA DE TAREAS ---")
            for linea in lineas:
                print(linea.strip()) # esto quita los espacios y demás al principio y al final (pero no en medio claro)
            print("-----------------------\n")
    except FileNotFoundError:
        print("Todavía no existe el archivo de tareas ")
        
        
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
                print(f"ID: {partes[0]}")
                print(f"Nombre: {partes[1]}")
                print(f"Descripción: {partes[2]}")
                print(f"Prioridad: {partes[3]}")
                print(f"Categoría: {partes[4]}")
                print("------------------------\n")
        if not encontrado:
            print("No se encontró ninguna tarea con ese ID ")
    except FileNotFoundError:
        print("No existe el archivo de tareas ")


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

        print("Tarea eliminada correctamente ")
    except FileNotFoundError:
        print("No existe el archivo de tareas ")


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
                print("Datos actuales de la tarea:")
                print(f"ID: {partes[0]}, Nombre: {partes[1]}, Descripción: {partes[2]}, Prioridad: {partes[3]}, Categoría: {partes[4]}")
                print("¿Qué quieres modificar?")
                print("1. Nombre")
                print("2. Descripción")
                print("3. Prioridad")
                print("4. Categoría")
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
            print("Tarea modificada correctamente ")
        else:
            print("No se encontró ninguna tarea con ese ID ")
    except FileNotFoundError:
        print("No existe el archivo de tareas ")



            
def menu():
    # Muestra el menú para que el usuario decida qué hacer (seleccionando un número)
    respuesta = int(input("¿qué quieres hacer?\n"
                          "1. Añadir tarea\n"
                          "2. Buscar una tarea\n"
                          "3. Listar mis tareas\n"
                          "4. Modificar una tarea\n"
                          "5. borrar una tarea\n\n"))
    return respuesta
            
            
            
            


    
