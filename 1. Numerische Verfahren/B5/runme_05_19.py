#    Numerische Verfahren fuer Materialwissenschaftler, Physiker und Wirtschaftsingenieure
#    Sommersemester 2025
#    Uebungsblatt 5 - Aufgabe 19

import numpy as np
import matplotlib.pyplot as plt


def grad(A, b, x, kmax=100):
    """ Verfahren des steilsten Abstiegs (Gradientverfahren). Voraussetzung: A spd """

    # Initialisierung der Iterationshistorie
    xhis = np.zeros((len(x), kmax+1))
    xhis[:, 0] = x

    ####

   
    # Initialisierung Residuum
    r = b -  np.dot(A, x) 
    # Iteration
    for k in range(1, kmax):
        a = (np.dot(r.T,r))/(np.dot(r.T, np.dot(A, r)))
        x = x + a * r
        xhis[:, k] = x
        r = r - a * np.dot(A, r)
       
    ###

    return (x, xhis)


if __name__ == '__main__':
    # Testbeispiel
    A = np.array([[1./50, 0], [0, 1]])
    b = np.array([1., 1])
    x0 = np.array([0., 0])

    (xgrad, xhis) = grad(A, b, x0)
   
    # Visualisiere das Konvergenzverhalten
    plt.figure()
    plt.plot(xhis[0, :], xhis[1, :], 'bo-', markersize=4, linewidth=1)
    plt.title('Typisches Konvergenzverhalten des Verfahrens des steilsten Abstiegs\n')
    plt.axis('equal')

    # Fuege Konturen-Plot hinzu, um die Hoehenlinien des Energiefunktionals
    # zu visualisieren
    delta = 0.25
    x = np.arange(min(xhis[0, :]) - 7.0, max(xhis[0, :]) + 7.0, delta)
    y = np.arange(-7.0, 9.0, delta)
    X, Y = np.meshgrid(x, y)
    (n1, n2) = X.shape
    n = n1 * n2
    xy = np.array([X.reshape(1, n)[0], Y.reshape(1, n)[0]])
    Z = np.zeros(n)
    for i in range(n):
        xyi = xy[:, i]
        Z[i] = 0.5 * np.dot(np.dot(A, xyi), xyi) - np.dot(b, xyi)
    Z = Z.reshape(n1, n2)      # Wert des Funktionals im Gitter X x Y
    plt.contour(X, Y, Z, 100)   # Konturlinien-Plot
    plt.plot(50.0, 1.0, 'r*')  # Die exakte Loesung

    plt.show()
