from gestor_tareas import añadir_tareas, buscar_tarea, listar_tareas,  eliminar_tareas, modificar_tareas, menu

while True:
    print("\n")  # salto de línea antes de mostrar el menú que me da rabia que se vea todo junto en la terminal (PD: encontrarás más de un salto de línea innecesario pero me da paz mental).
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
    else:
        print("Opción inválida")
        
    print("\n")
    salir = input("¿Quieres seguir usando el programa? (s/n): ")
    if salir.lower() == "n":
        print("Hasta luego!")
        break



