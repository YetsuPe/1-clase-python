#!/usr/bin/python
#-*-coding:utf-8 -*-
from sys import argv

nombre_fichero, archivo_texto= argv
texto=open(archivo_texto)
print "el nombre del archivo a leer es : %r"%archivo_texto
print texto.read()
print "ahora ingrese el siguiente archivo a leer"
nuevo_texto_nombre=raw_input()
nuevo_texto=open(nuevo_texto_nombre)
print "Contenido ====== %r%s"%(nuevo_texto.read(),"=====" )
