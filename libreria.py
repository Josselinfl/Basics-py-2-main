"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""

def agregar_libro(titulo, autor):
    """Crea y retorna un diccionario con el título y el autor de un libro."""
    return {"titulo": titulo, "autor": autor}

libro_favorito = agregar_libro("Cien años de soledad", "Gabriel García Márquez")
segundo_libro = agregar_libro("1984", "George Orwell")

print(libro_favorito)
print(segundo_libro)


"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""

def listar_libros(libros):
    """Acepta una lista de diccionarios de libros y retorna una lista

    solo con sus títulos.
    """
    titulos = []
    for libro in libros:
        titulos.append(libro["titulo"])
    return titulos

mi_biblioteca = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "1984", "autor": "George Orwell"},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry"},
]

lista_de_titulos = listar_libros(mi_biblioteca)

print(lista_de_titulos)

"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""

def buscar_libro(libros, titulo):
    """Busca un libro por su título en la lista de diccionarios.

    Retorna el diccionario del libro si lo encuentra, o None si no.
    """
    for libro in libros:
        
        if libro["titulo"].lower() == titulo.lower():
            return libro
    return None


mi_biblioteca = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "1984", "autor": "George Orwell"},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry"},
]


resultado1 = buscar_libro(mi_biblioteca, "1984")
print("Búsqueda '1984':", resultado1)

resultado2 = buscar_libro(mi_biblioteca, "el principito")
print("Búsqueda 'el principito':", resultado2)


resultado3 = buscar_libro(mi_biblioteca, "Don Quijote de la Mancha")
print("Búsqueda 'Don Quijote':", resultado3)

"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""

def quitar_libro(libros, titulo):
    """Intenta eliminar un libro por su título.

    Si lo encuentra, lo borra de la lista y lo retorna.
    Si no lo encuentra, lanza un ValueError.
    """
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            libros.remove(libro)
            return libro  

    
    raise ValueError(f"Error: El libro '{titulo}' no se encuentra en la lista.")




mi_biblioteca = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "1984", "autor": "George Orwell"},
]


print("--- Intento 1: Eliminar '1984' ---")
try:
    eliminado = quitar_libro(mi_biblioteca, "1984")
    print(f"Éxito: Se ha eliminado {eliminado}")
    print(f"Biblioteca actualizada: {mi_biblioteca}\n")
except ValueError as e:
    print(e)


print("--- Intento 2: Eliminar 'El Principito' ---")
try:
    eliminado = quitar_libro(mi_biblioteca, "El Principito")
    print(f"Éxito: Se ha eliminado {eliminado}")
except ValueError as e:
    print(f"Capturado con éxito -> {e}")


"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""

def crear_inventario(libros):
    """Acepta una lista de diccionarios de libros y retorna un diccionario

    con la cantidad total de libros que tiene cada autor.
    """
    inventario = {}

    for libro in libros:
        autor = libro["autor"]
        # Si el autor ya está en el diccionario, sumamos 1.
        # Si no está, lo inicializamos en 0 y sumamos 1.
        inventario[autor] = inventario.get(autor, 0) + 1

    return inventario


mi_biblioteca = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "1984", "autor": "George Orwell"},
    {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez"},
    {"titulo": "Rebelión en la granja", "autor": "George Orwell"},
    {"titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez"},
    {"titulo": "Dune", "autor": "Frank Herbert"},
]


conteo_autores = crear_inventario(mi_biblioteca)


print("Inventario por autor:")
for autor, cantidad in conteo_autores.items():
    print(f"- {autor}: {cantidad} libro(s)")


"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""

def libros_por_autor(libros, autor):
    """Filtra los libros por autor y retorna una lista

    únicamente con los títulos de sus libros.
    """
    titulos_filtrados = []

    for libro in libros:
        
        if libro["autor"].strip().lower() == autor.strip().lower():
            titulos_filtrados.append(libro["titulo"])

    return titulos_filtrados

mi_biblioteca = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "1984", "autor": "George Orwell"},
    {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez"},
    {"titulo": "Rebelión en la granja", "autor": "George Orwell"},
    {"titulo": "Dune", "autor": "Frank Herbert"},
]


print("--- Libros de Gabriel García Márquez ---")
libros_gabo = libros_por_autor(mi_biblioteca, "Gabriel García Márquez")
print(libros_gabo)


print("\n--- Libros de Stephen King ---")
libros_king = libros_por_autor(mi_biblioteca, "Stephen King")
print(libros_king)

"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""

def existe_libro(libros, titulo):
    """
    Busca un libro por su título en una lista de diccionarios.
    Retorna True si lo encuentra, False en caso contrario.
    """
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            return True
    return False


mis_libros = [
    {"titulo": "El Quijote", "autor": "Cervantes"},
    {"titulo": "Cien años de soledad", "autor": "García Márquez"},
    {"titulo": "1984", "autor": "George Orwell"}
]


print(existe_libro(mis_libros, "1984"))          
print(existe_libro(mis_libros, "El Quijote"))           
print(existe_libro(mis_libros, "El principito"))       

