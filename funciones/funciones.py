
# inicializar matriz
def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []

    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

COLUMNA = 0
JURADO_1 = 1
JURADO_2 = 2
JURADO_3 = 3

# Validaar que los datos a ingresar sean correctos
def validar_nota_jurado(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
  """"
    - Valida que los datos ingresados estén entre los rangos mínimo y máximo antes de cargarlos a la matriz.

  Parámetros:
    - mensaje: Un mensaje que será mostrado al usuario para pedirle que ingrese un dato.
    - mensaje_error: Un mensaje que se mostrará al usuario en caso de que ingrese un dato inválido.
    - minimo: El valor mínimo que la función aceptará como un dato válido.
    - máximo: El valor máximo que la función aceptará como un dato válido.
  
  Retorna:
    - Un número entero válido entre los rangos mínimo y máximo.
  """

  numero = int(input(mensaje))
  while numero > maximo or numero < minimo:
      numero = int(input(mensaje_error))
  return numero

#1 Carga secuencial de cocineros y notas
def cargar_datos( matriz:list ) -> list:
  """"
    - carga los datos de forma secuancial en una matriz bidimensional.
  
  Parámetros:
    matriz (list): Una matriz bidimensional inicializada previamente donde se cargarán los datos.
    - Cada fila representa un participante con sus respectivas notas por jurado.
    - Cada columna representa al numero de participante y ademas, la nota de cada juez.

  Notas:
    - Se validan usando la función validar_nota_jurado() antes de ser cargadas.

  """

  print("""\nCarga de datos secuencial.
-------------------------------------\n""")
  
  for fila in range(len(matriz)):
    matriz[fila][COLUMNA] = fila +1
    print(f"Participante N°: {fila +1}")
    matriz[fila][JURADO_1] = validar_nota_jurado("Ingrese la nota del jurado 1: ", "!!ERROR¡¡ La nota no puede ser menor a 1 ni mayor a 100. Ringrese la nota del jurado 1: ", 1, 100)
    matriz[fila][JURADO_2] = validar_nota_jurado("Ingrese la nota del jurado 2: ", "!!ERROR¡¡ La nota no puede ser menor a 1 ni mayor a 100. Ringrese la nota del jurado 2: ", 1, 100)
    matriz[fila][JURADO_3] = validar_nota_jurado("Ingrese la nota del jurado 3: ", "!!ERROR¡¡ La nota no puede ser menor a 1 ni mayor a 100. Ringrese la nota del jurado 3: ", 1, 100)
    print(f"\n")

# Calculamos la cantidad de votos totales de la matriz
def calcular_votos_totales(matriz:list) -> list:
  """"
    - Calcula la cantidad de votos totales que están cargados en la matriz usando una funcion complementaria.
  
  Parámetros:
    - matriz (list): Una matriz bidimensional con los datos ya cargados.

  Función complementaria:
    - sumar_votos_fila(matriz,fila) --> Recorre cada fila de la matriz pasada por argumento y acumula la cantidad de votos en la variable votos_totales.
    
  Retorna:
    - La cantidad total de votos de toda la matriz.
  """
  votos_totales = 0
  for fila in range(len(matriz)):
    votos_totales += sumar_votos_fila(matriz, fila)
  return votos_totales
    
# Calculamos la cantidad de votos por fila (es decir, por participante)
def sumar_votos_fila(matriz:list, fila:int) -> int:
  """"
    - Calcula la cantidad de votos de cada fila sumando sus columnas.
  
  Parámetros:
    - matriz (list): Una matriz bidimensional con los datos ya cargados.
    - fila (int): Un número entero que representa cada fila de la matriz a recorrer.

  Retorna:
    - votos_por_fila: Variable que guarda la cantidad total de votos por fila.
  """

  votos_por_fila =  matriz[fila][JURADO_1] + matriz[fila][JURADO_2] + matriz[fila][JURADO_3]
  return votos_por_fila

# Calculamos el promedio de votos por participante
def calcular_promedio_de_votos(matriz:list, fila:int) -> float:
  """"
    - Calcula la cantidad de votos entre todos los participantes.
    - Calcula un promedio sumando los votos por fila y dividiendolos por la cantidad de columnas de la fila.
  
  Parámetros:
    - matriz (list): Una matriz bidimensional con los datos ya cargados.
    - fila (int): Un numero entero que representa cada fila de la matriz a recorrer.

  Funciónes complementarias:
    - calcular_votos_totales(matriz) --> Recibe una matriz y calcula la cantidad de votos totales que tiene cargada
    - sumar_votos_fila(matriz,fila) --> Recorre cada fila de la matriz pasada por argumento y acumula la cantidad de votos en la variable votos_totales.
    
  Retorna:
    - un numero (float) redondeado usando el método round(). El mismo tiene como máximo dos dígitos despúes de la coma.
  """
  promedio = 0
  votos_totales = calcular_votos_totales(matriz)
  votos_por_fila = sumar_votos_fila(matriz, fila)
  if votos_totales > 0:
    promedio = votos_por_fila / (len(matriz[0]) -1)
    
  return round(promedio,2)


# 2 MOSTRAR VOTOS

def mostrar_lista(fila:list) -> None:
  """"
    - Muestra datos.

  Parámetros:
    - fila (list): Una matriz con datos cargados.
  """
  print(f"PARTICIPANTE N°: {fila[COLUMNA]}")
  print(f"NOTA DEL JURADO N° 1: {fila[JURADO_1]} votos")
  print(f"NOTA DEL JURADO N° 2: {fila[JURADO_2]} votos")
  print(f"NOTA DEL JURADO N° 3: {fila[JURADO_3]} votos")

# Mostamos los resultados más el cálculo del promedio
def mostrar_resultados(matriz:list) -> list:
  """"
    - Recorre la matriz recibida por parámetro.
    - Muestra los resultados usando una funcion complementaria mostrar_lista.
    - Calcula el promedio de votos usando la función (calcular_promedio_de_votos()) y los muestra.

  Parámetros:
    - matriz (list): Una matriz con datos cargados.
  función complementaria:
    - mostrar_lista(fila:list).
    - calcular_promedio_de_votos(matriz,fila).
  Retorna:
    - Los datos mostrados de forma prolija más el cálculo del promedio utilizando la función calcular_promedio_de_votos(matriz,fila).
  """

  print("""
Mostrando los resultados cargados.
----------------------------------\n""")

  for fila in range(len(matriz)):
    mostrar_lista(matriz[fila])
    print(f"PROMEDIO DE VOTOS: {calcular_promedio_de_votos(matriz, fila)}")
    print("\n")


# 3  ORDENAR LA MATRIZ POR PROMEDIOS

def ordenar_matriz_desc(matriz:list) -> list:
  """"
    - Ordena una matriz pasada por parámetro.

  Parámetros:
    - fila (list): Una matriz con datos cargados.
  Retorna:
    - Una matriz ordenada por su columna promedio.
  """

  for i in range(len(matriz) - 1):
    for j in range(i+1,len(matriz)):
      if calcular_promedio_de_votos(matriz,i) < calcular_promedio_de_votos(matriz,j):
        auxiliar = matriz[i]
        matriz[i] = matriz[j]
        matriz[j] = auxiliar
  return matriz
 
def ordenar_matriz_asc(matriz:list) -> list:
  """"
    - Ordena la matriz pasada por parámetro.

  Parámetros:
    - fila (list): Una matriz con datos cargados.
  Retorna:
    - Una matriz ordenada de forma ascendente por su columna promedio.
  """

  for i in range(len(matriz) - 1):
    for j in range(i+1,len(matriz)):
      if calcular_promedio_de_votos(matriz, i) > calcular_promedio_de_votos(matriz, j):
        auxiliar = matriz[i]
        matriz[i] = matriz[j]
        matriz[j] = auxiliar
  return matriz

# 4  MOSTRAR LOS 3 PARTICIPANTES CON PEOR PROMEDIO

def mostrar_peores_promedios(matriz:list) -> list:
  """"
    - Ordena la matriz pasada por parámetro..

  Parámetros:
    - fila (list): Una matriz con datos cargados.
  Retorna:
    - Una matriz ordenada por promedios. Se muestran solo los 3 primeros resultados.
    - para que conincida con lo que pide la consigna. 
  """
  res = ordenar_matriz_asc(matriz)
  for fila in range(len(res)-2):
    print(f"PARTICIPANTE N°: {res[fila][COLUMNA]}")
    print(f"NOTA DEL JURADO N° 1: {res[fila][JURADO_1]}")
    print(f"NOTA DEL JURADO N° 2: {res[fila][JURADO_2]}")
    print(f"NOTA DEL JURADO N° 3: {res[fila][JURADO_3]}")
    print(f"PROMEDIO DE VOTOS: {calcular_promedio_de_votos(res, fila)}\n")
 

# 5 MAYOR PROMEDIO
def mostrar_mayor_promedio(matriz:list) -> list:
  """"
    - Calcula el promedio de todas las notas (la suma de puntos de los 5 participantes devidida la cantidad de notas "15").
    - Luego recorre las filas calculando el promedio de notas que obtuvo cada participante y lo compara contra ese
    - promedio general de notas. 
    - Si la nota promedio del participante super la nota promedio general, se muestran los datos de ese participante.

  Funciones Complementarias:
    - calcular_votos_totales().
    - calcular_promedio_de_votos().

  Parámetros:
    - fila (list): Una matriz con datos cargados.
  Retorna:
    - Aquellos promedios que superen al promedio total de todos los votos.
  """
  votos_totales =  calcular_votos_totales(matriz)
  promedio_de_todas_las_notas = votos_totales / 15


  for fila in range(len(matriz)):
    promedios = calcular_promedio_de_votos(matriz, fila)
    if promedios > promedio_de_todas_las_notas:
      print(f"PARTICIPANTE N°: {matriz[fila][COLUMNA]}")
      print(f"NOTA DEL JURADO N° 1: {matriz[fila][JURADO_1]}")
      print(f"NOTA DEL JURADO N° 2: {matriz[fila][JURADO_2]}")
      print(f"NOTA DEL JURADO N° 3: {matriz[fila][JURADO_3]}")
      print(f"PROMEDIO DE VOTOS: {calcular_promedio_de_votos(matriz, fila)}\n")

# 6 JURADO MALO
def mostrar_jurado_malo(matriz:list) -> list:
  """"
    - Recibe la matriz con datos para pasarsela a la función calcular_jurado_malo().

  Parámetros:
    - fila (list): Una matriz con datos cargados.
  """
  calcular_jurado_malo(matriz)
 
       
def sumar_votos_por_columna(matriz:list, columna:int) -> int:
  """"
    - Suma los votos por columna de una matriz recibida por parámetro.

  Parámetros:
    - fila (list): Una matriz con datos cargados.
    - columna (int) Un número entero que va a representar a cada columna dinámicamente.
  Retorna:
    - La suma total de los elementos por columna.
  """
  suma_por_columna = 0
  for fila in range(len(matriz)):
    suma_por_columna += matriz[fila][columna]
  return suma_por_columna


def calcular_jurado_malo(matriz:list):
  """"
    - Suma las notas que cada jurado puso por participante y las promedia.
    - Los promedios se comparan entre si para saber cual de los 3 jueces
      puso la nota mas baja entre todos los participantes. 

  Parámetros:
    - fila (list): Una matriz con datos cargados.
  Retorna:
    - El promedio mas bajo calculado de las notas que los jueces pusierona a los cocineros.
  """
  promedio_de_votos_del_jurado_1 = (sumar_votos_por_columna(matriz, JURADO_1) / 5)
  promedio_de_votos_del_jurado_2 = (sumar_votos_por_columna(matriz, JURADO_2) / 5)
  promedio_de_votos_del_jurado_3 = (sumar_votos_por_columna(matriz, JURADO_3) / 5)
       
  if promedio_de_votos_del_jurado_1 < promedio_de_votos_del_jurado_2 and promedio_de_votos_del_jurado_1 < promedio_de_votos_del_jurado_3:
    print(f"El jurado numero 1 es quien puso en promedio las notas mas bajas: {promedio_de_votos_del_jurado_1}")
  elif promedio_de_votos_del_jurado_2 < promedio_de_votos_del_jurado_3:
    print(f"El jurado numero 2 es quien puso en promedio las notas mas bajas: {promedio_de_votos_del_jurado_2}")
  else:
    print(f"El jurado numero 3 es quien puso en promedio las notas mas bajas: {promedio_de_votos_del_jurado_3}")
   


def calcular_sumatoria(matriz:list) -> list:
  """"
    - Suma los votos por columna de una matriz recibida por parámetro.

  Parámetros:
    - fila (list): Una matriz con datos cargados.
    - columna (int) Un número entero que va a representar a cada columna dinámicamente.
  Retorna:
    - La suma total de los elementos por columna.
  """
  coincidencia = False
  numero_ingresado = validar_nota_jurado("Ingrese un número entre 3 y 300: ", "!ERROR¡ El numero debe estar entre 3 y 300. Reingrese un múmero: ", 3, 300)
  for fila in range(len(matriz)):
    if numero_ingresado == sumar_votos_fila(matriz, fila):
      mostrar_lista(matriz[fila])
      coincidencia = True
  if not coincidencia:
    print("¡ERROR! No se encontraron coincidencias...")
    

def calcular_ganador(matriz:list) -> list:
  """"
    - Busca el promedio mas alto entre los participantes para ver si existe un ganador.
    - Guarda en la matriz secundaria (fila_ganador) el primer promedio encontrado en la matriz
      pasada por argumento. Luego, compara el resto de los promedios con el primero encontrado
      Si encuentra un promedio mayor al primero, lo reemplaza.

  Parámetros:
    - fila (list): Una matriz con datos cargados.
  
  Funciones complementarias:
    - calcular_promedio_de_votos()
    - mostrar_ganador()

  """
  bandera = True
  ganador = 0
  fila_ganador = []

  for fila in range(len(matriz)):
    resultado = calcular_promedio_de_votos(matriz, fila)
    if resultado > 0 and bandera == True:
      ganador = resultado
      bandera = False
      fila_ganador = matriz[fila]
    elif resultado > ganador:
      ganador = resultado
      fila_ganador = matriz[fila]
  mostrar_ganador(fila_ganador, ganador)


def mostrar_ganador(fila_ganador:list, ganador:int) -> list:
  """"
    - Muestra por pantalla los resultados que recibe por argumento.

  Parámetros:
    - fila_ganador (list): Contiene la fila con los datos del cocinero ganador.
    - ganador (int): Contiene el promedio de votos que obtuvo el cocinero ganador.
  Retorna:
    - La suma total de los elementos por columna.
  """
  print("EL GANADOR ES:")
  print("--------------")
  mostrar_lista(fila_ganador)
  print(f"PROMEDIO DE VOTOS: {ganador}\n")
  







