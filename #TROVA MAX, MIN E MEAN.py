#TROVA MAX, MIN E MEAN

def main():
    # Leggi la dimensione dell'array
    n = int(input("Inserisci il numero di elementi dell'array: "))

    # Crea un array di dimensione n
    arr = []

    # Inserisci n elementi nell'array
    print(f"Inserisci {n} numeri interi:")
    for i in range(n):
        num = int(input(f"Elemento {i + 1}: "))
        arr.append(num)

    # Trova il massimo, il minimo e calcola la somma
    max_val = max(arr)
    min_val = min(arr)
    somma = sum(arr)  # Calcolo della somma

    # Calcola la media
    media = somma / n

    # Stampa il massimo, il minimo e la media
    print(f"Il valore massimo è: {max_val}")
    print(f"Il valore minimo è: {min_val}")
    print(f"La media è: {media:.2f}")

if __name__ == "__main__":
    main()