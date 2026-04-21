#Clase 2, actividad 1: 
#Define variables para almacenar el nombre, edad y profesión del usuario.
#Solicita estos datos por teclado utilizando input().
#Imprime en pantalla un mensaje personalizado incluyendo todos estos datos.

#Paso 1, definir las variables e inicializarlas
nombre = '';
edad = '';
profesion_usuario = '';

#Paso 2, solicitar por pantalla la información
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
profesion_usuario = input("¿Cuál es tu profesion? ")

#Paso 3, Imprimir la información guardada
print(f"Hola {nombre}, tu edad es {edad} y tu profesión es {profesion_usuario}")
