import math


def calc_accuracy(list_of_points, actual_point, d):
    theta_list = []
    for i in range(list_of_points):
        theta_list.append(
            math.atan(
                math.sqrt(
                    math.pow(list_of_points[i].x - actual_point.x, 2)
                    + math.pow(list_of_points[i].y - actual_point.x, 2)
                )
                / d
            )
        )
    return theta_list


def calc_accuracy_avg(list_of_points, actual_point, d):
    accuracy_list = calc_accuracy(list_of_points, actual_point, d)
    return sum(accuracy_list) / len(accuracy_list)


def calc_precision(list_of_points, actual_point, d):
    precision = 0
    accuracy_list = calc_accuracy(list_of_points, actual_point, d)
    avg_accuracy = calc_accuracy_avg(list_of_points, actual_point, d)
    n = len(accuracy_list)
    sum_of_all = 0
    for i in range(n):
        sum_of_all += pow(accuracy_list[i] - avg_accuracy, 2)
    precision = 1 / (n * sum_of_all)
    return math.sqrt(precision)
