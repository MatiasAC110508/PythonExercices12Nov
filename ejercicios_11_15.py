# 11

""" def finalizar_ruta(paradas):
    
    if not paradas:
        print("\nERROR: -paradas- esta vacía.")
        return
    
    for i, item in enumerate(paradas, start = 1):
        print(f"{i}. {item}(Visitada).")

    paradas.clear()
    print(f"\nLas paradas han sido limpiadas correctamente.")

paradas = ["Parque Central", "Museo", "Terminal", "Hotel"]
finalizar_ruta(paradas)

paradas = []
finalizar_ruta(paradas)

ruta_mañana = ["Centro", "Hospital", "Plaza"]
print("\nIniciando ruta de la mañana...")
finalizar_ruta(ruta_mañana)
print("Ruta de la mañana completada.")
 """

# 12

""" def marcar_asistencia(estudiantes, indice, estado):
   
    if 0 <= indice < len(estudiantes):
        estudiantes[indice] = estado  

    presentes = 0
    ausentes = 0

    for e in estudiantes:
        if e == "presente":
            presentes += 1
        elif e == "ausente":
            ausentes += 1

    return presentes, ausentes   

lista = ["presente", "ausente", "presente"]

print(marcar_asistencia(lista, 1, "presente")) """

# 13

""" def actualizar_carrito(carrito, accion, item, posicion = None):
    
    if accion == "agregar":
        if posicion is None:
            carrito.append(item)
        elif 0 <= posicion <= len(carrito):
            carrito.insert(posicion, item) 
        else:
            pass
    
    elif accion == "quitar":
        if posicion is None:
            print("ERROR: -posicion esta vacío.")
        elif 0 <= posicion < len(carrito):
            del carrito[posicion]        
        else:
            print("ERROR: posicion invalida.")
            
    print("\nCarrito actual:\n")
    
    for i, item in enumerate(carrito, start = 1):
        print(f"{i}. {item}.")
    
    return  

carrito = ["Pan", "Leche", "Huevos"]

actualizar_carrito(carrito, "agregar", "Manzanas")
actualizar_carrito(carrito, "agregar", "Café", posicion=1)
actualizar_carrito(carrito, "quitar", item=None, posicion=0)
actualizar_carrito(carrito, "quitar", item=None, posicion=len(carrito)-1) """
