from  __future__  import division

#    Numerische Verfahren fuer Materialwissenschaftler, Physiker
#    und Wirtschaftingenieure
#    Sommersemester 2025
#    Uebungsblatt 4 - Aufgabe 15
#
#    Mustermann, Max - Gruppe 99
#    max.mustermann@uni-a.de

import numpy as np
# l = A[j+1:n,j]/A[j,j]

#         A[j+1:n,j] = A[j+1:n,j] - l * A[j,j]
#         temp[j+1:n,j] = l
# print(temp[j+1,j+2:n] )
    #     temp[j+1,j+2:n] = A[j+1, j+2:n] - l * 
    # print("A nacher: ",A)
    # print("temp: ",temp)
def lr(A):
    '''
    Ueberschreibe die Matrix A mit den Eintraegen von L und R.
    Das Anlegen von Frobenius-Matrizen L_i ist VERBOTEN!
    '''
    n = A.shape[0]  # Anzahl der Zeilen von A.    
    temp = A.copy()
    ltemp = []
    for j in range(n-1):
        A[j+1:,j] = A[j+1:,j]/A[j,j]  
        A[j+1:,j+1:] -= np.outer(A[j+1:,j], A[j,j+1:])
        #temp[j+1:n, j:n] = temp[j+1:n, j:n] - l[:, np.newaxis] * A[j, j:n]
        #temp[j+1:n,j] = l
        
        #print(temp)
    #     ltemp.append(l)
       
    # gesamt = np.concatenate(ltemp)
    # print(gesamt)
    # i, c = 0, 0
    # for i in range(n):
    #     temp[i+1,c:] = temp[i+1,c:] - l * A[i,]
    #     if(i+1 == n): 
    #         c +=1
            
        
        
   


    return A

def forw_sub(LR, b):
    '''
    Loese Lz = b durch Vorwaertssubstitution, wobei L untere Dreiecksmatrix.
    Beachte: Die Einsen auf der Diagonalen von L sind in der Matrix LR
             nicht eigens abgespeichert und werden soz. hinzugedacht.
    '''
    z = np.zeros_like(b)
    z[0] = b[0]  # Wir haben uns gespart: .. / L_00, denn L_ii = 1.
    for i in range(1,len(b)):
        
        z[i] = b[i] - np.dot(LR[i,0:i], z[0:i])
        
    return z 

def backw_sub(LR, z):
    '''
    Loese Rx = z durch Rueckwaertssubstitution, wobei R obere Dreiecksmatrix.
    '''
    
    x = np.zeros_like(z)
    for i in range(len(z)-1, -1, -1):
        x[i] = z[i] - np.dot(LR[i,i+1:], x[i+1:]) / LR[i,i]
    return x    

def solveAxb(A, b):    
    LR = lr(A)
    z = forw_sub(LR, b)
    x = backw_sub(LR, z)
    return x
    
if __name__ == '__main__':
    # Testproblem mit verschiedenen Dimensionen.
    
    # #A = np.array([[1,2,1,3], [3,2,9,4], [1,2,1,2], [1,2,1,2]])
    # A = np.array([[1,2,1],[2,5,2],[1,2,1]])
    # b = np.array([1,902913,2])
    # # print("A: ",A)
    # # lr(A)
    # LR = lr(A.copy())
    # z = forw_sub(LR, b.copy())
  
    N = [5, 50, 500]
    for n in N:
    
        # [Code einfuegen: A und b definieren.]    
        A = 2*np.eye(n) - np.eye(n,n,-1) - np.eye(n,n,+1)
        i = np.arange(n)
        b = i
        x = solveAxb(A.copy(), b.copy())    # Wichtig: Verwende .copy()!
        print(x)
        #  Warum NICHT(!) so:  x = solveAxb(A, b)  ?
        #
        xx = np.linalg.solve(A,b)
        print(xx)
        #
        res = b - np.dot(A, x)
        norm = np.linalg.norm
        print('Residuum fuer n=%d: %.2e' % (n, norm(res)/norm(b)))
