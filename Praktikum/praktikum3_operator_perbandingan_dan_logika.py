# 1. Buat variabel nilai dan kehadiran. 
# 2. Gunakan operator >= untuk memeriksa masing-masing syarat.
# 3. Gunakan operator and untuk menentukan apakah mahasiswa memenuhi kedua syarat.
# 4. Ubah nilai menjadi 70. Jalankan kembali program dan amati perubahan hasil.
# 5. Coba gunakan or.


# 1. Deklarasi variabel dengan nilai 82 dan kehadiran 90
# Dengan logika and

print("Dengan nilai 82: ")
nilai = 82
kehadiran = 90

# Perbandingan dan Logika
if nilai >= 75 and kehadiran >= 80:
    print(f"Nilai = {nilai}")
    print(f"Kehadiran = {kehadiran}")
    print("Selamat anda lulus")
else:
    print(f"Nilai = {nilai}")
    print(f"Kehadiran = {kehadiran}")
    print("Anda tidak lulus")

# 2. Deklarasi variabel dengan nilai 70 dan kehadiran 90
# Dengan logika and

print("\nDengan nilai 70:")
nilai = 70
kehadiran = 90

# Perbandingan dan Logika
if nilai >= 75 and kehadiran >= 80:
    print(f"Nilai = {nilai}")
    print(f"Kehadiran = {kehadiran}")
    print("Selamat anda lulus")
else:
    print(f"Nilai = {nilai}")
    print(f"Kehadiran = {kehadiran}")
    print("Anda tidak lulus")

# 3. Deklarasi variabel dengan nilai 70 dan kehadiran 90
# Logika menggunakan or

print("\nDengan nilai 70 dan menggunakan logika or:")
nilai = 70
kehadiran = 90

# Perbandingan dan Logika
if nilai >= 75 or kehadiran >= 80:
    print(f"Nilai = {nilai}")
    print(f"Kehadiran = {kehadiran}")
    print("Selamat anda lulus")
else:
    print(f"Nilai = {nilai}")
    print(f"Kehadiran = {kehadiran}")
    print("Anda tidak lulus") # Kerika salah satunya terpenuhin maka di nyatakan lulus