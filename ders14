"""
Stirng - Liste - Dosya
  - Fonksiyon yazıyoruz.
  - Bu fonksiyon iki parametre alacak. (dosya, string)
  1. sorun : Dosyanın içinde string var ise True döndürecek yok ise False 
  2. sorun : Dosyanın içinde string bulunursa ilk bulunduğu konumu return edecek
  3. sorun : Dosyanın içerisinde yazdığımız strinng kaç kere var onu liste halinde return eden fonksiyon
  
"""

def fonkString(text, string):
    if string in text:
        print("TRUE")
        print(text.index(string), ". sirada ilk", string, "bulundu")
        print(text.count(string),"tane",string, "var")

        liste = []

        for i in range(len(text)):
            if(text[i] == string):
                liste.append(i)
        for x in liste:
            print(x)
    else:
        print("FALSE")

fonkString("Programlama laboratuvari calisma sorulari dosya string liste kullanma ", "m")
