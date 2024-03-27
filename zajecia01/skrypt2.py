# Działania matematyczne
import math
import random

wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**12
tekst = str(potega)
wartosc_pi = math.pi
losowa = random.choice([1,2,3,4,5])

# Łańcuchy znaków

tekst =  f"Wartosc: {tekst}"
print(f"Dlugosc zmiennej tekst: {len(tekst)}, wykorzystanie wycinkow: {tekst[1:4]}")
print(dir(tekst))
tekst = tekst.upper()
print(f"Po zamianie na wielkie litery: {tekst}")
#tekst[2] = 'p'


# Listy
lista = list(tekst)
lista = lista[0:8]
lista.append([1,2,3,4,5])
lista.remove(":")
print(lista)

lista2 = [1,2,3,"banan",100]
lista3 = []
for i in lista2:
    if i != "banan":
        i=i**2
    lista3.append(i)
lista4 = list(range(2,17,2))

print(lista2, lista3, lista4)

# Slowniki
ja = {}
ja["imie"] = "Agnieszka"
ja["nazwisko"] = "Ramian"
ja["wiek"] = 21
ja["rodzice"] = [{"imie": "Danuta", "Wiek": 52}, {"imie": "Dariusz", "wiek": 52}]

print(ja["rodzice"])
print(ja["rodzice"][0]["imie"])
print(ja.keys())
print(ja.get("rodzenstwo"))

# Krotki
krotka1 =  (1,2,"3",4,2,5)
print(f"Dlugosc: {len(krotka1)}, pierwszy wyraz: {krotka1[0]}")
print(f"Wartosc 2 wystepuje {krotka1.count(2)} razy")
#krotka1[0] = 2

# Zbiory
X = set("kalarepa")
Y = set("lepy")
print(Y.intersection(X))

# Instrukcje
lista_imion = ["Anna", "Hanna", "Joanna"]
for i in enumerate(lista_imion):
    print(i)


if wartosc%2 == 0 and wartosc>0:
    print("Liczba jest dodatnia i parzysta")

# liczba = input()
# if liczba != 0:
#     print("Liczba jest różna od zera")

# koszyk = ['jabłko', 'banan', 'pomarańcza', 'kiwi', 'maliny']
# owoc = input()
# if owoc in koszyk:
#     print("Owoc jest dostępny")

# suma = 0
# liczba = 0
# while suma < 100:
#     liczba = input()
#     suma = suma + int(liczba)
# print(suma)


# “Dziwactwa”
# 1. Przypisanie tworzy referencje, a nie kopie
L = [1,2,3,4]
M = [1,2,3,L,4]
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow"
print(f"Wartość zmiennej M po zmianie L: {M}")

# 2. Powtórzenie dodaje jeden poziom zagłębienia
L = [4,5,6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")
L = [4,5,6]
Y = [list(L)] * 4
L[1] = "wow"
print(f"Y: {Y}")
Y[0][1] = "wow"
print(f"Y: {Y}")











