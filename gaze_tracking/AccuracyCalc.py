import math

class Accuracy():

    def calcaccuracy(self, point, base, d):#Make this use a point class

        theta = math.atan(math.sqrt(math.pow(point.x-base.x)+math.pow(point.y-base.y))/d)

        return theta

    def calcaccuracylist(self, list, base, d):
        result = [1]
        for x in list:
            result.append(math.atan(math.sqrt(math.pow(x.x-base.x)-math.pow(x.y-base.y))/d))

        return result

    def calcaccuracyavelist(self, list):
        result = 0
        for x in list:
           result = x + result

        result = result/list.count
        return result