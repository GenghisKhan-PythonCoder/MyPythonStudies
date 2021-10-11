from song import *
import time

print("""
-------------------------------------------------
Şarkı Listesi Programına Hoşgeldiniz.

1.Şarkıları Göster

2.Şarkı Sorgula

3.Şarkı Ekle

4.Şarkı Sil

Çıkış 'q'
-------------------------------------------------
""")

song = Data()

while True:

    islem = input("İşlem seçiniz: ")

    if islem == "q":
        print("Program sonlanıyor...\nYine bekleriz.")
        break

    elif islem == "1":
        song.show_songs()

    elif islem == "2":
        name = input("Hangi şarkıyı sorguluyorsunuz?: ")
        print(f"{name} isimli şarkı sorgulanıyor.")
        time.sleep(2)
        song.question_song(name)

    elif islem == "3":
        name = input("Şarkı ismi: ")
        artist = input("Sanatçı ismi: ")
        album = input("Albüm adı: ")
        production = input("Prodüksiyon şirketi: ")
        time1 = float(input("Şarkı süresi (Örn: 3.15): "))

        new = Song(name,artist,album,production,time1)

        print("Şarkı ekleniyor....")
        time.sleep(2)

        song.add_song(new)
        print("Şarkı eklendi.")

    elif islem == "4":
        name = input("Hangi şarkıyı silmek istiyorsunuz?: ")
        ask = input("Emin misiniz? (H/E)")

        if ask == "E":
            print("Şarkı siliniyor....")
            time.sleep(2)

            song.del_song(name)
            print("Şarkı silindi.")
        elif ask == "H":
            print("Silme işlemi gerçekleştirilmedi.")
        else:
            print("Geçersiz işlem!!\nHerhangi bir işlem gerçekleştirilmedi.")

    else:
        print("Geçersiz İşlem....")