#!/usr/bin/python
#-*-coding:utf-8 -*-

miSemana=70
pasaje=1.5
almuerzo=5
gastosU=5.5 #diarios
carrera="Ing. de sistemas"
actividad="Curso de python " #MENTIRA en el almuerzo XD

print "Hola soy omar y tengo ", miSemana, "para toda mi semana"
print "gasto a diario en la universidad %g " %gastosU
print """estudio %s en la UNPRG y actualmente pienso 
en mi %s"""%(carrera,actividad)
print "cuanto gasto en almuerzos a las semana %g" %(5*7)
print 'lo cual es  %g %s de mi semana ' %( ((float(35)/70)*100),'%' )

#para mas info http://docs.python.org/release/2.5.2/lib/typesseq-strings.html