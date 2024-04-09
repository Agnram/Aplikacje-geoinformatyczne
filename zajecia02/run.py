#przypisania
lsita = [1,(1,2), "abc", 123, "xyz"];
a, *b, c = lsita
# print(a,b,c)

a = 123
b = a
# print(a)

#Konwencja dotycząca nazewnictwa
_lista = [1,2,3]
#itp.

#tworzenie petli
#isinstance()
#zip()
#map()



a = 123
b = [1,2,3]
def zmien(x,y):
    x = "abcsd"
    y[0] = "zmienilo sie"
    print(f"Wewnatrz {x}, {y}")
    pass

# def duzo_arg (*args, **kwargs):
#     print(args)
#     print(kwargs)

# duzo_arg(1,2,3,4,5,6,c=22,b="qwerty")

print(a,b)
zmien(a,b)
print(a,b)



def zmien_wartosc(arg):
    if isinstance(arg, list):  # Sprawdzenie, czy arg jest listą
        arg[0] = 'kalafior'
    elif isinstance(arg, int):  # Sprawdzenie, czy arg jest integerem
        arg = 65482652
    return arg

# Przykłady użycia funkcji
# Dla listy
lista = [1, 2, 3]
print("Przed zmianą:", lista)
zmien_wartosc(lista)
print("Po zmianie:", lista)  # Output: ['kalafior', 2, 3]

# Dla integera
integer = 123
print("Przed zmianą:", integer)
zmien_wartosc(integer)
print("Po zmianie:", integer)

    