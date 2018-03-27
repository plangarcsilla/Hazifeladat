import numpy as np
def feladat1():
    n=0
    s=1
    n=int(input("Add meg az n: "))
    szam = int(input("Szám: "))
    ertek=szam
    while s<=n-1:
        szam=int(input("Szám: "))
        if ertek==szam:
            sorszam=s+1
            elozoszam=s

            print("a {0}. szám egyenlő a {1}. számmal".format(elozoszam,sorszam))
            s+=1
        ertek=szam

def main():
    feladat1()
if __name__ == '__main__':
    main()

def feladat2():
    n=5
    i=1
    szam=0
    paros=0
    paratlan=0
    while i<=n:
        szam=int(input("Adj egy számot: "))

        if szam%2==0:
            paros+=1
        else:
            paratlan+=1
        i+=1
    print("{0}:{1}  páros : páratlan ".format(paros,paratlan))

def main():
    feladat2()
if __name__ == '__main__':
    main()

def feladat3():
    n=int(input("N:"))
    i=0
    szum=0
    li=[]
    while i<=n:
        szam=int(input("Adj egy számot: "))

        li.append(szam)
        i+=1
    for i in li:
        szum += abs(i)
    print( szum/n)

def main():
    feladat3()
if __name__ == '__main__':
    main()

def feladat4():
    szum=  0
    k=1
    i=1
    negativ=0
    n=int(input("N: "))
    while i <= n:
        szam=int(input("Szám: "))
        if szam>0:
            k*=szam
        else:
            szum+=szam
            negativ+=1
        i+=1
    print("Szorzat: {0}.Számtani középarányos: {1}. ".format(k,szum/negativ))

def main():
    feladat4()
if __name__ == '__main__':
    main()

def feladat5():
    n=int(input("N: "))
    i=1
    li=[]
    sum=0
    while i <=n:
        szam=int(input("Szám: "))
        li.append(szam)
        i+=1
    szorzat=1
    for i in li:
        if i<7:
            szorzat*=i
        if szam>10:
            sum+=i
    print("Szorzat{0] összeg: {1}".format(szorzat,sum))

def main():
    feladat5()
if __name__ == '__main__':
    main()

def feladat6():
    szam1=int(input("Szám: "))
    szam2=int(input("Szám: "))


    while True:
        sum=szam1+szam2
        szam3=int(input("Szám: "))
        if szam3==0:
            break

        if szam3==sum:
            print("egyeznek" ,szam3)
        s=szam2
        szam1=szam2
        szam2=szam3

def main():
    feladat6()
if __name__=='__main__':
    main()


def feladat9(m,n):
    mar=m%n
    if mar==0:
        return n
    else:
        return feladat9(n,mar)

def rel_prim(t,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if feladat9(t[i],t[j]!=1):
                return False
    return True

def main():
    n=int(input())
    tomb=np.empty(n,dtype='int')

    for i in range(0,n):
        tomb[i]=int(input())

    print(rel_prim(tomb,n))
if __name__ == '__main__':
    main()


def zhfeladat_ascii(n,m):
    zhfeladat_ascii=np.zeros(n,m)

    for i in range(0,n):
        for j in range(0,m):
            if i==0 or i==n//2 or i==n-1:
                zhfeladat_ascii[i][j]=42
            else:
                zhfeladat_ascii[i][j]=32
        zhfeladat_ascii[i][0]==42
        if i>n//2:
            zhfeladat_ascii[i][m-1]=42

    for i in range(0,n):
        for j in range(0,m):
            print(chr(int(zhfeladat_ascii[i][j])),end=' ')
        print('\n')

def main():
    esetek=int(input())
    t=np.zeros(2*esetek,dtype='int')
    for i in range(0,2*esetek):
        sor=input()
        sor=sor.strip()
        sor=sor.split()
        t[i]=int(sor[0])
        t[i+1]=int(sor[1])

    for i in range(0,2*esetek,2):
        print(zhfeladat_ascii(t[i],t[i+1]))

if __name__ == '__main__':
    main()
