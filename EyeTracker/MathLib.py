import math


def calc_accuracy(list_of_points, actual_point, d):
    try:
        theta_list = []
        for i in range(len(list_of_points)):
            theta_list.append(
                math.degrees(
                    math.atan(
                        math.sqrt(
                            math.pow(list_of_points[i][0] - actual_point[0], 2)
                            + math.pow(list_of_points[i][1] - actual_point[1], 2)
                        )*math.cos(math.radians(80))
                        / d
                    )
                )
            )
        return theta_list
    except:
        return -1


def calc_accuracy_avg(accuracy_list):
    try:
        return sum(accuracy_list) / len(accuracy_list)
    except:
        return -1


def calc_precision(list_of_points, actual_point, d):
    try:
        precision = 0
        accuracy_list = calc_accuracy(list_of_points, actual_point, d)
        avg_accuracy = calc_accuracy_avg(accuracy_list)
        n = len(accuracy_list)
        sum_of_all = 0
        for i in range(n):
            sum_of_all += pow(accuracy_list[i] - avg_accuracy, 2)
        precision = 1 / (n * sum_of_all)
        return math.sqrt(precision)
    except:
        return -1
