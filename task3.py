# run command : python task3.py 'x*4+x*x*x-2'

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

from termer import term_eval


def main(input):

    X = np.array([-4, -2, -1, 4, 5, 6, 7, 8])
    Y = np.array([])

    for x in X:
        term = input.replace("x", str(x))
        y = int(term_eval(term))
        Y = np.append(Y, y)

    X_Y_Spline = make_interp_spline(X, Y)

    X_ = np.linspace(X.min(), X.max(), 50)
    Y_ = X_Y_Spline(X_)

    plt.plot(X_, Y_)
    plt.title("y = " + input)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


main((sys.argv[1]))
