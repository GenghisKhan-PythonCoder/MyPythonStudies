class animal():
    def __init__(self,type,nutrition,redroductive):
        print(">> Hayvan sınıfı init fonksiyonu <<")
        self.type = type
        self.nutrition = nutrition
        self.redroductive = redroductive
    def information(self):
        print("*** Hayvan Sınıfı Bilgileri ***")
        print(f"TÜRÜ:{self.type}\nBESLENME:{self.nutrition}\nÜREME:{self.redroductive}\n")

class dog(animal):
    def __init__(self,name,type,nutrition,redroductive,size):
        super(dog, self).__init__(type,nutrition,redroductive)
        print(">> Köpek sınıfı init fonksiyonu <<")
        self.name = name
        self.size = size
    def information(self):
        print("*** Köpek Sınıfı Bilgileri ***")
        print(f"AD:{self.name}\nTÜR:{self.type}\nBESLENME:{self.nutrition}\nBOYUT:{self.size}\nÜREME:{self.redroductive}\n")


class bird(animal):
    def __init__(self,name,type,nutrition,redroductive,size):
        super(bird, self).__init__(type,nutrition,redroductive)
        print(">> Kuş sınıfı init fonksiyonu <<")
        self.name = name
        self.size = size
    def information(self):
        print("*** Kuş Sınıfı Bilgileri ***")
        print(f"AD:{self.name}\nTÜR:{self.type}\nBESLENME:{self.nutrition}\nBOYUT:{self.size}\nÜREME:{self.redroductive}\n")

class horse(animal):
    def __init__(self,name,type,nutrition,redroductive,size):
        super(horse, self).__init__(type,nutrition,redroductive)
        print(">> At sınıfı init fonksiyonu <<")
        self.name = name
        self.size = size
    def information(self):
        print("*** At Sınıfı Bilgileri ***")
        print(f"AD:{self.name}\nTÜR:{self.type}\nBESLENME:{self.nutrition}\nBOYUT:{self.size}\nÜREME:{self.redroductive}")


animal1 = animal("Köpek","Etcil","Eşeyli")
animal2 = animal("Kuş","Etcil&Otcul","Eşeyli")
print(animal1.information(),animal2.information())

dog1 = dog("Dost","Golden","Etcil","Eşeyli","Büyük")
dog2 = dog("Bulut","Kangal","Etcil","Eşeyli","Büyük")
print(dog1.information(),dog2.information())

bird1 = bird("Kartal","Kaya Kartalı","Etcil","Eşeyli","Büyük")
bird2 = bird("Kanarya","Sarı Kanarya","Otcul","Eşeyli","Küçük")
print(bird1.information(),bird2.information())

horse1 = horse("Yağız","Arap Atı","Otcul","Eşeyli","Büyük")
horse2 = horse("Serin","İngiliz Atı","Otcul","Eşeyli","Büyük")
print(horse1.information(),horse2.information())