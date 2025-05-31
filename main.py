#sistema de notas
# 1 ingresar notas
#calcular estadistica de otas
#nota mas baja
#cantidad de aprobados


from notas.menu import menu
#from notas import *
from notas.ingresa_notas import ingresar_notas
from notas.calculos import calcular_estadisticas
    
def main():
    notas = []

    while True:
        menu()
        opcion = (input("ingrese una opcion"))  #  falta tray set  poner solo numeros validos
        
        if opcion == "1":
            ingresar_notas()
            print("notas ingresadas")

            #break
        elif opcion == "2":  # promedio, nota mayor, nota menor, aprobados
            if calcular_estadisticas(notas) == None:
                print()
                notas = ingresar_notas()

            estadisticas = calcular_estadisticas(notas)
            #print(notas)

        elif opcion == "3":
           estadisticas
           print(estadisticas)
        
        else:
            print("terminado")
            break


if __name__ == "__main__":
    main()