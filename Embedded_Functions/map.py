def alan(x):
    return x[0]*x[1]

d = [(3,4),(10,3),(5,6),(1,9)]

liste = list(map(alan,d))
print(liste)