print("===TUPLES===")
# A. Buatlah sebuah Tuple bernama mahasiswa berisi data diri 
Nama ="Aprilya Eka Nurfadilah"
Nim = 2605060015
Prodi ="Teknologi Informasi"
data_mahasiswa =("Nama : Aprilya Eka Nurfadilah","Nim : 2605060015","Prodi : Teknologi Informasi")
print(f"data diri mahasiswa ={data_mahasiswa}")

# B. Tampilkan data NIM dan Prodi dengan cara mengakses indeksnya
print(data_mahasiswa[1])
print(data_mahasiswa[2])

# C. Coba jalankan kode mahasiswa[2] = "TEKNOLOGI INFORMASI"
# tidak bisa mengubah,menambahkan,atau menghapus elemen didalamnya
# data_mahasiswa[2] ="Teknologi Informasi"
# print(data_mahasiswa)

# D. Buatlah sebuah set dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis 2 kali
data_sets = { 10, 4, 3, 2, 4, 10, 7, 5}
print(data_sets)
# karena set tidak ada duplikasinya maka, ketika kita memasukkan angka double maka yang akan kesimpan hanya 1 angka jadinya angka 10 dan 4 hanya diambil satu doang

print("===MANIPULASI DICTIONARY===")
# A.  Buatlah sebuah dictionary data_mahasiswa
data_mahasiswa={
    "nim":240101,
    "nama":"Budi Santoso",
    "prodi":"Teknologi Informasi",
}
print(data_mahasiswa)
for key,value in data_mahasiswa.items():
    print(f"key={key},value={value}")

# B. Ubah nilai"Prodi" menjadi "Sastra mesin" dan menambahkan key baru " Angkatan"dengan nilai 2026
data_mahasiswa["prodi"]="sastra mesin"
print(data_mahasiswa)
data_mahasiswa["angkatan"]=2026
print(data_mahasiswa)

# C. menghapus "nim"
del data_mahasiswa["nim"]
print(data_mahasiswa)

print("===PERULANGAN PADA DICTIONARY===")
# A. Buatlah dictionary bernama keranjang
keranjang= { 
 "apel": 5000, 
 "pisang":3000,
 "jeruk":7000,
 "anggur":15000,
} 
print(keranjang)

# B. Gunakan perulangan untuk menampilkan setiap barang dan harganya
Total_belanja = 0
for buah,harga in keranjang.items():
    print(f"harga {buah} : Rp {harga}")
print("---------------------------------------------------------------------------")

# C. Tampilkan total belanja
Total_belanja = sum(keranjang.values())
print(f"Total Belanja : Rp{Total_belanja}")

