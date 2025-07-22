print("Actividad 08")
opcion = 0

def factorial (n)


while (opcion!=6):
    print("+++Menu+++")
    print("1. Calcular el factorial de un número")
    print("2. Suma de los primeros N números naturales")
    print("3. Calcular el n-ésimo número de Fibonacci")
    print("4. Contar cuántas veces aparece una letra en una palabra")
    print("5.  Invertir una cadena de texto")
    print("6. Calcular la potencia de un número (base^exponente)")
    print("Salir del programa")

    try:
        opcion = int(input("Igrese su Opción: "))
    except ValueError:
        print("\nOpción Invalida... ")
        continue

    match opcion:







