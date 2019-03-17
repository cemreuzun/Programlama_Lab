# 12.03.2019
# kullaniciya para ustunu soruyoruz
# aldigimiz para degiskenini bozuk para listesindeki paralarla tane olarak en az olmak kosuluyla veriyoruz
# kod girilen para degiskenini kac tane ve nasıl verilmesi gerektigini soyluyor

# benim yaptigim
bozukPara = [1, 5, 10, 25, 50]
para = int(input("Para Ustu: "))

def paraUstu(liste, a, bilinen):
    min = a
    if a in liste:
        bilinen[a] = 1
        return 1
    elif(bilinen[a]>0):
        return bilinen[a]
    else:
        for i in [c for c in liste if c<=a]:
            sayac = 1 + paraUstu(liste, a-i, bilinen)
            if(sayac<min):
                min = sayac
                bilinen[a] = min
    return min

sonuc  = paraUstu(bozukPara, para, [0]*(para+1))
print(sonuc)

# hocanin derste gosterdigi
def recMC(coinValueList,change):
  minCoins=change
  if(change in coinValueList):
    return 1
  else:
    for i in [c for c in coinValueList if c<=change]:
      numCoins=1+recMC(coinValueList,change-i)
      if(numCoins<minCoins):
        minCoins=numCoins
  return minCoins
print(recMC([1,5,10,25,50],30))

# gelistirilmis hali

def recMC(coinValueList,change,knownResults):  #coinValueList:bozuk para listesi change:degisken knownResult:bilinen sonuc
  minCoins=change
  if(change in coinValueList):
    knownResults[change]=1
    return 1
  elif(knownResults[change]>0):
    return knownResults[change]
  else:
    for i in [c for c in coinValueList if c<=change]:
      numCoins=1+recMC(coinValueList,change-i,knownResults)
      if(numCoins<minCoins):

        minCoins=numCoins
        knownResults[change]=minCoins
  return minCoins
print(recMC([1,5,10,25,50],60,[0]*61))



# ODEV
# global olarak yaz(knownResults)
