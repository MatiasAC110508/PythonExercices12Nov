# 1

""" def agregar_plato(menu, plato):
    
    if plato == "":
        print("Porfavor agregue un plato.")
        return
    elif plato in menu:
        print("Plato duplicado.")
    else:
        print("Plato agregado.")
        menu.append(plato)
    
    for i, item in enumerate(menu, start = 1):
        print(f"{i}. {item}")

menu = []

agregar_plato(menu,"arroz con pollo")
agregar_plato(menu, "hamburguesa")
agregar_plato(menu, "chilaquiles")  """

# 2

""" def insertar_reserva(butacas, nombre, posicion):
    
    if posicion < 0 or posicion > len(butacas):
        print("\nError: posición invalida.")
        return
    
    butacas.insert(posicion, nombre)
    
    print(f"Reserva de {nombre} agregada en la posición {posicion}.")
    print("\nReservas actuales:")
    
    for i, item in enumerate(butacas, start=1):
        print(f"{i}. {item}")
        
butacas = ["Ana", "Luis", "Sofía"]

insertar_reserva(butacas, "Carlos", 1)
insertar_reserva(butacas, "María", 10)
insertar_reserva(butacas, "Pedro", 0)  """

# 3
    
""" def extender_inventario(actual, nuevos):
    
    if not nuevos:
        print("Error: -nuevos- esta vacio.")
        return
    
    actual.extend(nuevos)
    print(f"Inventario actualizado. Total de productos: {len(actual)}\n")
    
    for i, item in enumerate(actual, start = 1):
        
        if item in nuevos:
            print(f"{i}. {item} (nuevo)")
        else:
            print(f"{i}. {item}")
        
actual = ["leche", "pan", "café"]
nuevos = ["azúcar", "arroz"]

extender_inventario(actual, nuevos) """

# 4

""" def eliminar_libro(catalogo, titulo):
    
    if titulo in catalogo:
        catalogo.remove(titulo)
        print(f"\n{titulo} fue removido del catalogo.")
    else:
        print("\nNo encontrado.")
    
    print("\nCatalogo actualizado:")
    for i, item in enumerate(catalogo, start = 1):
        print(f"{i}. {item}")
        
catalogo = ["Harry Potter", "El Principito", "Don Quijote"]

eliminar_libro(catalogo, "El Principito")
eliminar_libro(catalogo, "It") """

# 5 
    
""" def liberar_ultima(butacas):
    
    if not butacas:
        print("Sala vacía.")
        return
    
    ultima = butacas.pop() 
    print(f"Silla liberada: {ultima}")
    
    print("\nEstado actual de las butacas:")
    for i, item in enumerate(butacas, start=1):
        print(f"{i}. {item}")
    
    return ultima
    
butacas = ["A1", "A2", "A3"]
liberar_ultima(butacas)

resultado = liberar_ultima(["A1", "A2", "A3"])
print("Valor devuelto:", resultado) """

# 6
    
""" def buscar_ticket(tickets, codigo):
    
    try:
        
        indice = tickets.index(codigo)
        duplicados = tickets.count(codigo)
        
        print(f"Ticket encontrado en posición {indice}.")
        
        if duplicados > 1:
            print(f"Hay {duplicados} tickets con el mismo código.")
        
        print("\nTickets actuales:\n")
        
        for i, item in enumerate(tickets, start=1):
            print(f"{i}. {item}")
        
        return indice

    except ValueError:
        print("Ticket no encontrado.")
        return -1

tickets = ["A12", "B55", "C77", "A12", "X01"]

buscar_ticket(tickets, "A12")
buscar_ticket(tickets, "C77")
buscar_ticket(tickets, "Z99")
buscar_ticket(tickets, "") """

# 7

""" def contar_marcador(marcadores, valor):
    if valor == "":
        print("ERROR: valor vacío.")
        return 0
    apariciones = marcadores.count(valor)


    if apariciones == 0:
        print(f"No hay apariciones en {marcadores} de el valor {valor}.")
        return 0
    
    print(f"El valor '{valor}' aparece {apariciones} veces.\n")
        
    print("\nMarcadores actuales:\n")
    for i, item in enumerate(marcadores, start = 1):
        if item == valor:
            print(f"- Posición {i}")

    return apariciones 
marcadores = [10, 20, 10, 30]
valor = 10

contar_marcador(marcadores, valor)

resultado = contar_marcador(marcadores, valor)
print("Apariciones totales: ", resultado) """

# 8

""" def ordenar_registros(registros, descendente = False):
    
    if not registros:
        print("La lista de registros está vacía.")
        return []
    try:
                
        ordenados = sorted(registros, reverse = descendente)
        
    except TypeError:
        print("\nError: los elementos no son comparables entre sí.")
        return None     
       
    print("Lista ordenada:", ordenados)
    print("\nTOP 3:\n")
        
    for i, item in enumerate(ordenados[:3], start=1):
        print(f"{i}. {item}")
        
    return ordenados
        
ordenar_registros([50, 10, 80, 30], descendente = False)
ordenar_registros([50, 10, 80, 30], descendente = True)
       
ordenar_registros(["hola", 10, 80.5, False], descendente=False)

resultado = ordenar_registros([50, 10, 80, 30], descendente = False)
print("\nRegistros ordenados: ", resultado) """

# 9 

""" def invertir_playlist(playlist):
    if not playlist:
        print("\nERROR: -playlist- esta vacía.")
        return
    
    playlist.reverse()
    
    print("\nReproduciendo las primeras 5 canciones (o menos):\n")
    
    for i, item in enumerate(playlist[:5], start = 1):
        print(f"{i}. {item}")
        
invertir_playlist(["Song A", "Song B", "Song C", "Song D", "Song E", "Song F"])
invertir_playlist(["Intro", "Beat 1", "Beat 2"])
invertir_playlist([]) """

# 10

""" def clonar_plan(modulos):
    
    if not modulos:
        print("\nError: -modulos- esta vacío.")
        return
    
    copia = modulos.copy()
    copia.append("NUEVO MÓDULO DE PRUEBA")

    print("\n--Comparación entre original y copia--\n")
    print("Plan original:")
    
    for i, item in enumerate(modulos, start=1):
        print(f"{i}. {item}")
    
    return copia

clonar_plan(["Intro a Python", "Variables", "Listas"])

resultado = clonar_plan(["Intro a Python", "Variables", "Listas"])
print("\nContenido de la copia retornada:\n")
print(resultado) """