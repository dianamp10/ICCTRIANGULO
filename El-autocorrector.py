def leerArchivo():
    archivo = open("C:\diccito.txt.dic", "r")
    linea = archivo.readline()
    while linea != "":
        print(linea)
        linea = archivo.readline()
    archivo.close()
leerArchivo()
