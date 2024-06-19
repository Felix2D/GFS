from numpy import *
from MATRIX import a

def TestS(Spieler):
    for i in range (len(a)):
        if  a[0][i] == a[1][i] == a[2][i] == Spieler:
            return True
        



#Erstelle die Methode TestS, welche die Spalten überprüft.
#Die vom "Spielfeld" übermittelte Variable ist die Spielernummer
