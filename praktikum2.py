# Sebuah toko menjual buku seharga Rp12.500 per buah. Seorang pelanggan membeli 4 buku

# Deklarasi variabel
harga = 12500
jumlah = 4

# Perhitungan
hasil = harga * jumlah
sisa = hasil % 2000

diskon = 5000
total = hasil - diskon

# Menampilkan hasil
print("Harga barang: ",harga)
print("Total barang: ",jumlah)
print("Total harga: ",int(hasil))
print("Total harga setelah sisa pembagian 2000: ",int(sisa))
print("Total harga setelah dikurangi diskon: ",int(total))
