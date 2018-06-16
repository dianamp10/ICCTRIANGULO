def leerArchivo():
    archivo = open("C:\data.txt", "r")
    #Las primeras comillas son la ubicacion de tu archivo 
    linea = archivo.readline()
    while linea != "":
        print(linea)
        linea = archivo.readline()
    archivo.close()
leerArchivo()
