from operaciones import sumar, restar, multiplicar, dividir

def ejecutar_calculadora():
    print("⋆⭒˚.⋆ Calculadora ⋆⭒˚.⋆")
    
    try:
        # Solicitamos los números al usuario y los convertimos a float
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        print("\n¿Qué querés calcular hoy?")
        print("------------")
        print("|1. Sumar\n|2. Restar\n|3. Multiplicar\n|4. Dividir")
        print("------------")
        opcion = input("Seleccioná (1/2/3/4): ")

        # Lógica de decisión según la opción elegida
        if opcion == '1':
            resultado = sumar(num1, num2)
            simbolo = "+"
        elif opcion == '2':
            resultado = restar(num1, num2)
            simbolo = "-"
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            simbolo = "*"
        elif opcion == '4':
            resultado = dividir(num1, num2)
            simbolo = "/"
        else:
            print("Opción no válida.")
            return

        # Mostramos el resultado final
        print(f"\nEl resultado de {num1} {simbolo} {num2} es: {resultado} ⋆˚✰ ݁˖⭑")

    except ValueError:
        # Se ejecuta si el usuario ingresa texto en lugar de números
        print("Error: Entrada inválida. Por favor, ingresa solo números.")
    
    except ZeroDivisionError as e:
        # Se ejecuta si el segundo número es cero en una división
        print(f"Error: {e}")
    
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_calculadora()