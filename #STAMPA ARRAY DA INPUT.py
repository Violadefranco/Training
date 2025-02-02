#STAMPA ARRAY DA INPUT

def main():
    # Definizione dell'array
    array = []

    # Ciclo per leggere i valori dall'input
    for i in range(10):
        num = int(input(f"Inserisci un numero per l'elemento {i + 1}: "))
        array.append(num)

    # Stampa dei valori inseriti
    print("I numeri inseriti sono:")
    for num in array:
        print(num)

if __name__ == "__main__":
    main()