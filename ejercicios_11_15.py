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
actualizar_carrito(carrito, "quitar", item=None, posicion=len(carrito)-1)  """

#14

""" def fusionar_candidatos(base_a, base_b, clave_desc = False, primeros_n = 5):
    
    if not base_a or not base_b:
        print("ERROR: Las listas no pueden estar vacías.")
    
    tipo_a = type(base_a[0])
    tipo_b = type(base_b[0])
    
    if tipo_a is not tipo_b:
        raise TypeError(f"Las listas deben contener el mismo tipo de dato. "
                        f"Base A: {tipo_a}, Base B: {tipo_b}")
    
    fusion = base_a + base_b
    
    try:
        
        f_ordenada = sorted(fusion, reverse = clave_desc)
    
    except Exception:
        raise ValueError("Los elementos no son comparables para ordenar.")
    
    print(f"Primeros {primeros_n} candidatos:")
    for candidato in f_ordenada[:primeros_n]:
        print("-", candidato)
    
    return f_ordenada

base_a = ["Ana", "Luis", "Carla"]
base_b = ["Pedro", "Jorge"]

resultado = fusionar_candidatos(base_a, base_b, clave_desc=True, primeros_n=3) """

# 15

""" def depurar_ventas(ventas, umbral):
    
    ventas_validas = []
    removidos = 0
    
    for venta in ventas:
        if venta is None or  venta < 0:
            removidos += 1
        else:
            ventas_validas.append(venta)
            
    counter = {}
    ventas_f = []
    
    for venta in ventas_validas:
        counter.setdefault(venta, 0)

        if counter[venta] < umbral:
            ventas_f.append(venta)
            counter[venta] += 1
        else:
            removidos += 1
    
    print("Lista final depurada:", ventas_f)
    print("Cantidad de elementos removidos:", removidos)

    return ventas_f, removidos

ventas = [10, 20, 20, 20, 20, None, -5, 10, 10, 10]
umbral = 2

depurar_ventas(ventas, umbral) """
    
    