from numpy import *
from MATRIX import a

def TestDiag(spieler):

    if a[0][0] == a[1][1] == a[2][2] == spieler:
        return True

    if a[2][0] == a[1][1] == a[0][2] == spieler:
        return True

    
    