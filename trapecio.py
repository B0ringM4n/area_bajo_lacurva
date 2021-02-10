import math
import os
a=0 
b=0
fa=0
fb=0
fab=0
cen=0 
resultado=[]
actual=0 
anterior=0
intervalo=0
valorE=0 
constante=[]
ecu=0
numPartes=0
area=0
def ecuacion(y,d,e,f,g,h,i,j,varx):
 	valorE=((j*(varx**7))+(i*(varx**6))+(h*(varx**5))+(g*(varx**4))+(f*(varx**3))+(e*(varx**2))+(d*varx)+y)
 	return valorE
 
print("Hola esto saca area de un trapecio bajo una curva")
print("")
print("ingrese las constantes para un polinomio de grado 7")
constante.append(float(input("ingresa la constante C: ")))
constante.append(float(input("ingresa contante para x: ")))
constante.append(float(input("ingresa cons. para x2: ")))
constante.append(float(input("ingresa cons. para x3: ")))
constante.append(float(input("ingresa cons. para x4: ")))
constante.append(float(input("ingresa cons. para x5: ")))
constante.append(float(input("ingresa cons. para x6: ")))
constante.append(float(input("ingresa cons. para x7: ")))
print("")
os.system('cls')
a=float(input("ingresa el punto de inicio"))
b=float(input("ingresa el punto final"))
numPartes=int(input("ingresa el numero de partes a dividir "))
intervalo=(b-a)/numPartes
cen=a
while cen<=b :
    resultado.append(ecuacion(constante[0],constante[1],constante[2],constante[3],constante[4],constante[5],constante[6],constante[7],cen))
    cen +=intervalo
for i in range(numPartes):
    area += ((resultado[i]+resultado[i+1])*intervalo)/2

print("El area total es: "+str(area))
    
pausa=input()
os.system('cls')
