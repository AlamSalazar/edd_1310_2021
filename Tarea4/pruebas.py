import csv
from arrays import Array

with open('junio.dat', encoding='utf-8-sig') as data: #Lea el archivo
	entrada=list(csv.reader(data, delimiter=','))

trabajadores = Array(len(entrada)-1)
for x in range(trabajadores.get_length()):
  trabajadores.set(entrada,x)
old=0
new=10
for x in range(1,trabajadores.get_length()):
    horasExtra = 276.5*int(trabajadores.get_horasExtra(x))
    antiguedad = 2020-int(trabajadores.get_anoIngreso(x))
    pago = antiguedad *( (int(trabajadores.get_sueldoBase(x))/100)*3 ) + int(trabajadores.get_sueldoBase(x))
    print(f"Trabajador [{x}]\t-> {trabajadores.get_nTrabajador(x)} {trabajadores.get_nombre(x)} {trabajadores.get_paterno(x)} {trabajadores.get_materno(x)} {horasExtra} {pago} {trabajadores.get_anoIngreso(x)}")
    
    
    if antiguedad >= old:
      old = antiguedad
      viejon=x
    if antiguedad <= new:
      new = antiguedad
      niño=x

print("---------------------------------------------------------------------")
print(f"El trabajador más viejo es el trabajador {trabajadores.get_nombre(viejon)} {trabajadores.get_paterno(viejon)} (numero {viejon}) con {old} años de antiguedad")
print(f"El trabajador más nuevo es el trabajador {trabajadores.get_nombre(niño)} {trabajadores.get_paterno(niño)} (numero {niño}) con {new} años de antiguedad")

    




