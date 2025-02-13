def kalkulaator():
    nimi = input("Tere! mis on teie nimi") #
    print(f"Tere, {nimi}! Tere tulemast kalkulaatori")

    while True:
        print("\nVali arvutuse tüüp:")
        print("1. Liitmine (+)")
        print("2. Lahutamine (-)")
        print("3. Korrutamine (*)")
        print("4. jagamine (/)")
        print("5. Lõpeta")

        valik = input("Sisesta valiku number (1-5): ")

        if valik == "5":
            print(f"Aitäh kasutamast {nimi}! Head päeva!")
            break

        if valik not in ("1", "2", "3", "4"):
            print("Vigane sisestus, proovi uuesti.")
            continue

        try:
            arv1 = float(input("Sisesta esimene arv: "))
            arv2 = float(input("Sisesta teine arv: "))

            if valik == "1":
                tulemus = arv1 + arv2
                märk = "+"
            elif valik == "2":
                tulemus = arv1 - arv2
                märk = "-"
            elif valik == "3":
                tulemus = arv1 * arv2
                märk = "*"
            elif valik == "4":
                if arv2 == 0:
                    print("Viga: Nulliga jagamine ei ole lubatud.")
                continue
            tulemus = arv1 / arv2
            märk = "/"
            print(f"tulemus: {arv1} {märk} {arv2} = {tulemus}")

        except ValueError:
            print("Viga: Palun sisesta numbrid!")
kalkulaator()

#
