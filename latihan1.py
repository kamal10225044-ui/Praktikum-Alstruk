try:
    angka = int(input("Masukan bilangan apapun: "))

    if angka < 0:
        print(f"{angka} ini adalah bilangan negatif")
    elif angka > 0:
        print(f"{angka} ini adalah bilangan positif")
    else:
        print(f"{angka} ini adalah bilangan nol")
except ValueError:
    print("Error")