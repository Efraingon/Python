# -*- coding: utf-8 -*-
import calculadora_indices as calc

print("En esta función se va calcular el índice de masa corporal de una persona a partir de la ecuación definida anteriormente")
print("     ") 
peso=float(input("Ingrese el peso de la persona (en kilogramos ) : "))
altura=float(input("Ingrese la altura de la persona (en Metros) :"))
imc=calc.calcular_IMC(peso, altura)

print("     ") 
print("     ") 

print("-- Índice de masa corporal de la persona :",round(imc,2)) 


