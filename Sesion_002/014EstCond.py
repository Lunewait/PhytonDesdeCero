#el programa evaluara la estatura del ususario y
#si la estatura es menor que 160cms imprimira : Eres chaparrito
#Si la estatura es entre 160 cms y entre 175 cms imprimira: Eres de estatura mediana
#Si la estatura es mayor a 175 cms imprimira : Eres alto
nombre= input("Escribe tu nombe: ")
estatura=int (input("Escribe tu estatura en cm: "))

if estatura<160:
    print(f'{nombre} Eres chaparrito....')
if (estatura>=160 and estatura<=175) :
    print(f'{nombre} Eres mediano.....')
if(estatura>=175):
    print(f'{nombre} Eres alto....')