numero = 0
simbolo = 0
nombre = 0
categoria = 0
radiactivo = [43,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118]
peso = 0
#Metales Alcalinos = ma
#metales de transicion = mt
#metales alcalinoterreos mat
#metaloide = ml
#semiconductores = sm
#Actinidos = ac
#No Metal = nm
#Halogenos = ha
#lantanidos = la
#Gases Nobles = gn
entra = input(int)
if radiactivo.index(entra) == 0:
    print("Es radiactivo")
else: print("no es")
