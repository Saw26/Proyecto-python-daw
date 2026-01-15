import logging
from gestor_tareas import añadir_tareas, buscar_tarea, listar_tareas,  eliminar_tareas, modificar_tareas, menu, exportar_a_json, importar_json

while True:
    print("\n")  # salto de línea antes de mostrar el menú
    opcion = menu()
    if opcion == 1:
        print("\n")
        añadir_tareas()
    elif opcion == 2:
        print("\n")
        buscar_tarea()
    elif opcion == 3:
        print("\n")
        listar_tareas()
    elif opcion == 4:
        print("\n")
        modificar_tareas()
    elif opcion == 5:
        print("\n")
        eliminar_tareas()
    elif opcion == 6:
        print("\n")
        exportar_a_json()
    elif opcion == 7:
        print("\n")
        importar_json()
    else:
        logging.warning("Opción inválida")
        
    print("\n")
    salir = input("¿Quieres seguir usando el programa? (s/n): ")
    if salir.lower() == "n":
        logging.info("Hasta luego!")
        break



