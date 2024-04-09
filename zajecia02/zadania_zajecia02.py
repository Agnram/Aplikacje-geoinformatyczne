import this
#Przypisania
#6
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print(rok, jezyk, wersja)
#7
oceny = [4,3,5,2,5,4]
pierwsza,*srodek,ostatnia = oceny
print(pierwsza,srodek, ostatnia)
#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, *_, zawod = info
print(imie, nazwisko, zawod)
#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok, (jezyk, wersja, (opis, _)) = dane
print(rok, jezyk, wersja, opis)

#Przypisania z wieloma celami i współdzielone referencje
#10
a = b = [1, 2, 3]
b[0] = 'zmieniono'
print(a, b)
#Zmiana b wplynela rowniez na a poniewarz b jest referencja do a
#Tak, listy są obiektami mutowalnymi
#11
c = a[:]
c[0] = "nowa wartosc"
print(a, b, c)
#Zmiana nie wplynela na a poniewaz c jest kopia poczatkowej wartosci a, a nie referencja
#12
x = y = 10
y += 1
print(x,y)
# Przypisanie x = y = 10 oznacza, ze x i y odnosza sie do tego samego obiektu. Zmiana y spowoduje, że będzie wstazywać na inną wartość, a x pozostanie bez zmian.
#Nie, intigery nie są obiektami mutowalnymi
#13
K = [1, 2]
L = K
K = K + [3, 4]
print(K)
print(L)
M = [1, 2]
N = M
M += [3, 4]
print(M)
print(N)
# Po konkatenacji, zmienna wskazuje na nową listę, a przypisanie rozszerzone modyfikuje istniejącą już listę.

#Techniki tworzenia pętli - uzupełnienie
#14
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]
for i in zip(imiona, oceny):
    print(i)
#15
liczby = [1, 2, 3, 4, 5]
def kwadrat(x):
    return x**2
for i in map(kwadrat, liczby):
    print(i)

#Argumenty
#16
def  zmien_wartosc(arg):
    if isinstance(arg,list):
        arg[0] = 'kalafior '
    elif isinstance(arg,int):
        arg = 65482652
    return arg
lst = ['kot','pies','koza']
nt =int(123)
zmien_wartosc(lst)
zmien_wartosc(nt)
print(lst,nt)
##############
#17
def zamowienie_produktu(nazwa_produktu: str,*,cena:float,ilosc: int=1) -> tuple[str, float]:
    
    lcena = cena*ilosc #wartosc zamowienia
    podsumowanie = "Nazwa produktu: " + nazwa_produktu + "\nlaczna cena: " + str(lcena) + "\nilosc zamowionego produktu: "+ str(ilosc)
    return podsumowanie, lcena

zamowienia = []
zamowienia.append(zamowienie_produktu("Kakao", cena=10, ilosc=12))
zamowienia.append(zamowienie_produktu("Cukier", cena=15, ilosc=6))
zamowienia.append(zamowienie_produktu("Rum", cena=20))

for zamowienie in zamowienia:
    print(zamowienie[0])

suma_zamowien = sum(zamowienie[1] for zamowienie in zamowienia)
print(suma_zamowien, "zł")

#18


#Funkcje fabrykujące - obiekty funkcji, które pamiętają wartości w otaczających zasięgach
#19
def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj
potega_2 = stworz_funkcje_potegujaca(2) # Tworzy funkcję potęgującą do kwadratu
print(potega_2(4)) # Wynik: 16
#20 - a
def licznik():
    count = 0
    def inkrementacja():
        nonlocal count
        count += 1
        return count
    return inkrementacja
#20 - b
count = 0
def licznik():
    global count
    count += 1
    return count
#20 - c
class Licznik:
    def __init__(self):
        self.count = 0
        
    def __call__(self):
        self.count += 1
        return self.count
#20 - d
def licznik():
    if not hasattr(licznik, 'count'):
        licznik.count = 0
    licznik.count += 1
    return licznik.count

#Adnotacje
#21 -> patrz funkcja zamowienie_produktu (#17)

#Funkcje anonimowe – lambda
#22
ksiazki = [
    {'tytul': 'Balladyna', 'autor': 'Juliusz Slowacki', 'rok_wydania': 1234},
    {'tytul': 'Dziady cz.III', 'autor': 'Adam Mickiewicz', 'rok_wydania': 2020},
    {'tytul': 'Lalka', 'autor': 'Buleslaw Prus', 'rok_wydania': 2002},
    {'tytul': 'Hamlet', 'autor': 'William Shakespeare', 'rok_wydania': 1111}
]
# a. Sortowanie książek według roku wydania
posortowane = sorted(ksiazki, key=lambda x: x['rok_wydania'])
print("Posortowane ksiazki: ")
for k in posortowane:
    print(k)
# b. Filtracja książek wydanych po 2000 roku
po_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, ksiazki))
print("Wydane po 2000 roku:")
for k in po_2000:
    print(k)
# c. Transformacja listy do listy tytułów
tytuly = list(map(lambda x: x['tytul'], ksiazki))
print("Tytuły:")
print(tytuly)

#Generatory – funkcje generatorów i wyrażenia generatorów
#23
def dni_tygodnia():
    dzien = "poniedziałek"
    while True:
        yield dzien
        if dzien == "niedziela":
            break
        dzien = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"][(["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"].index(dzien) + 1)]
for dzien in dni_tygodnia():
    print(dzien)
trzy_dni = []
generator = dni_tygodnia()
for _ in range(3):
    trzy_dni.append(next(generator))
print(trzy_dni)

#Pakiety modułów
#24















