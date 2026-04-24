import os
os.system("cls")

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
natija = []

for i in lst:
    yangi_tuple = i[:-1] + (100,)
    natija.append(yangi_tuple)

print(natija)