"""
    MATRİS İŞLEMLERİ
    - Yazdırma
    - Matematiksel İşlemleri( TOPLAMA - ÇIKARMA - SKALER ÇARPIM - ÇARPIM )
"""
m_1 = [[1,2,3],[2,3,4],[3,4,5]]
m_2 = [[1,2,3],[4,5,6],[1,2,3]]
m_3 = [[2,4,6],[8,10,12],[1,2,3]]

""" BU FONKSİYON KULLANICI TARAFINDAN MATRİSLERİN BELİRLEMESİNİ SAĞLAR.
def matris_yaz(matris):
    for row in matris:
        for eleman in row :
            print(eleman, end=' ')
        print()
print(matris_yaz(m_1))
"""
"""
EN İYİSİ ***matris_toplam*** fonksiyonudur.
"""
def matris_toplam(m_1,m_2):
    result = []
    for i in range(len(m_1)):  #m_1 satır sayısı döner ..
        add = [m_1[i][k] + m_2[i][k] for k in range(len(m_1[i]))]    #print(add) 'ÇIKTISI'  >>>[2, 4, 6]  >>>[6, 8, 10]  >>>[4, 6, 8]
        result.append(add)
    return result

#print(matris_toplam(m_1, m_2))


def matris_toplam2(m_1,m_2):
    result = []
    for i in range (len(m_1)):
        add = []
        for k in range(len(m_1[0])):#m_1 satır sayısı döner ..
            add.append(m_1[i][k] + m_2[i][k])
        result.append(add)
    #result[i][k].append(add)
    return result

#print(matris_toplam2(m_1, m_2))

def matrix_addition(m_1,m_2):
    result = []
    for satir in range (len(m_1)):
        result.append([]) # result'u [[],[],[]] hale getirir.2. for bitimin de bir liste oluşturur
        for sütun in range (len(m_1[0])):
            result[satir].append(m_1[satir][sütun] + m_2[satir][sütun])
    return result
#print(matrix_addition(m_1,m_2))

def matris_cikartma(m_1,m_2):
    result = []
    for i in range(len(m_1)):
        add = [m_1[i][k] - m_2[i][k] for k in range(len(m_1[0]))]
        result.append(add)
    return result
#print(matris_cikartma(m_1,m_2))

def matris_skaler_carpim(m_1, alpha):
    result = []
    for row in range (len(m_1)):
        result.append([])
        for sutun in range(len(m_1[row])):
             result[row].append(m_1[row][sutun]*alpha)
    return result
a = 5
#print(matris_skaler_carpim(m_1, a))

def matris_skaler_carpim2(m_1, alpha):
    result = []
    for row in range (len(m_1)):        #add=[m_1[row][sutun] * alpha for sutun in range(len(m_1[row]))]
        result.append([m_1[row][sutun] * alpha for sutun in range(len(m_1[row]))])
    return result
print(matris_skaler_carpim2(m_1, a))
