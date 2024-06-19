from numpy import *
from MATRIX import a
#Erstelle die Methode TestZ, welche die Zeilen überprüft.
#Die vom "Spielfeld" übermittelte Variable ist die Spielernummer

def TestZ(Spieler):
    temp =0
    for y in range(3):
        if a[0][y] == a[1][y] == a[2][y] == Spieler:
            return True
