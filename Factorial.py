def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def suma_naturales(n):
    if n == 0:
        return 0
    return n + suma_naturales(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def contar_letras(palabra, letra):
    if len(palabra) == 0:
        return 0
    if palabra[0] == letra:
        return 1 + contar_letras(palabra[1:], letra)
    return contar_letras(palabra[1:], letra)


def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    return invertir_cadena(cadena[1:]) + cadena[0]


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


# Menú principal
def menu():
    while True:
        print("\n--- MENÚ RECURSIVO ---")
        print("1. Calcular el factorial de un número")
        print("2. Suma de los primeros N números naturales")
        print("3. Calcular el n-ésimo número de Fibonacci")
        print("4. Contar cuántas veces aparece una letra en una palabra")
        print("5. Invertir una cadena de texto")
        print("6. Calcular la potencia de un número (base^exponente)")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción (1-7): "))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            continue

        match opcion:
            case 1:
                n = int(input("Ingrese un número entero positivo: "))
                if n < 0:
                    print("Debe ser un número positivo.")
                else:
                    print(f"Factorial de {n} es: {factorial(n)}")
            case 2:
                n = int(input("Ingrese un número entero positivo: "))
                if n < 0:
                    print("Debe ser un número positivo.")
                else:
                    print(f"Suma de los primeros {n} números naturales es: {suma_naturales(n)}")
            case 3:
                n = int(input("Ingrese la posición n del número de Fibonacci: "))
                if n < 0:
                    print("Debe ser un número positivo.")
                else:
                    print(f"Fibonacci número {n} es: {fibonacci(n)}")
            case 4:
                palabra = input("Ingrese una palabra: ")
                letra = input("Ingrese una letra a buscar: ")
                if len(letra) != 1:
                    print("Debe ingresar solo una letra.")
                else:
                    cantidad = contar_letras(palabra, letra)
                    print(f"La letra '{letra}' aparece {cantidad} veces en '{palabra}'")
            case 5:
                cadena = input("Ingrese una cadena de texto: ")
                print(f"Cadena invertida: {invertir_cadena(cadena)}")
            case 6:
                base = int(input("Ingrese la base: "))
                exponente = int(input("Ingrese el exponente (positivo): "))
                if exponente < 0:
                    print("El exponente debe ser positivo.")
                else:
                    print(f"{base}^{exponente} = {potencia(base, exponente)}")
            case 7:
                print("Saliendo del programa... 👋")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")


# Ejecutar el menú
menu()
