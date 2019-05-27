"""
DERSTE YAPILANLAR ->
    >random sayı üret (.seed ifadesi ile her seferinde aynı sayılar üretilir.)
    >üretilen random sayilarlarin ortalamasini alan fonk yaz
    >standart sapmasini bulan fonk yaz
    >normalizasyon bulan fonk yaz
    (her değerin ortalamadan olan uzaklıklarının standart sapmaya oranı ile bulunur)
    >komsu orani bulan fonk yaz
    >insertion sort ile sırala
"""



import random
def random_sayi_üret(n):
    random.seed(100)
    numbers = []
    for i in range (n):
        s = random.randint(-100,100)
        numbers.append(s)
    return numbers

def n_sayinin_ortalamasi(numbers):
    toplam = 0
    kactane = 0
    for sayi in numbers:
        toplam += sayi
        kactane += 1
    return toplam / kactane

def n_sayinin_std(numbers):
    toplam = 0
    kactane = 0
    ort = n_sayinin_ortalamasi(numbers)

    for sayi in numbers:
        toplam = toplam + (sayi-ort)**2
        kactane = kactane + 1

    var1 = toplam/(kactane - 1)
    std1 = var1 * 0.5
    return std1

sayilar = random_sayi_üret(10)
#print("n tane sayinin ortalamasi: ",n_sayinin_ortalamasi(sayilar))
#print("n tane sayinin standart sapması: ", n_sayinin_std(sayilar))
#print(sayilar)
def normalizasyon(numbers):
     new_numbers = []
     ort = n_sayinin_ortalamasi(numbers)
     std = n_sayinin_std(numbers)
     for x in numbers:
         new_x = (x-ort)/std
         new_numbers.append(new_x)
         #print("x: ",x)
     return new_numbers

#print(normalizasyon(sayilar))

def komsu_orani_elde_etme(numbers):
    kactane = 0
    toplamKacSayi = 0

    ort = n_sayinin_ortalamasi(numbers)
    std = n_sayinin_std(numbers)

    low = ort - std
    high = ort + std

    for x in numbers:
        toplamKacSayi = toplamKacSayi + 1
        if( x > low and x < high ):
            kactane = kactane + 1
    return kactane / toplamKacSayi

#print(komsu_orani_elde_etme(sayilar))

def insertion(numbers): #Küçükten büyüğe sıralama
    sayilar_2 = numbers

    uzunluk_1 = len(sayilar_2)
    print(sayilar_2)
    for i in range(1, uzunluk_1):
        for j in range(i, 0, -1):
            if (sayilar_2[j] < sayilar_2[j - 1]):
                # swap
                temp = sayilar_2[j - 1]
                sayilar_2[j - 1] = sayilar_2[j]
                sayilar_2[j] = temp

    return sayilar_2

def insertion(numbers): #Küçükten büyüğe sıralama
    sirali_list = numbers

    uzunluk_1 = len(sirali_list)
    print(sirali_list)

    for i in range(1, uzunluk_1):
        for j in range(i, 0, -1):
            print(j)
            if (sirali_list[j] < sirali_list[j - 1]):
                # swap
                temp = sirali_list[j - 1]
                sirali_list[j - 1] = sirali_list[j]
                sirali_list[j] = temp
                #print(sirali_list)

    return sirali_list
print(" k -> b sıralanmış liste : ", insertion(sayilar))
