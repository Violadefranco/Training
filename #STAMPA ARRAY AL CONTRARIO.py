#STAMPA ARRAY AL CONTRARIO

def main():
    # Definizione e istanziazione dell'array
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Stampa di un valore per riga in ordine inverso
    for value in reversed(array):
        print(value)

if __name__ == "__main__":
    main()