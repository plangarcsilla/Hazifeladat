"""def feladat10(fajl_nev):
    fajl=open(fajl_nev,mode="r")
    max=0
    for sor in fajl:
        if (sor.[0].isupper() and len(sor)>max):
            max=len(sor)
    print(max)
    fajl.close()

def main:
    feladat10("be.txt")
if __name__ == '__main__':
    main()"""


def feladat5_osztok(szam):
    db=2
    for i in range(2, szam//2+1):
        if szam%i==0:
            db=db+1
    return db

def eros(n):
    max=1
    for i in range(2,n+1):
        if max<feladat5_osztok(i):
            max=feladat5_osztok(i)
            print(i)

def main():
    eros(12)
if __name__ == '__main__':
    main()