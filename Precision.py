from cmath import sqrt
from Accuracy import accuracy_average
from Accuracy import calc_accuracy


class Precision:
    def __init__(self):
        self.r = self.precision(calc_accuracy(type(list)),accuracy_average())


def precision(calc_accuracy(type(list)), accuracy_average()):
    r = 0
    n = 0
    for n in range(calc_accuracy(type(list))):
        r += n * (calc_accuracy(type(list))[:n] - accuracy_average())^2
    return sqrt(r*1/n)