import math
print("Datos del triángulo rectángulo")
base = 0
altura = 0
perimetro = 0
hipotenusa = 0
base = int(input("Ingrese la base : "))
altura = int(input("Ingrese la altura: "))
hipotenusa = math.sqrt((base**2)+(altura**2))
perimetro = str(base+altura+hipotenusa)
print("     /|")
print(("    / |<-")+(" (")+str(altura)+(")"))
print(("   /<-|---")+(" (")+str(hipotenusa)+(")"))
print(("  /   |"))
print("  ``^``")
print(("   ")+("(")+str(base)+(")"))
print("")
print (str(base * altura / 2) + (" de área"))
print(str(hipotenusa)+(" de hipotenusa"))
print(str(perimetro)+(" de perímetro"))
