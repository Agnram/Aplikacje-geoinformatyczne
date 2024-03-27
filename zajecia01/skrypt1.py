
#print("Hello World")
#help(print)

# Moduły i przestrzenie nazw
from os import getcwd
import czas
import time
from importlib import reload

current_path = getcwd()

print(current_path)


print(czas.aktualny_czas)

time.sleep(20)

print(czas.aktualny_czas)

reload(czas)

print(czas.aktualny_czas)


