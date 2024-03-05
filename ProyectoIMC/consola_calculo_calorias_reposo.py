# -*- coding: utf-8 -*-

import calculadora_indices as calc

print("En esta función se va calcular la cantidad de calorías que una persona quema estando en reposo (esto es, su tasa metabólica basal)")
print("     ") 


peso=float(input("Ingrese el peso de la persona (en kilogramos ) : "))
altura=float(input("Ingrese la altura de la persona (en centímatros) :"))
edad=int(input("Ingrese la edad de la persona (en años) :"))
valor_genero=float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer :"))

reposo=calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)

print("     ") 
print("     ") 

print("-- La cantidad de calorías que la persona quema en reposo es :",reposo) 




