import sys

def main(argv):
    total_words = 0
    lines = 0
    signs = 0
    harnasie = 0
    andrzeje = 0

    if len(argv) != 2:
        print('Zła liczba argumentów')
        sys.exit()

    try:
        with open(argv[1], 'r', encoding='utf-8') as infile:
            for line in infile:
                lines += 1
                words = line.split()
                for word in words:
                    if word.lower().strip() == "harnaś":
                        harnasie += 1
                    elif word.lower().strip() == "andrzej":
                        andrzeje += 1
                    total_words += 1
                    signs += len(word)

        print(f"Liczba słów: {total_words}\nLiczba znaków: {signs}\nLiczba wierszy: {lines}\nHarnaś mentioned {harnasie} razy\nIle andrzejów potrzeba, aby wkręcić żarówkę? {andrzeje}")

    except FileNotFoundError:
        print('Nie ma takiego pliku')
        sys.exit()


if __name__ == "__main__":
    main(sys.argv)