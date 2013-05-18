#!/usr/bin/python
#-*-coding:utf-8 -*-
formato = "%r %r %r %r"

print formato % (1, 2, 3, 4)
print formato % ("uno", "dos", 3, 4)
print formato % (True, False, False, True)
print formato % (formato, formato, formato, formato)
print formato % (
    "Hola mundo",
    "hello world",
    "ola ke ase",
    "Bonjour tout le monde" #french :p
)