"""
matrisin terisni bulmak
matrisin birebir kopyasını almak
"""
#dededededdededededede cemree
import numpy
def invert_matrix(A,tol=None):
    n = len(A)
    BM = numpy.matrix.copy(A)  #matrisin birebir kopyası için
    I = identity_matrix(n)
    IM = copy_matrix(I)
    indires = list(range(n))
    for fd in range (n):
        fdscaler = 1.0/BM[fd][fd]
        for j in range(n):
            BM[fd][j] *= fdscaler
            IM[fd][j] *= fdscaler
    for i in indires[0:fd] + indires[fd+1]:
        print(i)
        crscaler = BM[i][fd]
        for j in range (n):
            BM[i][j] = BM[i][j] - crscaler * BM[fd][j]
            IM[i][j] = IM[i][j] - crscaler * IM[fd][j]

    return IM

A = (1,2,3,4,5)
print(invert_matrix(A))
