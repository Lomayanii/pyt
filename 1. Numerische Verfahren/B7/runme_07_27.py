#    Numerische Verfahren fuer Materialwissenschaftler, Physiker und Wirtschaftsingenieure
#    Sommersemester 2025
#    Uebungsblatt 7 - Aufgabe 27

import numpy as np
import matplotlib.pyplot as plt


def buildAb(data, n):
    '''
    Input:
    data: numpy-Array der Dimension m x 2
    n:    (Grad+1) des gewuenschten Ausgleichspolynoms (Bsp: n=2 => Gerade)

    Output:
    A:  Matrix des Ausgleichsproblems; viele Zeilen, n Spalten
    b:  rechte Seite des APs

    Algorithmus:
    Mit der ersten Spalte aus data wird die Matrix A definiert,
    mit der zweiten Spalte die rechte Seite b.
    Stellen Sie A so auf, dass die Ausgaben am Ende des Programms
    "print ( 'Ausgleichsgerade:  g(z) = %g + %g z' % (a[0],a[1]) )"
    (zweiter Aufgabenteil analog) korrekt sind.
    '''
   
    # Dimensionen der Input-Daten pruefen
    (m, q) = data.shape
    if q != 2:
        message = 'Falsche Dimension der Daten: ' + str(m) + ' x ' + str(q)
        raise ValueError(message)
    if n > m:
        raise ValueError('Zu wenige Messwerte fuer gewuenschten Polynomgrad')

    # Arrays A und b aufstellen
    A = np.zeros((m,2))
    A[:, 0] = data[:, 0]
    A[:, 1] = 1
    b = data[:, 1]
    
    return (A, b)


def linAP(data, n=2):
    '''
    Loese das lineare Ausgleichsproblem
    'Polynom vom Grad n-1 durch die (x,y)-Daten data'.
    Resultat sind die Koeffizienten des Ausgleichspolynoms vom Grad n-1
    (Default: Ausgleichsgerade).
    '''

    # Erstelle A und b aus den Daten
    A, b = buildAb(data, n)

    # Loese nun das Ausgleichsproblem durch Loesen der Normalengleichungen
    A_A = np.dot(A.T, A)
    b = np.dot(A.T, b)
    print("hi")
    x = np.linalg.solve(A_A, b)
    print("bu")

    # x enthaelt die Koeffizienten des gesuchten Ausgleichpolynoms vom Grad (n-1)
    return x


def horner(coeff, x):
    '''
    Werte das Polynom p mit Koeffizienten coeff in den Punkten (!) x mittels
    Horner-Schema aus. Diese Form der Auswertung ist erheblich effizienter
    als die Standard-Version   p(x) = sum{i=0..n}(coeff[i]*x**i) .
    Beide Parameter sind als np.array anzugeben. Das Ergebnis ist ein Vektor,
    mit  p[i] = p(x[i]).
    '''
    n = len(coeff)
    p = coeff[n-1] * np.ones_like(x)
    for i in range(n-2, -1, -1):
        p = p * x + coeff[i]
    return p


def visualizeAP(data, n, x, h=0.1, off=0.5):
    '''
    Visualisiere Messpunkte und Ausgleichs-Polynom
    Input:
    data: Messpunkte (m,2), d.h. Matrix mit 2 Koordinaten pro Zeile
    n:    (Grad+1) des Ausgleichs-Polynoms
    x:    Koeffizienten des Ausgleichspolynoms
    h:    Schrittweite der Stellen, an denen das Polynom fuer die Grafik ausgewertet werden soll
    off:  Offset der Stellen, an denen das Polynom fuer die Grafik ausgewertet werden soll

    Die Grafik wird an die X-Ordinaten [x_min-off,x_max+off] angepasst.
    Das Ausgleichspolynom wird im Intervall [x_min-off+h,x_max+off-h] gezeichnet.
    h und off sind 'optionale Parameter'; wenn nicht anders angegeben, haben
    sie den im Header genannten Wert. Beide haben lediglich grafischen Einfluss.
    '''
    plt.figure()

    # Erstelle Graphen (zh, fh) des Ausgleichspolynoms.
    mindata = min(data[:, 0])
    maxdata = max(data[:, 0])
    zh = np.arange(mindata - off+h, maxdata + off, h)
    fh = horner(x, zh)

    # Plotte die gegebenen Daten und den Graphen.
    plt.plot(data[:, 0], data[:, 1], 'ro', markersize=7)
    plt.plot(zh, fh, 'b-', linewidth=2.5)
    plt.axis('equal')

    # Beschriftung.
    agp = 'Ausgleichspolynom vom Grad ' + str(n-1)
    if n == 2:
        agp = 'Ausgleichsgerade'
    title = agp + ' zu ' + str(data.shape[0]) + ' Messwerten\n'
    plt.title(title, fontsize=18)

    # Ausgabe der Polynomgleichung im Bild.
    ndigits = 2    # Legt Anzahl der ausgegebenen Nachkommastellen fest.
    equ = 'Polynom p(z) ='
    for i in range(n-1, -1, -1):
        # Haenge termweise an: Vorzeichen Koeffizient Monom.
        sign = (' - ' if x[i] < 0 else (' + ' if i < n-1 else ' '))
        number = str(round(abs(x[i]), ndigits))
        monom = ('z^' + str(i) if i >= 2 else ('z' if i == 1 else ''))
        equ += (sign + number + monom)
    plt.text(mindata-off+h, max(fh), equ, fontsize=16)
    plt.show()
    return


if __name__ == '__main__':

    n = 2
    # Testproblem 1.
    data1 = np.array([[0, 0], [1, 1], [2, 2], [3, 2]], dtype=float)
    a = linAP(data1, n)
    visualizeAP(data1, n, a)
    print(a)
    print('Ausgleichsgerade:  p(z) = %g + %g z' % (a[0], a[1]))
    #  Korrekte Loesung:  g(z) = 0.2 + 0.7 z

    # # Testproblem 2.
    # data2 = np.genfromtxt('Messwerte.txt', delimiter=',', dtype=float)
    # b = linAP(data2, n)
    # visualizeAP(data2, n, b)
    # print(b)
    # print('Ausgleichsgerade:  p(z) = %g + %g z' % (b[0], b[1]))
    # # Korrekte Loesung: 0.563364 + 0.9281 z
