import sqlite3

class Product():
    def __init__(self,name,type,price):
        self.name = name
        self.type = type
        self.price = price

    def __str__(self):
        pass
        return f"Ürün ismi:{self.name}\nÜrün türü:{self.type}\nÜrün fiyatı:{self.price}"


class Market():
    def __init__(self):
        self.connection()

    def connection(self):
        self.connection = sqlite3.connect("supermarket.db")

        self.cursor = self.connection.cursor()

        ask = "CREATE TABLE IF NOT EXISTS supermarket (name TEXT, type TEXT, price FLOAT)"

        self.cursor.execute(ask)

        self.connection.commit()

    def show(self):
        ask = "SELECT * FROM supermarket"

        self.cursor.execute(ask)

        data = self.cursor.fetchall()

        if (len(data) == 0):
            print("Kayıtlı ürün bulunmuyor...")
        else:
            for i in data:
                product = Product(i[0],i[1],i[2])
                print(product,"\n")

    def question(self,name):
        ask = "SELECT name FROM supermarket WHERE name = ?"

        self.cursor.execute(ask,(name,))

        data = self.cursor.fetchall()

        if (len(data) == 0):
            print("Böyle bir ürün bulunmuyor....")
        else:

            product = Product(data[0][0],data[0][1],data[0][2])
            print(product)

    def named(self,product):
        ask = "INSERT INTO supermarket VALUES(?,?,?)"

        self.cursor.execute(ask,(product.name,product.type,product.price))

        self.connection.commit()

    def delete(self,name):
        ask = "DELETE FROM supermarket WHERE name = ?"

        self.cursor.execute(ask,(name,))