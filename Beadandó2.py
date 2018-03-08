def feladat10(fajl_nev):
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
    main()
