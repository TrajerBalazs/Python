def kalkulator():
    print("Válasz a következő műveletek közül: ")
    print("1. Összeadás (+)")
    print("2. Kivonás (-)")
    print("3. Szorzás (*)")
    print("4. Osztás (/)")

    muvelet = input("Add meg a művelet sorszámát (1/2/3/4): ")
    
    if muvelet not in ['1', '2', '3', '4']:
        print("A szám nem szerepel a műveletek között.")
        return
    
    try:
        szam1 = float(input("Add meg az első számod: "))
        szam2 = float(input("Add meg a második számot: "))
    except ValueError:
        print("Érvénytelen szám formátum!")
        return
    
    eredmeny = None
    if muvelet == '1':
        eredmeny = szam1 + szam2
        print(f"Az eredmény: {szam1} + {szam2} = {eredmeny}")
    elif muvelet =='2':
        eredmeny = szam1 - szam2
        print(f"Az eredmény: {szam1} - {szam2} = {eredmeny}")
    elif muvelet =='3':
        eredmeny = szam1 * szam2
        print(f"Az eredmény: {szam1} * {szam2} = {eredmeny}")
    elif muvelet =='4':
        eredmeny = szam1 / szam2
        print(f"Az eredmény: {szam1} / {szam2} = {eredmeny}")

kalkulator()