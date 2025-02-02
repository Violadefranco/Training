#QUOZIENTE RESTO 14-3

def main():
    q = 0
    X = 14
    D = 3
    r = X

    while r >= D:
        r = r - D
        q += 1

    print(f"r={r}, q={q}")

if __name__ == "__main__":
    main()