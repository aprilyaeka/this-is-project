kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
#               0      1           2       3              
#              -4      -3         -2      -1
# print(kendaraan)

# a) menambah di akhir list-> data.appened
kendaraan.append ("truk")
print(f"data ditambah lagi ={kendaraan}")
# b) menyisipkan data di list
kendaraan.insert(1,"becak")
print(f"data sesudah ditambah={kendaraan}")
# c) menghapus data paling akhir
kendaraan.pop ()
print(f"data akhir={kendaraan}")
# d) mengubah elemen
kendaraan [3] ="skuter"
print(f"data setelah diubah = {kendaraan}")
# e) jumlah total data dalam list
panjang_data = len(kendaraan)
print(f"jumlah data yang ada di list = {panjang_data}")

# soal 2
angka = [75, 80, 90, 75, 85, 100, 65] 
#         0   1   2   3   4   5    6
#        -7    -6    -5  -4  -3  -2    -1
#print(angka)
posisi_angka_100= angka.index(100)
print(f"posisi angka 100 = {posisi_angka_100}")
# b) banyak siswa mendapat skor 75
jumlah_data_75= angka.count(75)
print(f"banyaknya siswa yang mendapat skor 75 adalah {jumlah_data_75}")
# c) urutkan list skor ujian
angka.sort ()
print(f"data diurutkan dari terkecil ke terbesar adalah {angka}")
# d) balikkan urutan list dari terbesar ke terkecil
angka.reverse ()
print(f"data diurutkan dari terbesar ke terkecil ={angka}")

#soal 3
menu_utama = ["Nasi Goreng", "Mie Ayam"] 
menu_tambahan = ["Kerupuk", "Es Teh"] 
menu_utama.extend(menu_tambahan)
print(f"penggabungan 2 menu adalah {menu_utama}")

#soal 4
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]] 
#                     0                  1               2               
#                    -3                  -2                -1
# a) tampilkan harga pensil
harga_pensil = data_barang[1][1]
print(f"harga pensil adalah {harga_pensil}")
# b) perulangan 
for barang in data_barang:
    nama = barang[0]
    harga = barang[1] 
    print(f"nama:{nama},harga:{harga},")

          
   