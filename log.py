comandos = []
while True:
    comando = input("Escribe un comando (o 'history' para terminar): ")
    if comando.lower() == 'history':
        break
    comandos.append(comando) 

print("Comandos ingresados:", (comandos[-3:]))


