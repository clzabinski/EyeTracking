from math import sqrt


def FindMiddlePoint(inputarr_x, inputarr_y):
    val_x = sum(inputarr_x) / len(inputarr_x)
    val_y = sum(inputarr_y) / len(inputarr_y)
    return (val_x, val_y)


def DetectOutlier(inputarr_x, inputarr_y):
    threshhold = 200
    val_x, val_y = FindMiddlePoint(inputarr_x, inputarr_y)
    for index, coord in enumerate(inputarr_x):
        # print(index, coord)
        # print("Coords = " + str(coord) + ":" +  str(inputarr_y[index]))
        distance_from_middlepoint = sqrt(
            pow((coord - val_x), 2) + pow(inputarr_y[index] - val_y, 2)
        )
        # print(distance_from_middlepoint)
        if distance_from_middlepoint > threshhold:
            # print("Detecting outlier, eliminating")
            inputarr_x.remove(coord)
            del inputarr_y[index]

    return FindMiddlePoint(inputarr_x, inputarr_y)


print(DetectOutlier([1, 2, 3, 123], [4, 5, 6, 431]))