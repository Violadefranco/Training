#ORDINA IN MODO CRESCENTE

def main():
    a = 100  # Prima variabile intera
    b = 20   # Seconda variabile intera
    c = 30   # Terza variabile intera

    # Stampa dei valori originali
    print("Prima dell'ordinamento:")
    print(f"a = {a}, b = {b}, c = {c}")

    # Ordinamento crescente utilizzando scambi
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    # Stampa dei valori ordinati
    print("Dopo l'ordinamento crescente:")
    print(f"a = {a}, b = {b}, c = {c}")

if __name__ == "__main__":
    main()