from Funciones.granulometria import *
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np


def coeficientes():      
  global Cc                                          
  Cc=float(input("Ingrese el coeficiente de curvatura: "))
  global Cu
  Cu=float(input("Ingrese el coeficiente de uniformidad: ")) 

def limites():                                           
  global Ll
  Ll=float(input("Ingrese el Limite Liquido: "))
  global Lp
  Lp=float(input("Ingrese el limite Plastico: "))
  global Ip
  Ip=Ll-Lp


def clasificacion():
                             
  if granulometria2<=50:  
      print("El suelo esta conformado por su mayoria de material Grueso")
  
      if grava_arena2>50:
        print("El suelo corresponde a una arena (S) ")

        if finos_variable2 < 5 :
          coeficientes()                                          
          print('Arenas limpias')
          if  Cu >=6  and 1 <= Cc <= 3: 
            print('SW - Arena bien graduada')
          elif Cu < 6 and 1 > Cc > 3: 
            print('SP - Arena mal graduada')
          else:
            print('datos erroneos, revise')
        elif 5 < finos_variable2  and finos_variable2  < 12 :
          coeficientes()
          limites()
          print('Arenas limpias con finos')
          if (Cu >= 6 and 1 <= Cc <= 3) and Ip <  4: 
              print ('SW - SM  : Arena  bien graduada con limo')
          elif  (Cu >= 6 and 1 <= Cc <= 3) and Ip > 7 :
              print ('SW - SC  : Arena  bien graduada con arcilla')
          elif (Cu < 6 and 1 > Cc > 3) and Ip <  4 : 
              print ('SP - SM  : Arena  mal graduada con limo')
          elif (Cu < 6 and 1 > Cc > 3) and Ip > 7 :
              print( 'SP - SC : Arena mal graduada con arcilla')     
      else:
        print("El suelo corresponde a una grava (G)")
                          
        if finos_variable2 < 5:  
          coeficientes()
          limites()
          print("Gravas limpias") 
          if (Cu >= 4 and 1 <= Cc <= 3) and Ip <  4: 
            print ('GW - GM  : Grava  bien graduada con limo')
          elif  (Cu >= 4 and 1 <= Cc <= 3) and Ip > 7 :
            print ('GW - GC  : Grava  bien graduada con arcilla')
          elif (Cu < 4 and 1 > Cc > 3) and Ip <  4 : 
            print ('GP - GM  : Grava  mal graduada con limo')
          elif (Cu < 4 and 1 > Cc > 3) and Ip > 7 :
            print( 'GP - GC : Grava mal graduada con arcilla')                                        
                                                          
        elif finos_variable2 < 12 and finos_variable2 > 5:
          print('Gravas limpias con finos')
          coeficientes()
          limites()
          if (Cu >= 4 and 1 <= Cc <= 3) and Ip <  4: 
            print ('GW - GM  : Grava  bien graduada con limo')
          elif  (Cu >= 4 and 1 <= Cc <= 3) and Ip > 7 :
            print ('GW - GC  : Grava  bien graduada con arcilla')
          elif (Cu < 4 and 1 > Cc > 3) and Ip <  4 : 
            print ('GP - GM  : Grava  mal graduada con limo')
          elif (Cu < 4 and 1 > Cc > 3) and Ip > 7 :
            print( 'GP - GC : Grava mal graduada con arcilla')
        
            
          else:
            print('Gravas con finos')
            limites()
            coeficientes()
            if Cc!=0 and Ll!=0:
              if Cu>4 and 1<=Cc<=3:
                if Ip<0.79*(Ll-20) or Ip<4:
                  print("El suelo es una grava graduada con particulas de limo(GW-GM)")
                else:
                  print("El suelo es una grava graduada con particulas de arcilla(GW-GC)") 
              else:
                if Ip<0.79*(Ll-20) or Ip<4:
                  print("El suelo es una grava pobremente graduada con particulas de limo (GP-GM)")
                else:
                  print("El suelo es una grava pobremente graduada con particulas de arcilla(GP-GC)")
            elif Cu!=0:
              if Cu>6 and 1<=Cc<=3:
                print("El suelo es un grava graduada(GW)")
              else:
                print("El suelo es un grava pobremente graduada(GP)")
            elif Ll!=0:
              if Ip<0.79*(Ll-20) or Ip<4:
                print("El suelo es una grava limosa (GM)")
              else:
                print("El suelo es una grava arcillosa(GC)")
  else:
    print("carta de plasticidad")
