#    Numerische Verfahren fuer Materialwissenschaftler, Physiker und Wirtschaftsingenieure
#    Sommersemester 2026
#    Uebungsblatt 8 - Aufgabe 30

import numpy as np
import matplotlib.pyplot as plt
from random import randint


def sigmoid(x):
    '''
    Berechne die Sigmoid Funktion des Vektors x
    '''

    # Hinweis: Die Funktion np.exp(x) rechnet die Exponentialfunktion
    # komponentenweise aus.

    return  # [Code einfügen]


def backprop(x, y, W2, b2, W3, b3, a2, a3):
    '''
    Berechnet den Gradienten der Kostenfunktion bezüglich des Datenpukts (x, y).

    Die Parameter sind:
    - x, y:  Der Datenpunkt
    - W2, b2, W3 und b3:  Gewichte und Bias
    - a2 und a3:  Ausgangswerte der Schichten

    Die Funktion gibt zurück:
    - CW2:  Ableitung der Kostenfunktion bezüglich W2
    - Cb2:  Ableitung der Kostenfunktion bezüglich b2
    - CW3:  Ableitung der Kostenfunktion bezüglich W3
    - Cb3:  Ableitung der Kostenfunktion bezüglich b3
    '''

    # Berechne Ableitung bezüglich b1 und b2
    y3 = np.dot(W3, a2) + b3
    Cb3 = sigmoid(y3) * (1 - sigmoid(y3)) * (a3 - y)
    y2 = np.dot(W2, x)+b2
    Cb2 = sigmoid(y2) * (1 - sigmoid(y2)) * np.dot(W3.T, Cb3)

    # Berechne Ableitung bezüglich W1 und W2
    CW2 = np.outer(Cb2, x)
    CW3 = np.outer(Cb3, a2)

    return CW2, Cb2, CW3, Cb3


def F(x, W2, b2, W3, b3):
    '''
    Berechne die Ausgangswerte a2 und a3 der einzelnen Schichten des Netzwerks
    zur Eingabe x.
    '''

    # [Code einfügen]

    return a2, a3


def stochastic_gradient(X, Y, W2, b2, W3, b3, k=200000, lernrate=0.05):
    '''
    Führe k Schritt des stochastischen Gradientenverfahren aus. Dabei sind die
    Datenpunkte gegebe als die Zeilen (X[i], Y[i]) der Matrizen X und Y.
    W2, b2, W3 und b3 sind Gewichte und Bias des Netzwerks.
    '''

    for i in range(k):

        # Wähle zufälligen Index j aus der Datenmenge
        j = randint(0, X.shape[0]-1)

        # Berechne Ausgangswerte und Gradienten
        # Erneuere die Parameter

        # [Code einfügen]

        if i % 10000 == 0:
            print(f'Cost = {cost(X, Y, W2, b2, W3, b3)}')
            visualize(X, Y, W2, b2, W3, b3)


def cost(X, Y, W2, b2, W3, b3):
    '''
    Berechnet das Kostenfunktional.
    '''
    sum = 0
    for i in range(X.shape[0]):
        a1, a2 = F(X[i], W2, b2, W3, b3)
        err = Y[i] - a2
        sum += np.dot(err, err)
    return 0.5 / X.shape[0] * sum


def visualize(X, Y, W2, b2, W3, b3):
    '''
    Visualisiert die Datenpunkte und die Funktion F, die durch W2, b2, W3 und
    b3 gegeben ist.
    '''
    first = len(plt.get_fignums()) == 0
    if not first:
        plt.clf()

    # Visualisierung von F
    grid_x = np.linspace(0, 1, 20)
    grid_y = np.linspace(0, 1, 20)
    Y_grid = np.zeros((20, 20, 2))
    for (i, x) in enumerate(grid_x):
        for (j, y) in enumerate(grid_y):
            a2, a3 = F(np.array([x, y]), W2, b2, W3, b3)
            Y_grid[j, i] = a3
    z = Y_grid[:, :, 0] - Y_grid[:, :, 1]
    plt.contourf(grid_x, grid_y, z, [0, 100], colors=['#ccc'])
    plt.contour(grid_x, grid_y, z, [0])

    # Visualisierung der Datenpunkte
    color = []
    for i in range(X.shape[0]):
        if Y[i][0] == 1.:
            color.append("r")
        else:
            color.append("b")
    plt.scatter(X[:, 0], X[:, 1], c=color)
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    if not first:
        plt.draw()
        plt.pause(0.01)
    else:
        plt.draw()
        plt.pause(0.5)


if __name__ == '__main__':
    # Test der sigomid-Funktion
    x = np.linspace(-5, 5)
    plt.plot(x, sigmoid(x))
    plt.suptitle("sigmoid")
    plt.title("(Plot schließen, damit das Programm fortgesetzt wird)")
    plt.show()

    # Datenpunkte
    X = np.array([[0.1, 0.1], [0.3, 0.4], [0.1, 0.5], [0.6, 0.9], [0.4, 0.2], [0.6, 0.3], [0.5, 0.6], [0.9, 0.2], [0.4, 0.4], [0.7, 0.6]])
    Y = np.array([[1., 0.], [1., 0.], [1., 0.], [1., 0.], [1., 0.], [0., 1.], [0., 1.], [0., 1.], [0., 1.], [0., 1.]])
    plt.ion()

    # Zufällige Initialisierung der Gewichte und Biases
    W1 = np.random.standard_normal((3, 2))
    b1 = np.zeros(3)
    W2 = np.random.standard_normal((2, 3))
    b2 = np.zeros(2)

    # "Trainieren" des Netzwerkes
    stochastic_gradient(X, Y, W1, b1, W2, b2)

    plt.ioff()
    plt.show()
