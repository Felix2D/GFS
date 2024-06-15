import numpy as np

a = np.zeros([3,3], dtype = np.int16)

def FeldFrei(x,y):
    if a[x][y]==0:
        return True
    
  

def ArrayÄndern(x,y,SpielerNr):

    
    a[x][y]=SpielerNr
    
    print(a)


