def existe_libro(libros, titulo):
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            return True
    return False

def buscar_por_autor(libros, autor):
    """Busca y retorna todos los libros de un autor específico."""
    libros_autor = []
    for libro in libros:
        if libro['autor'].lower() == autor.lower():
            libros_autor.append(libro)
    return libros_autor

def main():
    
    biblioteca = [
        {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "disponible": True},
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": False},
        {"titulo": "1984", "autor": "George Orwell", "disponible": True},
        {"titulo": "Rebelión en la granja", "autor": "George Orwell", "disponible": False}
    ]

    
    print("--- COLECCIÓN DE LIBROS EN LA BIBLIOTECA ---")
    for libro in biblioteca:
        estado = "Disponible" if libro['disponible'] else "Prestado"
        print(
            f"- Título: '{libro['titulo']}' | Autor: {libro['autor']} | Estado: {estado}"
        )
    print("-" * 50)

    
    autor_a_buscar = "George Orwell"
    print(f"\n--- BUSCANDO LIBROS DE: {autor_a_buscar} ---")
    resultados = buscar_por_autor(biblioteca, autor_a_buscar)
    
    if resultados:
        for res in resultados:
            print(f"-> Encontrado: '{res['titulo']}'")
    else:
        print("No se encontraron libros de ese autor.")
    print("-" * 50)

    
    libro_a_verificar = "1984"
    print(f"\n--- VERIFICANDO DISPONIBILIDAD DE: '{libro_a_verificar}' ---")
    
    
    if existe_libro(biblioteca, libro_a_verificar):
       
        for libro in biblioteca:
            if libro['titulo'].lower() == libro_a_verificar.lower():
                if libro['disponible']:
                    print(f"¡Éxito! El libro '{libro_a_verificar}' está disponible para préstamo.")
                else:
                    print(f"Lo sentimos, el libro '{libro_a_verificar}' ya está prestado.")
    else:
        print(f"El libro '{libro_a_verificar}' no existe en nuestra colección.")
