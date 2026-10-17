# Buat program untuk mengelola data sederhana berikut. 
#  nilai = [78, 85, 90, 85] 
#  mahasiswa = {"nama": "Nadia", "kelas": "IF-A"} 
#  koordinat = (5, 8) 
#  angka = {2, 4, 4, 6, 8} 
# Tugas: 
# 1. Tampilkan nilai pertama dari list. 
# 2. Tambahkan nilai 95 ke list dan tampilkan list terbaru. 
# 3. Tampilkan nama mahasiswa dari dictionary. 
# 4. Tampilkan koordinat pertama dari tuple.
# 5. Tampilkan angka unik dengan sorted(angka). 
# 6. Jelaskan mengapa angka 4 hanya muncul satu kali pada set. 

# Deklarasi variabel

nilai = [78, 85, 90, 85]
mahasiswa = {"nama": "Nadia", "kelas": "IF-A"}
koordinat = (5, 8)
angka = {2, 4, 4, 6, 8}

# 1. Menampilkan nilai pertama dari list
print("Nilai pertama dari list: ",nilai[0])

# 2. Menambahkan nilai 95 ke list dan tampilkan list terbaru
print("Nilai list awal: ",nilai)
nilai.append(95)
print("Setelah di tambahkan angka 95: ",nilai)

# 3. Menampilkan nama mahasiswa dari dictionary
print("Menampilkan nama mahasiswa: ",mahasiswa["nama"])

# 4. Menampilkan koordinat pertama dari tuple
print("Menampilkan nilai koordinat pertama: ",koordinat[0])

# 5. Menampilkan angka unik dengan sorted angka
print("Menampilkan angka unik dengan sorted(): ",sorted(angka))

# 6. Jelaskan mengapa angka 4 hanya muncul satu kali pada set.
print("Tidak ada duplikasi pada set: ",angka)
# Angka 4 hanya muncul satu kali karena dalam set tidak boleh ada duplikasi