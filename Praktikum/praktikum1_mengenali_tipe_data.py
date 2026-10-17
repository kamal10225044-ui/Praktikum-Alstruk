# 1. Tampilkan semua nilai variabel. 
# 2. Tampilkan tipe data setiap variabel. 
# 3. Ubah nilai umur menjadi 20. Apa yang berubah pada output? 
# 4. Jelaskan perbedaan "19" dan 19.

nama = "Fajar"
umur = 19
berat = 54.5
terdaftar = True

# 1. Menampilkan semua nilai
print(f"""
nama = {nama}
umur = {umur}
berat = {berat}
terdaftar = {terdaftar}
""")

# 2. Menampilkan semua tipe data dari variabel
print("nama = ",type(nama))
print("umur = ",type(umur))
print("berat = ",type(berat))
print("terdaftar = ",type(terdaftar))

# 3. Mengubah nilai umur menjadi 20
print("\nMengubah nilai umur menjadi 20")
nama = "Fajar"
umur = 20
berat = 54.5
terdaftar = True

print(f"""
nama = {nama}
umur = {umur}
berat = {berat}
terdaftar = {terdaftar}
""") # Output umur menjadi 20

# 4. Perbedaan "19" dan 19:
# "19" adalah tipe data string
# 19 adalah tipe data integer

