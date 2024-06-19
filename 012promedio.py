#calcula y muestra el promedio de un alumno
print('El programa calcula el promedio de 3 calificaciones de un alumno: ')
nombre=input('Escribe tu nombre: ')
mat= float(input('Escribe tu Calif. de Matematicas: '))
fis =float(input('Escribe tu Calif. de Fisica: '))
quim=float(input('Escribe tu Calif. de Quimica: '))

prom=(mat+fis+quim)/3
if(prom<6):
    print(f'{nombre} tu calificacion es : {round(prom,2)} Desaprobado')
else:
    print(f'{nombre} tu promedio es : {round(prom,2)} Aprobado')