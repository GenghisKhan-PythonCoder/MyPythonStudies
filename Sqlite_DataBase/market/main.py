from market import *

print("""
-------------------------------------------------
SUPER MARKET ÜRÜNLER PROGRAMI
*****************************
1) Ürünleri göster

2) Ürün ara

3) Ürün ekle

4) Ürün sil

Çıkış 'q'

-------------------------------------------------
""")

product = Market()

while True:
    select = input("İşlem seçiniz: ")

    if select == "q":
        print("Çıkış gerçekleşiyor........")
        break

    elif select == "1":
        product.show()

    elif select == "2":
        name = input("Ürün adı: ")

        time.sleep(2)

        product.question(name)

    elif select == "3":
        name = input("Ürün adı: ")
        type = input("Ürün türü: ")
        price = input("Ürün fiyatı: ")

        product_ = Product(name,type,price)

        product.add(product_)

    elif select == "4":
        name = input("Ürün adı:")

        ask = input("Silmek istediğinize emin misiniz? (E/H): ")

        if ask == "E":
            product.delete(name)
        elif ask == "H":
            print("Ürün silmekten vazgeçtiniz.")
        else:
            print("Geçersiz işlem !!!\nHerhangi bir işlem gerçekleştirilmedi.")

    else:
        print("Geçersiz İşlem !!!")