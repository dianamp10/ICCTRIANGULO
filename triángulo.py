# Crear una calculadora de triángulos rectángulos
import math
print("Datos del triángulo rectángulo")
# Crear variables tipo,base,altura,perímetro,hipotenusa
base = 0
perimetro = 0
hipotenusa = 0
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: ")
hipotenusa = math.sqrt((base*2)+(altura*2))
perimetro = str(base + altura + hipotenusa)
#hacer un triángulo graficamente
#con símbolos         
print("     /|")
print(("    / |<-")+(" (")+str(altura)+(")"))
print(("   /<-|---")+(" (")+str(hipotenusa)+(")"))
print(("  /   |"))
print("  ``^``")
print(("   ")+("(")+str(base)+(")"))
print("")
print(str(base*altura/2) + ("de area"))
