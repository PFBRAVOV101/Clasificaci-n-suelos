import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

def granulometria():

  #Abertura malla de tamiz en (in)
  Tamiz = pd.Series([
        "1 1/2",
        "1" ,
        "3/4",
        "3/8", 
        "#4" ,
        "#10",
        "#20",
        "#30",
        "#40",
        "#60",
        "#100",
        "#140",
        "#200",
        "Fondo"
  ])

  #Abertura malla de tamiz en (mm)

  abertura = pd.Series([
        37.5, #tamiz de 1 1/2"
        25, #tamiz de 1"
        19, #tamiz de 3/4"
        9.5, #tamiz de 3/8"
        4.75 , #tamiz # 4
        2.00 , #tamiz # 10
        0.85 , #tamiz # 20
        0.60, #tamiz # 30
        0.425 , #tamiz # 40
        0.25 , #tamiz # 60
        0.150 , #tamiz # 100
        0.106 ,#tamiz # 140
        0.075 , #tamiz # 200
        0, #fondo
  ])

  #retenido en cada tamiz

   # Retenido en cada tamiz
  retenido = []
  for i in range(len(Tamiz)):
    ret = float(input(f"Ingrese el valor retenido en el tamiz {Tamiz[i]}: "))
    retenido.append(ret)
  retenido = pd.Series(retenido)
  # Sumatoria del peso retenido en cada tamiz
  peso_retenido =retenido.sum()
  peso_retenido

  #Tabla con datos sumistrados y acumulado de los retenido
  global Tabla
  Tabla = pd.DataFrame({
      'Tamiz': Tamiz,
      'Abertura' : abertura,
      'Retenido' : retenido,
  })

  # acumulado de los retenido
  Tabla['Retenido acumulado'] = Tabla['Retenido'].cumsum()

  #Cantidad que pasa 
  Tabla['pasa'] = retenido.sum() - Tabla['Retenido acumulado']
  Tabla

  # % que pasa
  Tabla['% pasa'] = (Tabla['pasa'] / retenido.sum()) * 100
  Tabla
  print(Tabla)

  granulometria=Tabla[Tabla["Abertura"]==0.075 ]["% pasa"] 
  global granulometria2
  granulometria2=float(granulometria)   

  grava_arena=Tabla[Tabla["Abertura"]==4.75 ]["% pasa"]
  global grava_arena2
  grava_arena2=float(grava_arena) 

  finos_variable=Tabla[Tabla["Abertura"]==0.075 ]["% pasa"]
  global finos_variable2
  finos_variable2=float(finos_variable)  


 # Crear figura y ejes
  fig, ax = plt.subplots()

  # Graficar curva granulométrica
  ax.plot(Tabla['Abertura'], Tabla['% pasa'], linestyle='--', marker='o', label='Curva granulométrica')

  # Configurar ejes y título
  ax.set_xlabel('Abertura en (mm)')
  ax.set_ylabel('% que pasa')
  ax.grid(True, which='both')
  ax.legend()
  ax.invert_xaxis()
  ax.set_title('Curva Granulométrica')

  # Mostrar gráfico
  plt.show()

granulometria()
