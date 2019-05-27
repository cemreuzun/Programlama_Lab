""""
# 1.
    - (text, string) 2 parametre alınacak.
    - (string) texte var ise TRUE, yoksa FALSE gönderen bir fonksiyon yazınız.
            örn: ('onsekiz mart üni', 'art') --> TRUE  örn: ('onsekiz mart', 'tr')  --> FALSE
    - (string) textte var ise bulunduğu cümlenin kaçıncı sıradasında bulunduğu yazan fonksiyonu yazınız.

# 2.
    - Gönderilen parametre 1.gönderilen parametrede n defa bulunuyorsa bulunduğu yerlerin
    başlangıç adresini (indis) liste halinde gönderen fonksiyonu yazınız.
            örn: [2, 15,....] --> n harfi
"""

def stringbul(text,string):
    x = 0
    list = []
    for i in text:
        x += 1
        if(string == i):
            list.append(x)
        #if(string == '.'):
            #print("\n")
    if(x == 0):
        print("False")
        print(list)
        return False
    else:
        print("True")
        print(string,len(list),"tane var.")
        print(list)
        return True
    print(text)

#stringbul("hayat garip. mesela yurekler cukur, icine dusenler vakur, geceyi bilenler camur, ileri gidenler durun",'r')
stringbul("Hayat endiseli. dedi ki yok bir seyim az once sorguladım ve simdi dort koseyim. kimle ters duseyim yasarken ilk neseyi, gurul gurul akan bir nehir var mı ask iceyim.",'k')
