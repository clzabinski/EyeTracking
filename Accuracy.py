import math


class Accuracy:
    def __init__(self):
        self.average = self.accuracy_average()
        self.accuracy_list = self.calc_accuracy()

    def accuracy_average(self):
        sum = 0
        for x in self.accuracy_list:
            sum += x
        average = math.sqrt(sum)
        return average

    # This should make use of the data points gathered by Mr. North
    def calc_accuracy(
        self,
    ):
        result = []
        # d = placeholder for screen distance
        # xi, xj, yi, yj = coords from points
        theta = math.atan(math.sqrt(math.pow(xi - xj) - math.pow(yi - yj)) / d)
        result.append(theta)
        return result
