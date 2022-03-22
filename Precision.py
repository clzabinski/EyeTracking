from cmath import sqrt


class Precision:
    def __init__(self):
        self.r = precision(,)


def precision(theta_i_list, theta_average):
    r = 0
    for n in range(theta_i_list):
        r += n * (theta_i_list[:n] - theta_average)^2
    return sqrt(r*1/n)