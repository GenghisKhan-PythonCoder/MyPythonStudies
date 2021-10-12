def besiktas(player):
    player = player[:-1]
    player = player.split(",")
    p_b = []

    if player[1]=="Beşiktaş":
        return player[0] + "," + player[1] + "\n"

def galatasaray(player):
    player = player[:-1]
    player = player.split(",")

    if player[1]=="Galatasaray":
        return player[0] + "," + player[1] + "\n"

def fenerbahce(player):
    player = player[:-1]
    player = player.split(",")

    if player[1]=="Fenerbahçe":
        return player[0] + "," + player[1] + "\n"

# ----- FUTBOLCULAR -----
with open("futbolcular.txt","w",encoding="utf-8")as f:
    f.write("Fernando Muslera,Galatasaray\nAtiba Hutchinson,Beşiktaş\nSimon Kjaer,Fenerbahçe\n")

# ----- BEŞİKTAŞ -----

with open("futbolcular.txt","r",encoding="utf-8")as f_besiktas:
    bjk_player = []

    for i in f_besiktas:
        bjk_player.append(besiktas(i))

    print(bjk_player)

with open("bjk.txt","w",encoding="utf-8")as f_besiktas1:
    for i in bjk_player:
        i= str(i)
        f_besiktas1.write(i)

# ----- GALATASARAY -----

with open("futbolcular.txt","r",encoding="utf-8")as f_galatasaray:
    gs_player = []

    for i in f_galatasaray:
        gs_player.append(galatasaray(i))

    print(gs_player)

with open("gs.txt","w",encoding="utf-8")as f_galatasaray1:
    for i in gs_player:
        i = str(i)
        f_galatasaray1.write(i)

# ----- FENERBAHÇE -----

with open("futbolcular.txt","r",encoding="utf-8")as f_fenerbahce:
    fb_player = []

    for i in f_fenerbahce:
        fb_player.append(fenerbahce(i))

    print(fb_player)

with open("fb.txt","w",encoding="utf-8")as f_fenerbahce1:
    for i in fb_player:
        i = str(i)
        f_fenerbahce1.write(i)