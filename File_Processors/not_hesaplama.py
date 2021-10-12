def not_hesapla(satir):
    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "-" + harf + "\n"

def kalan_bul(satir):
    satir = satir[:-1]
    liste = satir.split("-")

    if liste[1] == "FF":
        return liste[0] + "-" + liste[1] + "\n"
    else:
        pass

def gecen_bul(satir):
    satir = satir[:-1]
    liste = satir.split("-")

    if liste[1] != "FF":
        return liste[0] + "-" + liste[1] + "\n"
    else:
        pass


with open("dosya.txt","r",encoding="utf-8")as file:
    eklenecekler_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    print(eklenecekler_listesi)

with open("notlar.txt","w",encoding="utf-8")as file2:

    for i in eklenecekler_listesi:
        file2.write(i)

#-----------------------------------------------------------------------

with open("notlar.txt","r",encoding="utf-8")as file3:
    kalanlar_listesi = []

    for i in file3:
        kalanlar_listesi.append(kalan_bul(i))

    print(kalanlar_listesi)

with open("kalanlar.txt","w",encoding="utf-8")as file4:
    for i in kalanlar_listesi:
        i = str(i)
        file4.write(i)

#------------------------------------------------------------------------

with open("notlar.txt","r",encoding="utf-8")as file5:
    gecenler_listesi = []

    for i in file5:
        gecenler_listesi.append(gecen_bul(i))

    print(gecenler_listesi)

with open("gecenler.txt","w",encoding="utf-8")as file6:
    for i in gecenler_listesi:
        i = str(i)
        file6.write(i)