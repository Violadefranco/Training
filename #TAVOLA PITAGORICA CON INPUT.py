#TAVOLA PITAGORICA CON INPUT

def main():
    # Chiede all'utente di inserire il valore di n
    n = int(input("Inserisci un numero per generare la tavola pitagorica: "))

    # Genera la tavola pitagorica
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")  # Stampa il prodotto con spaziatura per allineare
        print()  # A capo per ogni riga

if __name__ == "__main__":
    main()