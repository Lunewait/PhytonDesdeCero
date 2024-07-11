#Extraer cadenas  cadena[start: end]
proverb = 'Agua pasada no mueve molino?'
print(proverb[:]) #Genera una copia del arreglo anterior
print(proverb[12:])#Extrae desde de la posicion 12 hasta el final de la cadena
print(proverb[:11])#Extrae desde el comienzo de la cadena hastan la posicion 11 menos 1 
print(proverb[5:11])#Extrae desde la posicion 5 hasta la posicion 11 menos 1(seria posicion 10)
print(proverb[5:11:2])#Extrae desde la posicion 5 hasta la posicion 11 menos 1(seria posicion 10) hace un salto de 2 posiciones
#Longitud de la Cadena
print(len(proverb))
#Pertenencia de un elemento
#solo utilizamos el conector in
print('Agua'in proverb)
print('Luna'in proverb)
#como sabemos si una subcadena esta en la cadena
print(not('Porque'in proverb))
#Dividir una cadena-- split(parametro)
print(proverb.split())
tools = 'Martillo,Sierra,Destornillador'
print(tools.split(','))
#Split nos devuelve variables tipos List
game = 'Piedra-Papel-Tijera'
print(type(game.split('-')))
#Utilizaremos la funcion partition
text = 'luna + sol'
print(text.partition('+'))
#Limpiar cadenas--(l,r)strip
serial_number = '\n\t  \n 4874983274832 \n\n\t \t \n'
print(serial_number.strip())#Eliminara cualquier espacio por defecto
print(serial_number.lstrip())#Eliminara el lado izquierda
print(serial_number.rstrip('\n'))#Eliminara el lado derecho
#Realizar busquedas --(end,star)swith()--find, index, count
lyrics = '''Quizas  porque mi niñez
Sigue jugando en tu vida
Y escondido tras las cañas
Duerme mi primer amor
Llevo tu luz y tu olor
Por dondequieras que vaya'''
print(lyrics.startswith('Quizas'))
print(lyrics.endswith('Final'))
print(lyrics.find('amor'))
print(lyrics.index('amor'))
print(lyrics.count('mi'))#Contador de cuantas veces aparece la letra mi
#Remplazar valores ---replace()
music = 'Quien mal anda mal acaba'
print(music.replace('mal','bien'))
print(music.replace('mal','bien',1))#remplaze una vez
#Mayusculas y minusculas
light ='quien a buen árbol se arrima Buena sombra le cobija'
print(light.capitalize())
print(light.title())#Mayusculas a todos las iniciales de las palabras
print(light.upper())#mayusculas a todas las palabras
print(light.lower())#minusculas a todas las palabras
print(light.swapcase())#convierte de mayusculas a minusculas y viceversa
#Identificar caracteres
print('R2D2'.isalnum())#Detectar si todos son numeros o letras
print('C3-P0'.isalnum())
print('314'.isnumeric())#Detectar si todos  los valores son numeros
print('3.14'.isnumeric())
print('Hola'.isalpha())#Detectar si todos son carecteres
print('h-o-l-a'.isalpha())
print('BIG'.isupper())#Si hay mayusculas
print('small'.islower())#si hay minusculas
print('First Heading'.istitle())#Si las palabras comienzan con mayusculas




