def feladat1(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)

def main():
    feladat1(12,-7)
if __name__ == '__main__':
    main()


def feladat3(x):
    if x>-2 and x<0:
        return 2*x
    elif x>=0 and x<2:
        return x*x
    elif x>2:
        return 10
    else:
        print("Nem értelmezhető!")
        return

def main():
    print(feladat3(10))
if __name__ == '__main__':
    main()


def feladat4(a, b, c):
    return min(a, b, c) and max(abs(a, b, c))

def main():
    feladat4(2, 3, 4)
if __name__ == '__main__':
    main()


def feladat5(a,b,c,d):
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

def main():
    feladat5(2,3,4,5)
if __name__ == '__main__':
    main()


import math as mt
def feladat6():
    while True:
        a=float(input("A háromszög oldalai: "))
        b=float(input("A háromszög oldalai: "))
        c=float(input("A háromszög oldalai: "))
        if a<=0 or b<=0 or c<=0:
            print("Nem megfelelő adatok!")
        else:
            break
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        T=mt.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=a*b*c/(4*T)
        print("R=%2.2f és r=%.2f" % (R,2))
    else:
        print("Nem értelmezhető!")

def main():
    print(feladat6())
if __name__ == '__main__':
    main()


def feladat7():
    a=float(input("A téglalap egyik oldala méterben: "))
    b=float(input("A téglalap egyik oldala méterben: "))
    c=float(input("A drót hossza méterben: "))
    if a<=0 or b<=0 or c<=0:
        print("Nem megfelelő adatok!")
    else:
        K=(a+b)*2
        s=c-K
        print(K,s)

def main():
    (feladat7()
if __name__ == '__main__':
    main()


def feladat10(a,b):
    db=0
    if a>0 and b>0:
        if a>=b:
            s=a-b
        else:
            s=b-a
        if s%4==0 and s%100!=0:
            db+=1
            print(db)

def main():
    print(feladat10(1997,1990))
if __name__ == '__main__':
    main()


def feladat12():
    a=float(input("A dolgozat max pontszáma: "))
    b=float(input("A dolgozat eredménye: "))
    s=b%a*100
    if s>=60:
        print("Sikeres dolgozat!")
    else:
        print("Sikertelen dolgozat!")

def main():
    feladat12()
if __name__ == '__main__':
    main()


def feladat13():
    a=int(input("Add meg az érdemjegyet!: "))
    if a==1:
        print("Elégtelen")
    elif a==2:
        print("Elégséges")
    elif a==3:
        print("Közepes")
    elif a==4:
        print("Jó")
    elif a==5:
        print("Jeles")
    else:
        print("Nem értelmezhető input!")

def main():
    feladat13()
if __name__ == '__main__':
    main()


def feladat14():
    a=int(input("A hónap sorszáma: "))
    if a==1:
        print("Január")
    elif a==2:
        print("Február")
    elif a==3:
        print("Március")
    elif a==4:
        print("Április")
    elif a==5:
        print("Május")
    elif a==6:
        print("Június")
    elif a==7:
        print("Július")
    elif a==8:
        print("Augusztus")
    elif a==9:
        print("Szeptember")
    elif a==10:
        print("Október")
    elif a==11:
        print("November")
    elif a==12:
        print("December")
    else:
        print("Nem értelmezhető input")

def main():
    feladat14()
if __name__ == '__main__':
    main()


def feladat15(a,b,hanyados):
    if a>=b:
        hanyados=hanyados+1
        a=a-b
    else:
        print("Nem értelmezhető!")
    return a

def main():
    print(feladat15(600,400,100))
if __name__ == '__main__':
    main()


def feladat16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a

def main():
    print(feladat16(360,225))
if __name__ == '__main__':
    main()


def feladat17(n):
    masolat=n
    uj_szam=0
    while n!=0:
        szj=n%10
        uj_szam=uj_szam*10+szj
        n=n/10
    return uj_szam==masolat

def main():
    print(feladat17(333))
if __name__ == '__main__':
    main()


def feladat19(n):
    n=int(input("Szám: "))
    prim=True
    if n==1:
        prim=False
    for i in range(2,n):
        if n%i==0:
            prim=False
            break
        if prim:
            print("Prímszám")
        else:
            print("Nem prímszám")

def main():
    feladat19(10)
if __name__ == '__main__':
    main()


def feladat20(n):
    a=1
    b=1
    if n==1:
        print(a, end=" ")
    elif n==2:
        print(a,b, end=" ")
    else:
        c=a+b
        print(a,b,c, end=" ")
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c, end=" ")
            k+=1

def main():
    feladat20(10)
if __name__ == '__main__':
    main()


def feladat21(n):
    ujszam=0
    while n!=0:
        maradek=n%10
        ujszam=ujszam*10+maradek
        n=n/10
    return ujszam

def main():
    print(feladat21(7532))
if __name__ == '__main__':
    main()


def feladat22(a,b,c):
    c=1
    while b>0:
        if b%2==1:
            c=c*a
            b=b-1
        else:
            a=a*a
            b=[b/2]
    return c

def main():
    feladat22(2,3,4)
if __name__ == '__main__':
    main()


def feladat25():
    a=input("Add meg az ország lakosainak számát ezer főben: ")
    b=input("Add meg az ország területét négyzetkilométerben:")
    c=a%b*1000
    if c<50:
        print("Ritkán lakott")
    elif c>=50 and c<300:
        print("Álagos népsűrűségű")
    else:
        print("Sűrűn lakott")

def main():
    feladat25()
if __name__ == '__main__':
    main()