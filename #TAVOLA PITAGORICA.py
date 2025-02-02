#TAVOLA PITAGORICA

def main():
    for riga in range(13):
        print(f"\n{riga} ", end="")
        for colonna in range(13):
            print(f" {riga * colonna} ", end="")

if __name__ == "__main__":
    main()