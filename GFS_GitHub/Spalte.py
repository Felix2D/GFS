from numpy import *
from MATRIX import a

def TestS(Spieler):
    for i in range (len(a)):
        if  a[i][0] == a[i][1] == a[i][2] == Spieler:
            return True
        



#Erstelle die Methode TestS, welche die Spalten überprüft.
#Die vom "Spielfeld" übermittelte Variable ist die Spielernummer
