lenta = [[' ' for _ in range(3)] for _ in range(3)]

def atspausdinti():
    for eile in lenta:
        print("|".join(eile))
        print("-" * 5)


def zaidejo_ejimas(zaidejas):
    while True:
        try:
            eilute = int(input(f"žaidėjas {zaidejas}, pasirinkite eilę (0,1,2): "))
            stulpelis = int(input(f"žaidėjas {zaidejas}, pasirinkite stulpelį (0,1,2): "))

            if 0 <= eilute <= 2 and 0 <= stulpelis <= 2:
                if lenta[eilute][stulpelis] == ' ':
                    lenta[eilute][stulpelis] = zaidejas
                    break

                else:
                    print("Šita viena panaudota, pasirinkite kita.")
            else:
                print("Tokio pasirinkimo nėra, pasirinkite nuo 0 iki 2")
        except ValueError:
            print("Tokio pasirinkimo nėra, pasirinkite nuo 0 iki 2")


def kas_laimejo(zaidejas):
    for eilute in lenta:
        if all([cell == zaidejas for cell in eilute]):
            return True

    for stulpelis in range(3):
        if all([lenta[eilute][stulpelis] == zaidejas for eilute in range(3)]):
            return True

    if all([lenta[i][i] == zaidejas for i in range(3)]) or all([lenta[i][2-i] == zaidejas for i in range(3)]):
        return True

    return False

def patikrinti_lygiasas():
    for eilute in lenta:
        if ' ' in eilute:
            return False
    return True

def zaidimas():
    zaidejas = 'X'

    while True:
        atspausdinti()
        zaidejo_ejimas(zaidejas)

        if kas_laimejo(zaidejas):
            atspausdinti()
            print(f"Žaidėjas {zaidejas} laimi !!!")
            break

        if patikrinti_lygiasas():
            atspausdinti()
            print("Lygiosios")
            break

        zaidejas = '0' if zaidejas == 'X' else 'X'

zaidimas()
