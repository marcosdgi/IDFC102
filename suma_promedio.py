def main():
    numero = 1
    numero2 = 2 
    numero3 = 3
    
    numero = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))
    
    suma = numero + numero2 + numero3
    promedio = suma / 3
    print("La suma es:", suma)
    print("El promedio es:", promedio)
    
if __name__ == "__main__":
    main()