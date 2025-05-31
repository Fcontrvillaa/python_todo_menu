#sistema de notas
# 1 ingresar notas
#calcular estadistica de otas
#nota mas baja
#cantidad de aprobados


#menu
def menu():
    print("""
Menu de Opciones
1. ingresar nota
2. Calcula estadisticas
3. Resultados
4. Salir
""")
    
def main():
    notas = []

    while True:
        menu()
        opcion = (input("ingrese una opcion"))  #  falta tray set  poner solo numeros validos
        
        if opcion == "1":
            n = input("ingresa las notas, separadas por espacio (7.0 3.4 4.4)")
            n = n.split(" ")
            notas = [float(nota) for nota in n ]
            print(notas)
            #break
        elif opcion == "2":  # promedio, nota mayor, nota menor, aprobados
            #print("2")
            #break


            try:   
                promedio = sum(notas) / len(notas)
                mayor = max(notas)
                menor = min(notas)
                aprobado = [ a for a in notas if a >= 4.0]
                print(aprobado)
            except ZeroDivisionError:
                print("no hay notas agregadas")


        elif opcion == "3":
            print(f"""
                promedio : {promedio}  
                minimo : {menor}
                maximo : {mayor}
                aprobado : {aprobado}
                  
            """)
        
        else:
            print("terminado")
            break


if __name__ == "__main__":
    main()