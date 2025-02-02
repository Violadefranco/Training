#SCAMBIO 2 NUMERI

def main():
    a = 1
    b = 2
    print(f"I numeri prima dello scambio sono: a={a}, b={b}")

    c = a
    a = b
    b = c

    print(f"I numeri dopo lo scambio sono: a={a}, b={b}")

if __name__ == "__main__":
    main()