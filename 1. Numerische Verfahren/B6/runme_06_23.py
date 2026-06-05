#    Numerische Verfahren fuer Materialwissenschaftler, Physiker und Wirtschaftsingenieure
#    Sommersemester 2025
#    Uebungsblatt 6 - Aufgabe 23

import numpy as np
import matplotlib.pyplot as plt


def cg(A, b, x, tol=1e-4):
    """ Konjugiertes Gradientenverfahren. Voraussetzung: A spd """

    # Initialisierung

    k = 0
    xk = x.copy()
    norm_b = np.linalg.norm(b)

    kmax = 100
    r = b - np.dot(A,xk)
    d = r.copy()

    for k in range(kmax):
        a = np.dot(r.T, r)/np.dot(d.T, np.dot(A, d))
        xk = xk + a * d
        rold = r.copy()
        r = r - a * np.dot(A, d)
        d = r + (np.dot(r.T, r)/np.dot(rold.T, rold)) * d
        
        norm_axb = np.linalg.norm(np.dot(A, xk) - b)
        if norm_axb/norm_b <= tol:
            break

    # [Ihr Code hier]

    return (xk, k)


if __name__ == '__main__':

    Ns = [10, 20, 50, 100]
    for N in Ns:
        A = 2 * np.eye(N) - np.eye(N, k=1) - np.eye(N, k=-1)
        b = np.ones(N)
        x0 = np.zeros(N)

        print(f"Berechnung für Dimension n = {N} ...")
        (x, k) = cg(A, b, x0)
        print(f"{k} Iterationen benötigt\n")

        if N == Ns[-1]:
            plt.plot(x)
            plt.show()
