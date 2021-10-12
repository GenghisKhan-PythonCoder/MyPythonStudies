import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

#function
def s(i):
    a = i.split(",")
    return a

#persons and mails
persons = []
mails = []
with open("mails.txt","r",encoding="utf-8")as file:
    for i in file:
        a= (s(i))
        persons.append(a[0])
        mails.append(a[1])

#messega send
for i,j in zip(persons,mails):
    messega = MIMEMultipart()
    messega["From"] = "deneme.48.hesabi.48@gmail.com"
    messega["To"] = f"{str(j)}"
    messega["Subject"] = f"{str(i)}"

    send = """
    Proje 2
    
    Elinizde 5 kişinin maillerinin ve isimlerinin bulunduğu bir dosya olsun. 
    Bu dosyayı okuyarak, her bir kişiye isimleriyle beraber mail göndermeye çalışın.
    
    MISSION COMPLETE
    """

    messega_body = MIMEText(send,"plain")
    messega.attach(messega_body)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("deneme.48.hesabi.48@gmail.com","48deneme48")
        mail.sendmail(messega["From"],messega["To"],messega.as_string())
        print("Mail başarıyla gönderildi....")
        mail.close()
    except:
        sys.stderr.write("Mail göndermesi başarısız oldu...")
        sys.stderr.flush()