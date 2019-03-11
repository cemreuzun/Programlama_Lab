#girilen sayinin asal olup olmadigini bulun
#sayi asal ise asal oldugunu geri dondursun
#asal degil ise tum carpanlarını cikti olarak versin

a=0
sayi=input('Sayı : ')
for i in range (2,int(sayi)):
    if (int(sayi)%i == 0):
        print(i)
        a = a+1

if(a = 1) :
    print("Sayi Asal degil")
else :
    print("Sayi Asaldir")
