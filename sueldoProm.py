# Defino la funcion para calcular el promedio
def calcular_promedio_sueldo(sueldos):
    total_sueldos = sum(sueldos)
    promedio = total_sueldos / len(sueldos)
    return promedio

#Defino la funcion para categorizar el sueldo
def categorizar_sueldo(sueldo):
    if sueldo < 300:
        return "Sueldo bajo"
    elif sueldo <= 900:
        return "Sueldo normal"
    else:
        return "Sueldo mejor de lo normal"

# Todos los sueldos de Juan los meses
sueldos_mensuales = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

# Llamo a la funcion para calcular el sueldo promedio de Juan
sueldo_promedio = calcular_promedio_sueldo(sueldos_mensuales)

# Redondear el promedio a dos decimales
sueldo_promedio_redondeado = round(sueldo_promedio, 2)

# Llamo a la funcion para categorizar el sueldo de Juan
categoria_sueldo = categorizar_sueldo(sueldo_promedio)

# Imprimo y muestro los resultados
print("Sueldos mensuales de Juan:", sueldos_mensuales)
print("Sueldo promedio de Juan:", sueldo_promedio_redondeado, "dólares")
print("Categoría de sueldo de Juan:", categoria_sueldo)
