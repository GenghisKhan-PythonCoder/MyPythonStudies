import requests
from bs4 import BeautifulSoup

# ALTIN
url = "https://altin.doviz.com/gram-altin"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

altin = soup.find_all("div",{"class":"text-xl font-semibold text-white"})

print("ALTIN".center(50,"*",),"\n",altin)

# DOLAR
url = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

dolar = soup.find_all("div", {"class": "text-xl font-semibold text-white"})

print("DOLAR".center(50,"-"),"\n",dolar)

# EURO
url = "https://kur.doviz.com/serbest-piyasa/euro"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

euro = soup.find_all("div",{"class":"text-xl font-semibold text-white"})

print("EURO".center(50,"_"),"\n",euro)

