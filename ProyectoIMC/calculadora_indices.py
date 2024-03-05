def calcular_IMC(peso:float, altura:float):
    return float(peso/(altura**2))

def calcular_porcentaje_grasa(peso:float,altura:float, edad:int,valor_genero:float):
    imc=calcular_IMC(peso,altura)
    porcentaje =float((1.2*imc)+(0.23*edad)-5.4-valor_genero)
    return porcentaje

def calcular_calorias_en_reposo(peso:float,altura:float,edad:int,valor_genero:float):
    
    tmb = (10*peso)+(6.25*altura)-(5*edad)+ valor_genero
    return tmb
    
def calcular_calorias_en_actividad(peso:float,altura:float,edad:int,valor_genero:float,valor_actividad:float):
    tmb= calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    actividad_fisica =float(tmb*valor_actividad)
    return actividad_fisica
def consumo_calorias_recomendado_para_adelgazar(peso:float,altura:float,edad:int,valor_genero:float):
    mensaje=""
    
    tmb= calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    xxx= float(tmb * 15.00)/100.00
    xxx=tmb - xxx
    zzz= float(tmb * 20.00)/100.00
    zzz=tmb - zzz
    
    
    
    mensaje = '-- Para adelgazar es recomendado que consumas entre: ' + str(round(zzz,2)) + ' y ' + str(round(xxx,2)) + ' calorías al día.'
    return mensaje   


    


