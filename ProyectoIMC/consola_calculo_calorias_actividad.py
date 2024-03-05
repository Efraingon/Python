import calculadora_indices as calc

print("En esta función  va a calcular la cantidad de calorías que una persona quema al realizar algún tipo de actividad física")
print("     ") 

peso=float(input("Ingrese el peso de la persona (en kilogramos ) : "))

altura=float(input("Ingrese la altura de la persona (en centímatros) :"))
edad=int(input("Ingrese la edad de la persona (en años) :"))
valor_genero=float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer :"))
print("")
print("")

mensaje='Ingrese actividad física semanal(1.2: poco o ningún ejercicio,\n '
mensaje= mensaje + '1.375: ejercicio ligero (1 a 3 días a la semana),\n'
mensaje= mensaje + '1.55: ejercicio moderado (3 a 5 días a la semana),\n'
mensaje= mensaje + '1.725: deportista (6 -7 días a la semana),\n'
mensaje= mensaje + '1.9: atleta (entrenamientos mañana y tarde),\n'
mensaje= mensaje + '):'

valor_actividad=float(input(mensaje))
actividad=calc.calcular_calorias_en_actividad(peso,altura,edad,valor_genero,valor_actividad)

print("     ") 
print("     ") 

print("-- La cantidad de calorías que quema al realizar algún tipo de actividad física semanalmente es:",round(actividad,2)) 



