def tateti ():
    tabla = (f"""
    —————————————————————————
    |       |       |       |
    |   {posiciones[0]}   |   {posiciones[1]}   |   {posiciones[2]}   |
    |       |       |       |
    —————————————————————————
    |       |       |       |
    |   {posiciones[3]}   |   {posiciones[4]}   |   {posiciones[5]}   |
    |       |       |       |
    —————————————————————————
    |       |       |       |
    |   {posiciones[6]}   |   {posiciones[7]}   |   {posiciones[8]}   |
    |       |       |       |
    —————————————————————————

    """)
    print (tabla)


def jugar():
    nombre_usuario1 = input ("Introduzca su nombre, Usuario 1: ")
    nombre_usuario2 = input ("introduzca su nombre, Usuario 2: ")
    tateti()
    while True:
        while True:
            usuario_1 = (input(f"Turno de {nombre_usuario1}, ingrese una posicion: ")) 
            if not usuario_1 in posiciones:
                print("Esa posicion ya se encuentra ocupada o es un valor invalido, por favor, elija otra posicion:")
            if usuario_1 in posiciones:
                lugar = posiciones.index(usuario_1)
                print (lugar) 
                posiciones[lugar] = "X"
                print (posiciones)
                break
        tateti()

        if not ("1" in posiciones or 
        "2" in posiciones or 
        "3" in posiciones or 
        "4" in posiciones or 
        "5" in posiciones or 
        "6" in posiciones or 
        "7" in posiciones or 
        "8" in posiciones or 
        "9" in posiciones):
            print("¡Empate! No hay más movimientos posibles.")
            break
        if posiciones[0] == "X":
            if posiciones[0] == posiciones [1] and posiciones[0] == posiciones[2]:
                print (f"El ganador es {nombre_usuario1}, ¡Felicitaciones!")
                break
            if posiciones[0] == posiciones [3] and posiciones[0] == posiciones[6]:
                print (f"El ganador es {nombre_usuario1}, ¡Felicitaciones!")
                break
            if posiciones[0] == posiciones [4] and posiciones[0] == posiciones [8]:
                print (f"El ganador es {nombre_usuario1}, ¡Felicitaciones!")
                break
        if posiciones[2] == "X":
            if posiciones [2] == posiciones[5] and posiciones[2] == posiciones[8]:
                print (f"El ganador es {nombre_usuario1}, ¡Felicitaciones!")
                break
            if posiciones [2] == posiciones [4] and posiciones [2] == posiciones [6]:
                print (f"El ganador es {nombre_usuario1}, ¡Felicitaciones!")
                break
        if posiciones[3] == "X":
            if posiciones [3] == posiciones [4] and posiciones [3] == posiciones [5]:
                print (f"El ganador es {nombre_usuario1}, ¡Felicitaciones!")
                break
        if posiciones [6] == "X":
            if posiciones [6] == posiciones [7] and posiciones[6] == posiciones [8]:
                print (f"El ganador es {nombre_usuario1}, ¡Felicitaciones!")
                break


        while True:    
            usuario_2 = (input(f"Turno de {nombre_usuario2}, ingrese un posicion: "))
            if not usuario_2 in posiciones:
                print ("Esa posicion ya se encuentra ocupada o es un valor invalido, por favor, elija otra posicion:")
            if usuario_2 in posiciones:
                lugar = posiciones.index(usuario_2) 
                print (lugar)
                posiciones[lugar] = "O"
                print (posiciones) 
                break
        tateti()

        if posiciones[0] == "O":
            if posiciones[0] == posiciones [1] and posiciones[0] == posiciones[2]:
                print (f"El ganador es {nombre_usuario2}, ¡Felicitaciones!")
                break
            if posiciones[0] == posiciones [3] and posiciones[0] == posiciones[6]:
                print (f"El ganador es {nombre_usuario2}, ¡Felicitaciones!")
                break
            if posiciones[0] == posiciones [4] and posiciones[0] == posiciones [8]:
                print (f"El ganador es {nombre_usuario2}, ¡Felicitaciones!")
                break
        if posiciones[2] == "O":
            if posiciones [2] == posiciones[5] and posiciones[2] == posiciones[8]:
                print (f"El ganador es {nombre_usuario2}, ¡Felicitaciones!")
                break
            if posiciones [2] == posiciones [4] and posiciones [2] == posiciones [6]:
                print (f"El ganador es {nombre_usuario2}, ¡Felicitaciones!")
                break
        if posiciones[3] == "X":
            if posiciones [3] == posiciones [4] and posiciones [3] == posiciones [5]:
                print (f"El ganador es {nombre_usuario2}, ¡Felicitaciones!")
                break
        if posiciones [6] == "O":
            if posiciones [6] == posiciones [7] and posiciones[6] == posiciones [8]:
                print (f"El ganador es {nombre_usuario2}, ¡Felicitaciones!")
                break



while True:
    menu = input("""MENU PRINCIPAL
        Seleccione una opción: 
        1-Jugar una nueva partida
        2-Salir
        Escriba aqui: """)
    if menu == "1":
        print("Comenzando...")
        posiciones = ["1","2","3", "4","5","6", "7","8","9"]
        jugar()
    elif menu == "2":
        while True:
            confirmar = input("¿Esta seguro que quiere salir? s/n: ").lower()
            if confirmar == "s":
                print ("Saliendo...")
                exit()
            if confirmar == "n":
                print("Volviendo al menu inicial")
                break
            else:
                print("Ese no es un valor correcto")
    else:
        print("Valor invalido, por favor, coloque un valor valido")
            
