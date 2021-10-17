def makePolyStr(coefficients):
    polystr = ""
    i = 1
    for w in coefficients:
        if w != 0:
            sign = "+"
            if w < 0:
                sign = ""
            if len(coefficients)-i == 1:
                x = "x"
            elif len(coefficients)-i == 0:
                x = ""
            else:
                x = f"x^{len(coefficients)-i}"
            polystr += f"{sign} {w}{x} "
        i += 1

    return polystr


def horner(coefficients, a):
    newCoefficients = []
    toAdd = 0
    if len(coefficients) > 1:
        for coef in coefficients:
            newCoefficients.append(coef + toAdd)
            toAdd = a * (coef + toAdd)
    return newCoefficients


def main():
    print("Podaj kolejne współczynniki wielomianu: (k aby zakończyć): ")
    coefficients = []
    x = input()
    while (x != 'k'):
        try:
            coefficients.append(int(x))
        except Exception:
            pass
        x = input()

    print(f"Podaj a: {makePolyStr(coefficients)} / (x - a)")
    a = input()
    while (not a.isnumeric()):
        a = input()
    a = int(a)

    print(f"Resultat: {makePolyStr(horner(coefficients, a))}")


if __name__ == "__main__":
    main()