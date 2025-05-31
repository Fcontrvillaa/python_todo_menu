
def ingresar_notas() -> list[float]:
    """Solicita al usuario ingresar notas separadas por espacios
        entrega lista de flotantes
    """
    n = input("ingresa las notas, separadas por espacio (7.0 3.4 4.4)")
    n = n.split(" ")
    notas = [float(nota) for nota in n ]
    return notas