from os import system
import time
from operations import Operations
import sys

def main_menu():
    system('cls')  
    opt = ""
    oper = Operations()
    while opt != "s":
        print("\033[96m-" * 22)
        print("|| Menú de opciones ||")
        print("-" * 22 + "\033[97m")
        print("1. Suma naturales iterativo")
        print("2. Suma naturales Gauss")
        print("3. Búsqueda secuencial")
        print("4. Búsqueda binaria")
        print("5. Ordenamientos (burbuja, selección e inserción)")
        print("S. Salir")
        opt = input("Ingrese su opción: ").lower()

        match opt:
            case "1":
                n = int(input("Ingrese n: "))
                start = time.time()
                print(f"Suma de 1 a {n} iterativo: {oper.sumNaturalsIterative(n)} ")
                end = time.time()
                print(f"Tiempo ejecución: {end - start:.6f} segundos")
            case "2":
                n = int(input("Ingrese n: "))
                start = time.time()
                print(f"Suma de 1 a {n} Gauss: {oper.sumNaturalsGauss(n)} ")
                end = time.time()
                print(f"Tiempo ejecución: {end - start:.6f} segundos")
            case "3":
                n = int(input("Ingrese n: "))
                valor = int(input("Valor a buscar: "))
                arr = list(range(1, n + 1))

                start = time.time()
                pos = oper.sequentialSearch(arr, valor)
                end = time.time()

                if pos != -1:
                    print(f"Valor encontrado en la posición {pos}")
                else:
                    print("Valor no encontrado")

                print(f"Tiempo ejecución: {end - start:.6f} segundos")

                #Tiempos
                tiempos = []

                # Mejor caso
                start = time.time()
                oper.sequentialSearch(arr, arr[0])
                end = time.time()
                tiempos.append(end - start)

                # Promedio
                start = time.time()
                oper.sequentialSearch(arr, arr[n // 2])
                end = time.time()
                tiempos.append(end - start)

                # Peor caso
                start = time.time()
                oper.sequentialSearch(arr, -1)
                end = time.time()
                tiempos.append(end - start)

                print(f"\nmin  = {min(tiempos):.6f} s")
                print(f"prom = {sum(tiempos)/len(tiempos):.6f} s")
                print(f"max  = {max(tiempos):.6f} s")

                # Medicion de memoria
                memoria_total = sys.getsizeof(arr) + sum(sys.getsizeof(x) for x in arr)
                memoria_mb = memoria_total / (1024 ** 2)
                print(f"\nMemoria utilizada por el arreglo: {memoria_mb:.2f} MB")

            case "4":
                n = int(input("Ingrese n: "))
                valor = int(input("Valor a buscar: "))
                arr = list(range(1, n + 1))

                start = time.time()
                pos = oper.binarySearch(arr, valor)
                end = time.time()

                if pos != -1:
                    print(f"Valor encontrado en la posición {pos}")
                else:
                    print("Valor no encontrado")

                print(f"Tiempo ejecución: {end - start:.6f} segundos")
                
                #Tiempos
                tiempos = []

                # Mejor caso
                start = time.time()
                oper.binarySearch(arr, arr[n // 2])
                end = time.time()
                tiempos.append(end - start)

                # Promedio caso
                start = time.time()
                oper.binarySearch(arr, arr[n // 4])
                end = time.time()
                tiempos.append(end - start)

                # Peor caso
                start = time.time()
                oper.binarySearch(arr, -1)
                end = time.time()
                tiempos.append(end - start)

                print(f"\nmin  = {min(tiempos):.6f} s")
                print(f"prom = {sum(tiempos)/len(tiempos):.6f} s")
                print(f"max  = {max(tiempos):.6f} s")

                 # Medicion de memoria
                memoria_total = sys.getsizeof(arr) + sum(sys.getsizeof(x) for x in arr)
                memoria_mb = memoria_total / (1024 ** 2)
                print(f"\nMemoria utilizada por el arreglo: {memoria_mb:.2f} MB")

            case "5":
                n = int(input("Ingrese n: "))
                base = list(range(n, 0, -1)) 
                tiempos = []

                # Burbuja
                arr = base.copy()
                start = time.time()
                oper.bubbleSort(arr)
                end = time.time()
                t_burbuja = end - start
                print(f"Burbuja: {t_burbuja:.6f} segundos")
                tiempos.append(t_burbuja)

                # Insercion
                arr = base.copy()
                start = time.time()
                oper.insertionSort(arr)
                end = time.time()
                t_insercion = end - start
                print(f"Insercion: {t_insercion:.6f} segundos")
                tiempos.append(t_insercion)

                # Seleccion
                arr = base.copy()
                start = time.time()
                oper.selectionSort(arr)
                end = time.time()
                t_seleccion = end - start
                print(f"Seleccion: {t_seleccion:.6f} segundos")
                tiempos.append(t_seleccion)

                print(f"\nmin  = {min(tiempos):.6f} s")
                print(f"prom = {sum(tiempos)/len(tiempos):.6f} s")
                print(f"max  = {max(tiempos):.6f} s")

                # Medicion de memoria
                memoria_total = sys.getsizeof(arr) + sum(sys.getsizeof(x) for x in arr)
                memoria_mb = memoria_total / (1024 ** 2)
                print(f"\nMemoria utilizada por el arreglo: {memoria_mb:.2f} MB")



            case "s":
                print("Programa finalizado")
            case _:
                print("Opción no válida")

if __name__ == '__main__':
    main_menu()
