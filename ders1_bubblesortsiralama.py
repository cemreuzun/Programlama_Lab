# derste random dizi olusturuldu
# bubble Sort ile kücükten buyuge siralama yapildi
# olusturduğumuz dizi de istedigimiz sayiyinin olup olmadigini kontrol edildi

import random
my_array = []

def rand_array(n):
    for i in range(n):
        s = random.randint(0,100)
        my_array.append(s)
    return my_array

my_arr = []
my_arr = rand_array(10)

print(my_arr)


for i in range(len(my_array)-1,0,-1):
    for j in range(i):
        if(my_array[j] > my_array[j+1]):
            t = my_array[j]
            my_array[j] = my_array[j+1]
            my_array[j+1] = t
print(my_array)


def my_search(array_2,item):
    found = False
    indis = -1
    for i in range(len(array_2)):
        if array_2[i] == item:
            found = True
            indis = i
    return (found,indis)

print(my_search(my_arr,100))
