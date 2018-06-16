def crearArchivo():
    archivo = open("diccito.txt","w")
    archivo.close()
def escribirArchivo():
    archivo = open("diccito.txt","a")
    archivo.write('nuestro\n')
    archivo.write('burbuja\n')
    archivo.write('puesto\n')
    archivo.write('cuido\n')
    archivo.write('corazon\n')
    archivo.write('caracol\n')
    archivo.write('nuesro\n')
    archivo.write('permiso\n')
    archivo.write('casa\n')
    archivo.write('luz\n')
    archivo.close
def leerArchivo():
    archivo = open("diccito.txt","r")
    linea = archivo.readline()
    while linea != "":
        print(linea)
        linea = archivo.readline()
    archivo.close()
leerArchivo()
