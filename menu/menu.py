
from funciones.funciones import *

def menu():
  matriz = []
  
  while(True):
    opcion = int(input("""
    Elija una opción:
    -----------------
                       
    1) Calificar cocineros
    2) Mostrar notas
    3) Ordenar por orden ascendente o descendent (ASC / DESC)
    4) Mostrar Peores Promedios
    5) Muestrar mayores promedios
    6) Jurado malo
    7) Sumatoria
    8) Mostrar ganador
    9) Salir
    
    Su opción elegida es: """))
    
    if opcion == 1:
      matriz = inicializar_matriz(5,4,0)
      cargar_datos(matriz)
    elif opcion == 2:
      if not matriz:
        print("!!ERROR¡¡ Aun no hay datos cargados... Presione la opción 1 para cargar datos.")
      else:
        mostrar_resultados(matriz)
    elif opcion == 3:
      if not matriz:
          print("!!ERROR¡¡ Aun no se puede ordenar la matriz, la misma está vacía.")
      else:
          orden = input("¿Desea ordenar de forma descendente o ascendente? (Ingrese 'desc' o 'asc'): ")
          if orden != "asc" and orden != "desc":
            print("¡Opción inválida!")
          elif orden == "asc":
            print("\n Matriz odenada de forma ascendente. Pulse la opción 2 para ver los resultados.")
            print("------------------------------------------------------------------------------\n")
            ordenar_matriz_asc(matriz)
          elif orden == "desc":
            print("\n Matriz odenada de forma descendente. Pulse la opción 2 para ver los resultados.")
            print("------------------------------------------------------------------------------\n")
            ordenar_matriz_desc(matriz)
    elif opcion == 4:
      if not matriz:
        print("¡¡ERROR!! No se pueden ver los peores promedios porque aún no hay datos cargados.")
      else:
        print("Mostrando los peores 3 participantes en base a su promedio.")
        print("----------------------------------------------------------\n")
        mostrar_peores_promedios(matriz)
    elif opcion == 5:
      if not matriz:
        print("¡¡ERROR!! No se pueden ver los 3 mejores promedios porque aún no hay datos cargados.")
      else:
        print("Mostrado los participantes que superan el promedio general de notas.")
        print("--------------------------------------------------------------------\n")
        mostrar_mayor_promedio(matriz)
    elif opcion == 6:
      if not matriz:
        print("¡¡ERROR!! El jurado aún no se ha pronunciado debido a que no hay datos cargados.")
      else:
        print("Mostrando al jurado que puso en promedio las peores notas.")
        print("---------------------------------------------------------\n")
        mostrar_jurado_malo(matriz)
    elif opcion == 7:
      if not matriz:
        print("¡¡ERROR!! No se pueden buscar coincidencias porque aún no hay datos cargados.")
      else:
        print("Mostrando (si lo hay) el/los participantes cuyas notas sumadas den la cifra ingresada.")
        print("--------------------------------------------------------------------------------------\n")
        calcular_sumatoria(matriz)
    elif opcion == 8:
      if not matriz:
        print("¡¡ERROR!! Aún no hay un ganador debido a que no hay datos que procesar.")
      else:
        print("Mostrando al ganador del concurso.")
        print("-----------------------------------\n")
        calcular_ganador(matriz)
    elif opcion == 9:
      print("Saliendo...........")
      break
    else:
      print("¡¡¡ERROR!!!! El valor ingresado debe estar entre los valores 1 y 9. Reingrese un número: ")
      

