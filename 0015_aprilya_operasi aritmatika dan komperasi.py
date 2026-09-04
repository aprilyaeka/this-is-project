print("1. hitunglah luas,volume dan keliling dari bangunan tersebut!") 
# input data
panjang = 12
lebar   = 5
tinggi  = 8
luas        = 2* ((panjang*lebar)+(panjang* tinggi)+(lebar*tinggi))
volume      = panjang*lebar* tinggi
keliling    = 4* (panjang +lebar+tinggi) 
print("hasil luas     =",luas)
print("hasil volume   =",volume)
print("hasil keliling =",keliling)
print("2.apakah luas bangunan tersebut lebih luas dari 50?")
print(" jawaban = ", luas>50)
print("3. apakah volume tersebut bernilai 480?")
print(" jawaban =",volume ==480)
