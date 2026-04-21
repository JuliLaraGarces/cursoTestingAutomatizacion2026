#Clase 2, actividad 2: 
#Escribe un pequeño script que utilice un bucle para mostrar los primeros 10 números pares.
#Usa condicionales para validar y mostrar sólo los números pares.

contador = 0
for i in range(10):
  if i % 2 == 0:
    contador += 1
    print(f"{i}")
print(f"Hay {contador} números pares")