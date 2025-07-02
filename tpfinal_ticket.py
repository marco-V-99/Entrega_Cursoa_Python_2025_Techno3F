import random, json, os

def cargar_tickets():
    if os.path.exists("tickets.json"):
        with open("tickets.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return {}

def guardar_tickets(cticket):
    with open("tickets.json", "w", encoding="utf-8") as archivo:
        json.dump(cticket, archivo, indent=4)

def alta_ticket(cticket):
    while True:
        info = {
            "Nombre": input("Introduzca su nombre: "),
            "Sector": input("Introduzca su área: "),
            "Asunto": input("Introduzca su asunto: "),
            "Problema": input("Introduzca su problema: ")
        }

        while True:
            nro_ticket = str(random.randint(0000, 9999))
            if not cticket.get(nro_ticket):  
                break

        cticket[nro_ticket] = info

        print(f"""
Tu número de ticket es {nro_ticket}, por favor RECORDAR ESTE NÚMERO
La información de tu ticket es:
    Nombre: {info['Nombre']}
    Sector: {info['Sector']}
    Asunto: {info['Asunto']}
    Problema: {info['Problema']}
""")

        guardar_tickets(cticket)

        while True:
            continuar = input("¿Desea generar otro ticket? (s/n): ").lower()
            if continuar == 's':
                break
            elif continuar == 'n':
                print("Finalizando la generación de tickets.")
                return
            else:
                print("Valor inválido. Por favor, ingrese 's' o 'n'.")

def menu():
    cticket = cargar_tickets()

    while True:
        iniciar = input("""Bienvenido, elija una opción:
1 - Crear un nuevo ticket
2 - Leer un ticket
3 - Salir
Opción: """)

        if iniciar == "1":
            alta_ticket(cticket)
        elif iniciar == "2":
            if not cticket:
                print("No hay tickets registrados.")
            else:
                elegido = input("Ingrese el número del ticket que desea ver: ")
                resultado = cticket.get(elegido)
                if resultado:
                    print(f"""
    Ticket Nº: {elegido}
Nombre: {resultado['Nombre']}
Sector: {resultado['Sector']}
Asunto: {resultado['Asunto']}
Problema: {resultado['Problema']}
""")
                else:
                    print("No se encontró un ticket con ese número.")
        elif iniciar == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()