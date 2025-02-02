#BATTAGLIA NAVALE

def stampa_matrice(matrix):
    # Funzione per stampare una matrice 10x10
    for row in matrix:
        print(" ".join(f"{cell:4}" for cell in row))

def main():

    # Creazione della matrice 10x10
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    shots = 10  # Numero di colpi consentiti

    # Posizionamento dei sommergibili
    matrix[1][2] = 1  # sommergibile 1
    matrix[3][4] = 1  # sommergibile 2
    matrix[5][6] = 1  # sommergibile 3
    matrix[7][8] = 1  # sommergibile 4
    matrix[9][0] = 1  # sommergibile 5

    # Stampa iniziale della matrice con sommergibili piazzati
    print("Matrice con sommergibili piazzati:")
    stampa_matrice(matrix)
    print()

    # Ciclo che consente al giocatore di sparare 10 colpi
    for k in range(shots):
        try:
            r, c = map(int, input(f"Inserisci le coordinate (riga colonna) per il colpo {k + 1}: ").split())
        except ValueError:
            print("Input non valido. Inserisci due numeri separati da uno spazio.")
            continue

        # Controllo della validità delle coordinate inserite
        if 0 <= r < 10 and 0 <= c < 10:
            if matrix[r][c] == 1:
                print("Colpito!")
                matrix[r][c] = 2  # Indica un colpo riuscito
            elif matrix[r][c] == 0:
                print("Acqua!")
                matrix[r][c] = -1  # Indica un colpo in acqua
            elif matrix[r][c] == 2 or matrix[r][c] == -1:
                print("Hai già sparato qui. Riprova.")
                continue
        else:
            print("Coordinate non valide. Riprova.")
            continue

        # Stampa della matrice aggiornata dopo ogni colpo
        print(f"\nMatrice aggiornata dopo il colpo {k + 1}:")
        stampa_matrice(matrix)
        print()

    print("Hai finito i 10 colpi!")

if __name__ == "__main__":
    main()