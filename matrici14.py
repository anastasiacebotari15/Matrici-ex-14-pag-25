n=int(input('Introduceti nr de linii:'))
A=[]
if n>=2 and n<=10 :
    for i in range(0,n):
        k=[]
        for l in range(0,n):
            k.append(int(input('Introduceti elementele: ')))
            A.append(k)
    print(A)
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
for i in range(len(A)):
    for j in range(len(A[0])):
        if i==j:
            a.append(A[i][j])
        if i<j:
            c.append(A[i][j])
        if i>j:
            d.append(A[i][j])
        if i+j<n-1 :
            e.append(A[i][j])
        if i+j>n-1 :
            f.append(A[i][j])
print('Suma componentelor pe diagonala principala este', sum(a))
print('Suma componentelor de pe diagonala secundara este', sum(b))
print('Suma componentelor mai sus de diagonala principala este', sum(c))
print('Suma componentelor mai jos de diagonala principala este', sum(d))
print('Suma componentelor mai sus de diagonala secundara este', sum(e))
print('Suma componentelormai jos de diagonala secundar este', sum(f))