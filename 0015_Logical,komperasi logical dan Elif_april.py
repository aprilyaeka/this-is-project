# meminta user memasukan usia
usia = int(input("masukan usia anda:"))
if  usia>=0 and usia <=12 :
    print("anak-anak")
elif  usia>=13 and usia<=17 :
    print("remaja")
elif usia>=18 and usia<=59 :
    print("dewasa")
else :
    print("lansia")

