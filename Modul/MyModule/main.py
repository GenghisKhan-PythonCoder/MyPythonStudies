import calculate
import time

print("""
*******************************
ALAN & ÇEVRE HESAPLAMA PROGRAMI
*******************************
""")

while True:
    print("""
    >> İŞLEMLER <<
    1 - Daire Alan Hesaplama
    2 - Daire Çevre Hesaplama
    3 - Dikdörtgen Alan Hesaplama
    4 - Dikdörtgen Çevre Hesaplama
    5 - Kare Alan Hesaplama
    6 - Kare Çevre Hesaplama
    7 - Üçgen Alan Hesaplama
    8 - Üçgen Çevre Hesaplama
    Q - Çıkış
    """)
    i = input("Yapmak istediğiniz işlemi seçiniz.\nİŞLEM : ")
    if i == "Q":
        print("ÇIKIŞ GERÇEKLEŞİYOR..")
        time.sleep(2)
        print("YİNE BEKLERİZ !! :)")
        break
    elif i == "1":
        r = int(input("Yarı çap : "))
        calculate.daireAlan(r)
    elif i == "2":
        r = int(input("Yarı çap : "))
        calculate.daireCevre(r)
    elif i == "3":
        a = int(input("Uzun kenar : "))
        b = int(input("Kısa kenar : "))
        calculate.dikdortgenAlan(a,b)
    elif i == "4":
        a = int(input("Uzun kenar : "))
        b = int(input("Kısa kenar : "))
        calculate.dikdortgenCevre(a,b)
    elif i == "5":
        a = int(input("Kenar : "))
        calculate.kareAlan(a)
    elif i == "6":
        a = int(input("Kenar : "))
        calculate.kareCevre(a)
    elif i == "7":
        a = int(input("Taban : "))
        h = int(input("Yükseklik : "))
        calculate.ucgenAlan(a,h)
    elif i == "8":
        a = int(input("1. Kenar : "))
        b = int(input("2. Kenar : "))
        c = int(input("3. Kenar : "))
        calculate.ucgenCevre(a,b,c)
    else:
        print("GEÇERSİZ İŞLEM !! :)")