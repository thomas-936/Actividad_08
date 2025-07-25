print("Actividad 08")
opcion = 0

def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n+1):
            resultado *= i
        return  resultado

def suma_naturales(n):
    if n == 0:
        return 0
    else:
        suma = 0
        for i in range(n, 0, -1):
            suma+=i
        return suma

def fibo (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n+2):
            a, b = b, a+ b
            return b

while (opcion!=7):
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
        case 1:
            print("**Calcular factorial**")
            numero = int(input("\nIngrese un número para calcuñar su factorial: "))
            if numero <= 0:
                print("El número ingresado no debe ser negativo: ")
            else:
                print(f"El factoroal del número {numero} es {factorial(numero)}")

        case 2:
            print("++Suma de los primero N números naturales++")
            num = int(input("Ingrese un número natural: "))
            if num < 0:
                print("El ingreso debe ser un número natural (positivo)")
            else:
                print(f"La suma de los numero naturales hasta {num} es {suma_naturales(num)} ")

        case 3:
            print("***Calular el factorial de un número n***")
            numero_fibo = int(input("Ingrese un número n: "))
            if numero_fibo < 0:
                print("El ingreso debe ser un número positivo: ")
            else:
                print(f"El fibonacci de {numero_fibo} es {fibo(numero_fibo)}")
