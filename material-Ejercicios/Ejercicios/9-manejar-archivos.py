from sys import argv
from os.path import exists #inporto este objeto para determinar si un archivo exite 

script, archivo_origen, archivo_destino = argv

print "Copying from %s to %s" % (archivo_origen, archivo_destino)

# Abrimos el archivo de origen 
in_file = open(archivo_origen)
indata = in_file.read()

print "el archivo de origen pesa %d bytes" % len(indata)

print "comprobamos si el archivo de destino existe? %r" % exists(archivo_destino)
print "si el resultado es true ENTER, si no existe presione CTRL - C"
raw_input()
#en caso ingresemos mal el nombre del archivo de salida
#se creara un nuevo archivo con el nombre que le asignemos como variable
out_file = open(archivo_destino, 'w')
out_file.write(indata)

print "Todo correcto :D"

out_file.close()
in_file.close()
