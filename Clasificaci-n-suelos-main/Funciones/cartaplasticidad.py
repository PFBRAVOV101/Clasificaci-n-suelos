import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

def calcular_IP(Ll):
    IP = 0.73 * (Ll - 20)
    return IP

def LLH(Ip):
    LLH = Ip / 0.73 + 20
    return LLH

def LLH2(Ip):
    LLH2 = Ip / 0.9 + 8
    return LLH2

def LLHI(IPHI):
    LLHI = IPHI / 0.73 + 20
    return LLHI

def LLHI1(IPHI):
    LLHI1 = IPHI / 0.9 + 8
    return LLHI1

def LLU(Ll):
    LLU = 0.9 * (Ll - 8)
    return LLU

def cartadeplasticidad():
    # Línea vertical
    lineaV = np.array([57, 0])
    lineaV1 = np.array([50, 50])
    plt.plot(lineaV1, lineaV, "b", label="")

    # Línea A
    LLmax = 100
    LLmin = 20
    IPmax = calcular_IP(LLmax)
    IPmin = calcular_IP(LLmin)
    lineaA = np.array([IPmin, IPmax])
    lineaA1 = np.array([LLmin, LLmax])
    plt.plot(lineaA1, lineaA, "grey", label="línea A")

    # Línea límite horizontal superior
    IPH = 7
    LLHmax = LLH(IPH)
    LLHmin = LLH2(IPH)
    lineaH = np.array([IPH, IPH])
    lineaH1 = np.array([LLHmin, LLHmax])
    plt.plot(lineaH1, lineaH, "red", label="")

    # Línea límite horizontal inferior
    IPHI = 4
    LLHImax = LLHI(IPHI)
    LLHImin = LLHI1(IPHI)
    lineaH = np.array([IPHI, IPHI])
    lineaH1 = np.array([LLHImin, LLHImax])
    plt.plot(lineaH1, lineaH, "y", label="")

    # Línea límite U
    LLUmax = 73
    LLUmin = 8
    LLU1 = LLU(LLUmax)
    LLU2 = LLU(LLUmin)
    lineaU = np.array([LLU1, LLU2])
    lineaU1 = np.array([LLUmax, LLUmin])
    plt.plot(lineaU1, lineaU, "m", ls='dashdot', label="línea U")

    # Gráfico
    plt.text(20, 40, "NO EXISTE", fontsize=8, fontweight='bold')
    plt.text(40, 20, "CL", fontsize=8, fontweight='bold')
    plt.text(18, 4.8, "CL-ML", fontsize=8, fontweight='bold')
    plt.text(65, 40, "CH", fontsize=8, fontweight='bold')
    plt.text(40, 5, "ML", fontsize=8, fontweight='bold')
    plt.text(65, 5, "MH", fontsize=8, fontweight='bold')
    plt.text(80, 40, "Línea A", fontsize=8, fontweight='bold', rotation=37)
    plt.text(65, 5, "MH", fontsize=8, fontweight='bold')
    plt.text(80, 40, "Línea A", fontsize=8, fontweight='bold', rotation=37)
    plt.text(65, 48, "Línea U", fontsize=8, fontweight='bold', rotation=41)

    global Ll
    Ll=float(input("Ingrese el Limite Liquido: "))
    global Lp
    Lp=float(input("Ingrese el limite Plastico: "))
    global Ip
    Ip=Ll-Lp

    plt.title("CARTA DE PLASTICIDAD", fontsize=10)
    plt.xlabel("LIMITE LIQUIDO", fontsize=10)
    plt.ylabel("INDICE DE PLASTICIDAD", fontsize=10)
    plt.scatter( Ll,Ip, lw =4, alpha = 0.5 )
    plt.legend()
    plt.grid(color="grey", ls = "dashdot", lw =1, alpha = 0.5)
    plt.show()
