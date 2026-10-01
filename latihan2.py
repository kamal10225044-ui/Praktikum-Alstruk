try:
    angka = int(input("Masukan angka: "))
    if angka % 2:
        print(f"{angka} ini adalah angka ganjil")
    else:
        print(f"{angka} ini adalah angka genap")
except ValueError:
    print("Error: Masukan angka!")