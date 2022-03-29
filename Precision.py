from cmath import sqrt


class Precision:
    def __init__(self, accuracy_list, average):
        self.r = self.__precision__(accuracy_list, average)

    def __precision__(self, accuracy_list, average):
        r = 0
        n = len(accuracy_list)
        for i in range(len(accuracy_list)):
            r += i * (i - average) ^ 2
        return sqrt(r * 1 / n)
