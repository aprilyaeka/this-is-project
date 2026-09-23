print("bilangan ganjil dan genap dari 1-50 adalah")
bilangan = range(1,51)
for i in bilangan:
    if i %2:
        print(i,"adalah bilangan ganjil") 
    else:   
        print(i,"adalah bilangan genap") 
print("bilangan prima antara 1 sampai 100 adalah")
for angka in range (1,101):
    if angka >1:
        is_prima = True
        for i in range (2,angka): 
            if angka % i ==0:
                is_prima = False
                break
        if is_prima:
            print(angka, end=" ")   
        