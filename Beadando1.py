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

