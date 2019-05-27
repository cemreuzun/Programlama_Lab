"""
> bubble sort (n-1)*n/2 kadar swap yapıyor bubble la selection aynı
> insertion sort (n-1)*n/2 kadar karşılaştırma yapıyor
> bubble, insertion, shell sort bunları karşılaştır
> veriye bağlı
> veri de herhangi bir değişiklik yapılması gerekiyorsa komşuyla karşılaştırma algoritmayı ilerlet komşu yerine daha uzaak bir sayı ile karşılaştır
> bubble sorta göre komşuyla karşılaştırma

Shell Sort :
-diziyi 2 e böl
-2 grubu kendi indisleri ile karşılaştır    örn: d1[1] ile d2[1]
-3 e böl kendi içinde karşılaştır
-en son her bir grupta tek sayı kalana kadar böl ve insertion yap

"""

import random
def get_n_random_integer(n):
    random.seed(10)
    numbers = []
    for i in range (n):
        s = random.randint(-10, 10)
        numbers.append(s)
    return numbers

def shellSort(arr):
    n = len(arr)
    pop = int(n // 2)
    karsilastirma = 0
    yerdegistirme = 0
    while(pop > 0):
        for i in range(pop, n):
            karsilastirma += 1
            temp = arr[i]
            j = i
            while (j >= pop and arr[j-pop] > temp):
                karsilastirma += 2
                yerdegistirme += 1
                arr[j] = arr[j-pop]
                j -= pop
            arr[j] = temp
        pop = pop // 2

    return arr, karsilastirma, yerdegistirme

#arr = [12,34,54,2,3,1]
#print(shellSort(arr))

#random fonksiyon
a = get_n_random_integer(10)
#print(a)
print(shellSort(a))
