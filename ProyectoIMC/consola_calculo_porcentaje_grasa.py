# -*- coding: utf-8 -*-
import calculadora_indices as calc

print("En esta función se va calcular el porcentaje de grasa de una persona")
print("     ") 


peso=float(input("Ingrese el peso de la persona (en kilogramos ) : "))
altura=float(input("Ingrese la altura de la persona (en metros) :"))
edad=int(input("Ingrese la edad de la persona (en años) :"))
valor_genero=float(input("Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer :"))

grasa=calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print("     ") 
print("     ") 

print("-- El porcentaje de grasa que tiene el cuerpo es :",round(grasa,2)) 

