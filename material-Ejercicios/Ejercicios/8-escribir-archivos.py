#!/usr/bin/python
#-*-coding:utf-8 -*-
archivo_texto = open('texto.txt', 'w') #w escribir #r leer y #a ambos

print "Truncando el archivo"
archivo_texto.truncate()

print "ahora escribimos"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "ingresamos el contenido"

archivo_texto.write(line1)
archivo_texto.write("\n")
archivo_texto.write(line2)
archivo_texto.write("\n")
archivo_texto.write(line3)
archivo_texto.write("\n")

print "y finalmente cerramos"
archivo_texto.close()