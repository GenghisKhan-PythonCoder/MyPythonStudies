import math
import time
print("""
*********************************
     KAPSAMLI HESAP MAKİNESİ
*********************************
""")
while True:
    print("""
    >> İŞLEMLER <<
1 - Toplama
2 - Çıkarma
3 - Çarpma
4 - Bölme
5 - Kalansız bölme
6 - Bölümden kalanı bulma
7 - Sayının karesini alma
8 - Sayının küpünü alma
9 - Faktöriyel
10 - Kosinüs
11 - Mutlak değer
12 - Ebob
13 - Kuvvet alma
14 - Sinüs
15 - Kare kök bulma
16 - Tanjant
17 - Yay sinüs
18 - Yay tanjant
19 - Açıyı dereceden radyana çevirme
20 - Gerçek sayıyı 0'a doğru en yakın İntegrale kadar keser.
Çıkış "Q"
    """)
    islem = input("İşlem seçiniz :")
    if islem == "1":
        numb1 = int(input("Sayı 1: "))
        numb2 = int(input("Sayı 2: "))
        result = numb1 + numb2
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb1} + {numb2} = {result}")
        print("Sonucu taban ya da tavan değerlerine yuvarlamak ister misiniz?(Evet için 'E' - Hayır için 'H' - Çıkış 'Q')")
        soru = input("İşlem seçiniz :")
        if soru == "E":
            print(f"{result} değerini taban değerine yuvarlamak için 'TABAN', tavan değerine yuvarlamak için 'TAVAN' yazınız.")
            soru = input("İşlem seçiniz :")
            if soru == "TABAN":
                taban = math.ceil(result)
                print("Hesaplanıyor..")
                time.sleep(2)
                print(f"{result} sayısının taban değeri {taban}")
            elif soru == "TAVAN":
                tavan = math.floor(result)
                print("Hesaplanıyor..")
                time.sleep(2)
                print(f"{result} sayısının tavan değeri {tavan}")
            else:
                print("GEÇERSİZ İŞLEM !!")
        elif soru == "H":
            continue
        else:
            print("GEÇERSİZ İŞLEM !!")
    elif islem =="2":
        numb1 = int(input("Sayı 1: "))
        numb2 = int(input("Sayı 2: "))
        result = numb1 - numb2
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb1} - {numb2} = {result}")
        print("Sonucu taban ya da tavan değerlerine yuvarlamak ister misiniz?(Evet için 'E' - Hayır için 'H' - Çıkış 'Q')")
        soru = input("İşlem seçiniz :")
        if soru == "E":
            print(f"{result} değerini taban değerine yuvarlamak için 'TABAN', tavan değerine yuvarlamak için 'TAVAN' yazınız.")
            soru = input("İşlem seçiniz :")
            if soru == "TABAN":
                taban = math.ceil(result)
                print("Hesaplanıyor..")
                time.sleep(2)
                print(f"{result} sayısının taban değeri {taban}")
            elif soru == "TAVAN":
                tavan = math.floor(result)
                print("Hesaplanıyor..")
                time.sleep(2)
                print(f"{result} sayısının tavan değeri {tavan}")
            else:
                print("GEÇERSİZ İŞLEM !!")
        elif soru == "H":
            continue
        else:
            print("GEÇERSİZ İŞLEM !!")
    elif islem == "3":
        numb1 = int(input("Sayı 1: "))
        numb2 = int(input("Sayı 2: "))
        result = numb1 * numb2
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb1} * {numb2} = {result}")
        print("Sonucu taban ya da tavan değerlerine yuvarlamak ister misiniz?(Evet için 'E' - Hayır için 'H' - Çıkış 'Q')")
        soru = input("İşlem seçiniz :")
        if soru == "E":
            print(f"{result} değerini taban değerine yuvarlamak için 'TABAN', tavan değerine yuvarlamak için 'TAVAN' yazınız.")
            soru = input("İşlem seçiniz :")
            if soru == "TABAN":
                taban = math.ceil(result)
                print("Hesaplanıyor..")
                time.sleep(2)
                print(f"{result} sayısının taban değeri {taban}")
            elif soru == "TAVAN":
                tavan = math.floor(result)
                print("Hesaplanıyor..")
                time.sleep(2)
                print(f"{result} sayısının tavan değeri {tavan}")
            else:
                print("GEÇERSİZ İŞLEM !!")
        elif soru == "H":
            continue
        else:
            print("GEÇERSİZ İŞLEM !!")
    elif islem == "4":
        numb1 = int(input("Sayı 1: "))
        numb2 = int(input("Sayı 2: "))
        result = numb1 / numb2
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb1} / {numb2} = {result}")
        print("Sonucu taban ya da tavan değerlerine yuvarlamak ister misiniz?\n(Evet için 'E' - Hayır için 'H' - Çıkış 'Q')")
        soru = input("İşlem seçiniz :")
        if soru == "E":
            print(f"{result} değerini taban değerine yuvarlamak için 'TABAN', tavan değerine yuvarlamak için 'TAVAN' yazınız.")
            soru = input("İşlem seçiniz :")
            if soru == "TABAN":
                taban = math.ceil(result)
                print("Hesaplanıyor..")
                time.sleep(2)
                print(f"{result} sayısının taban değeri {taban}")
            elif soru == "TAVAN":
                tavan = math.floor(result)
                print("Hesaplanıyor..")
                time.sleep(2)
                print(f"{result} sayısının tavan değeri {tavan}")
            else:
                print("GEÇERSİZ İŞLEM !!")
        elif soru == "H":
            continue
        else:
            print("GEÇERSİZ İŞLEM !!")
    elif islem == "5":
        numb1 = int(input("Sayı 1: "))
        numb2 = int(input("Sayı 2: "))
        result = numb1 // numb2
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb1} / {numb2} = {result}")
    elif islem == "6":
        numb1 = int(input("Sayı 1:"))
        numb2 = int(input("Sayı 2:"))
        result = numb1 % numb2
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb1} / {numb2} işleminden kalan {result}")
    elif islem == "7":
        numb = int(input("Sayı :"))
        result = numb ** 2
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının karesi {result}")
    elif islem == "8":
        numb = int(input("Sayı :"))
        result = numb ** 3
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının küpü {result}")
    elif islem == "9":
        numb = int(input("Sayı :"))
        result = math.factorial(numb)
        print("Hesaplanıyor..")
        print(f"{numb} sayısının faktöriyeli {result}")
    elif islem == "10":
        numb = int(input("Sayı :"))
        result = math.cos(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} değerinin kosinüsü {result}")
    elif islem == "11":
        numb = int(input("Sayı :"))
        result = math.fabs(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının mutlak değeri {result}")
    elif islem == "12":
        numb1 = int(input("Sayı 1:"))
        numb2 = int(input("Sayı 2:"))
        result = math.gcd(numb1,numb2)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb1} ve {numb2} sayılarının en büyük ortak böleni {result}")
    elif islem == "13":
        print("İlk önce sayıyı giriniz.Sonra alınacak kuvvetini giriniz.")
        numb = int(input("Sayı :"))
        power = int(input("Kuvvet :"))
        result = math.pow(numb,power)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının {power}. kuvveti {result}")
    elif islem == "14":
        numb = int(input("Sayı :"))
        result = math.sin(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının sinüsü {result} (radyan cinsinden ölçülür)")
    elif islem == "15":
        numb = int(input("Sayı :"))
        result = math.sqrt(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının kare kökü {result}")
    elif islem == "16":
        numb = int(input("Sayı :"))
        result = math.tan(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının sinüsü {result} (radyan cinsinden ölçülür)")
    elif islem == "17":
        numb = int(input("Sayı :"))
        result = math.asin(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının yay sinüsü {result} (radyan cinsinden ölçülür)")
    elif islem == "18":
        numb = int(input("Sayı :"))
        result = math.atan(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısının yay tanjantı {result} (radyan cinsinden ölçülür)")
    elif islem  == "19":
        numb = int(input("Sayı :"))
        result = math.radians(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"{numb} sayısı radyan değeri {result}")
    elif islem == "20":
        numb = int(input("Sayı :"))
        result = math.trunc(numb)
        print("Hesaplanıyor..")
        time.sleep(2)
        print(f"Gerçek {numb} sayısının 0'a doğru en yakın İntegrale kadar kesimi {result}")
    elif islem == "Q" or islem == "q":
        print("Çıkış gerçekleşiyor..")
        time.sleep(2)
        break
    else:
        print("GEÇERSİZ İŞLEM !!")