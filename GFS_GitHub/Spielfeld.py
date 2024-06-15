import pygame
from pygame import *
from MATRIX import ArrayÄndern
from MATRIX import FeldFrei
from Diag import TestDiag
from Zeile import TestZ
from Spalte import TestS
pygame.init()

# Variablen/KONSTANTEN setzen
W, H = 800, 600
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
BLAU    = (0,0,255)
ROT     = (255, 0, 0)



SpielerNr=1

# Definieren und Öffnen eines neuen Fensters
fenster = pygame.display.set_mode((W, H))
pygame.display.set_caption("TicTacToe")
spielaktiv=True
clock = pygame.time.Clock()
fenster.fill(WEISS)
draw.rect(fenster,BLAU,[10,30,300,300])

for i in range(0,4):
    pygame.draw.line(fenster,SCHWARZ,[10,30+i*100],[310,30+i*100],2)
    pygame.draw.line(fenster,SCHWARZ,[10+i*100,30],[10+i*100,330],2)

def Zeichnen(y,x,SpielerNr):
    x=x*100+11
    y=y*100+31
    if x >=11 and x<=310 and y>=31 and y<=330:
       
        if SpielerNr==1:
            draw.ellipse(fenster,ROT,[x,y,98,98])
            

        else:
            draw.line(fenster, SCHWARZ,[x,y],[x+100,y+100],3)
            draw.line(fenster, SCHWARZ,[x+100,y],[x,y+100],3)

        ArrayÄndern(ZeilenNr,SpaltenNr,SpielerNr)
        
def Test(SpielerNr):
    if TestZ(SpielerNr) ==True or TestDiag(SpielerNr) ==True or TestS(SpielerNr) ==True:
        print("Gewonnen")        



# Schleife Hauptprogramm
while spielaktiv:

    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == MOUSEBUTTONDOWN:
            SpaltenNr= (mouse.get_pos()[0]-10)//100
            ZeilenNr= (mouse.get_pos()[1]-30)//100
            print(ZeilenNr, SpaltenNr)
            if FeldFrei(ZeilenNr,SpaltenNr):
                Zeichnen(ZeilenNr,SpaltenNr,SpielerNr)
                Test(SpielerNr)
                if SpielerNr==1:
                    SpielerNr=2
                else:
                    SpielerNr=1

            #print(f"{x}Spieler hat Taste gedrückt")
            
    # Spiellogik

    # Spielfeld löschen
    
    # Spielfeld/figuren zeichnen




        



    
    # Fenster aktualisieren
    
    pygame.display.flip()
    clock.tick(60)
quit()