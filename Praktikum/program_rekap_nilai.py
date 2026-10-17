# 1. Simpan nama mahasiswa dalam variabel string. 
# 2. Simpan nilai tugas dan nilai ujian dalam variabel numerik. 
# 3. Hitung rata-rata kedua nilai. 
# 4. Mahasiswa dinyatakan lulus jika rata-rata minimal 75. 
# 5. Tampilkan nama, kedua nilai, rata-rata, dan status lulus (True/False). 
# 6. Uji program dengan minimal dua kombinasi nilai yang berbeda. 

print(5*"="+"Program Rekap Nilai Mahasiswa"+"="*5)

nama = "Ahmad Darus"
nim = 10225
kelas = "IF II B"

nilai_tugas = 70
nilai_ujian = 80

# konversi nilai keseluruhan menjadi list
nilai = [nilai_tugas, nilai_ujian]

# Menghitung rata-rata nilai
total_nilai = sum(nilai)
panjang_nilai = len(nilai)
rata_rata_nilai = total_nilai / panjang_nilai

if rata_rata_nilai >= 75:
    status = True
else:
    status = False

print(f""""
Nama = {nama}
Nim = {nim}
Kelas = {kelas}

Nilai Tugas: {nilai_tugas}
Nilai Ujian: {nilai_ujian}
Rata-Rata Nilai: {rata_rata_nilai}
Status: {status} (True = Lulus / False = Tidak Lulus)
""")


print("\n"+5*"="+"Program Rekap Nilai Mahasiswa"+"="*5)
nama = "Ahmad Darus"
nim = 10225
kelas = "IF II B"

nilai_tugas = 65
nilai_ujian = 50

# konversi nilai keseluruhan menjadi list
nilai = [nilai_tugas, nilai_ujian]

# Menghitung rata-rata nilai
total_nilai = sum(nilai)
panjang_nilai = len(nilai)
rata_rata_nilai = total_nilai / panjang_nilai

if rata_rata_nilai >= 75:
    status = True
else:
    status = False

print(f"""
Nama = {nama}
Nim = {nim}
Kelas = {kelas}

Nilai Tugas: {nilai_tugas}
Nilai Ujian: {nilai_ujian}
Rata-Rata Nilai: {rata_rata_nilai}
Status: {status} (True = Lulus / False = Tidak Lulus)
""")