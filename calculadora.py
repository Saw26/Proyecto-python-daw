def accion():
    # Solicita al usuario qué operación quiere realizar
    operacion = int(input("¿Qué quieres hacer?\n"
                          "1. Sumar\n"
                          "2. Restar\n"
                          "3. Multiplicar\n"
                          "4. Dividir\n"))
    return operacion


def menu():
    # Muestra el menú para que el usuario decida qué hacer
    respuesta = int(input("¿Qué quieres hacer?\n"
                          "1. Continuar haciendo cálculos?\n"
                          "2. Reiniciar calculadora\n"
                          "3. Historial de operaciones\n"
                          "4. Cerrar la calculadora\n"))
    return respuesta


def operaciones(almacenado, numero2, historial, operacion):
    # Realiza la operación seleccionada y guarda el historial
    if operacion == 1:
        suma = almacenado + numero2
        historial += f"{almacenado} + {numero2} = {suma}\n"
        almacenado = suma
    elif operacion == 2:
        resta = almacenado - numero2
        historial += f"{almacenado} - {numero2} = {resta}\n"
        almacenado = resta
    elif operacion == 3:
        multiplicación = almacenado * numero2
        historial += f"{almacenado} * {numero2} = {multiplicación}\n"
        almacenado = multiplicación
    elif operacion == 4:
        # Controla la división por cero
        if numero2 != 0:
            division = almacenado / numero2
            historial += f"{almacenado} / {numero2} = {division}\n"
            almacenado = division
        else:
            print("No se puede dividir por cero.")
            historial += f"{almacenado} / {numero2} = Error (división por cero)\n"
    return almacenado, historial


# Inicio del programa
numero1 = int(input("Introduce un número\n"))
respuesta = 1
almacenado = numero1
historial = ""

while respuesta != 4:
    if respuesta == 2:
        # Reiniciar la calculadora
        almacenado = int(input("Introduce el primer número\n"))
        historial = ""  # Limpiar el historial al reiniciar
    elif respuesta == 3:
        # Mostrar el historial de operaciones
        print("Historial de operaciones:")
        print(historial)

    # Llamar a la función 'accion' para obtener la operación
    calculo = accion()

    numero2 = int(input("Introduce otro número\n"))

    # Realizar la operación y actualizar el historial
    almacenado, historial = operaciones(almacenado, numero2, historial, calculo)

    # Mostrar el resultado
    print("El resultado es:", almacenado)

    # Mostrar el menú para seguir o salir
    respuesta = menu()

print("Calculadora cerrada.")
