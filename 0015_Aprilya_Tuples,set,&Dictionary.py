# # tuple
print("soal 1 : tuple")
data_mahasiswa =("Nama","NPM","Prodi")
print(f"data diri mahasiswa ={data_mahasiswa}")
print(data_mahasiswa[1])
print(data_mahasiswa[2])
# data_mahasiswa[2] ="Teknologi Informasi"
# print(data_mahasiswa)
#dinyatakan eror karena tuple bersifat immutable(tidak dapat mengubah,menambah,atau menghapus elemen didalamnya)
data_sets = { 10, 4, 3, 2, 4, 10, 7, 5}
print(data_sets)
# print("set tidak ada duplikasinya maka, ketika kita memasukkan angka double maka yang akan kesimpan hanya 1 angka")
print("soal 2 : manipulasi dictionary")
#mahasiswa=["Budi Santoso",240101,"Teknologi Informasi"]
#print(mahasiswa)
data_mahasiswa={
  
    "nim":240101,
    "nama":"Budi Santoso",
    "prodi":"Teknologi Informasi",

}
print(data_mahasiswa)
for key,value in data_mahasiswa.items():
    print(f"key={key},value={value}")
data_mahasiswa["prodi"]="sastra mesin"
print(data_mahasiswa)
data_mahasiswa["angkatan"]=2026
print(data_mahasiswa)
del data_mahasiswa["nim"]
print(data_mahasiswa)
print("soal 3 : perulangan pada dictionary")
keranjang= { 
 "apel": 5000, 
 "pisang":3000,
 "jeruk":7000,
 "anggur":15000,
} 
print(keranjang)
Total_belanja = 0
for buah,harga in keranjang.items():
    print(f"harga {buah} : Rp {harga}")
    Total_belanja +=harga
print(f"Total Belanja : Rp{Total_belanja}")

