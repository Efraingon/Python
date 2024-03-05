# -*- coding: utf-8 -*-
import calculadora_indices as calc

print("En esta función se va calcular la cantidad de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar")
print("     ") 

peso=float(input("Ingrese el peso de la persona (en kilogramos ) : "))

altura=float(input("Ingrese la altura de la persona (en centímatros) :"))
edad=int(input("Ingrese la edad de la persona (en años) :"))
valor_genero=float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer :"))
print("     ") 
print("     ") 
print(str(calc.consumo_calorias_recomendado_para_adelgazar(peso,altura,edad,valor_genero)))



