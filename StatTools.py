# This module holds all statistics functions implemented by me
import math

# Function takes in a dictionary and returns the correlation coefficient
def dictCorrelationCoeff(list, key1, key2):
    n = len(list)
    if n == 0:
        return 0
    key1Mean = 0
    key2Mean = 0
    for val in list:
        key1Mean += val.get(key1)
        key2Mean += val.get(key2)

    key1Mean = key1Mean / n
    key2Mean = key2Mean / n

    numeratorSum = 0
    key1NormSum = 0
    key2NormSum = 0

    for val in list:
        xVal = val.get(key1) - key1Mean
        yVal = val.get(key2) - key2Mean
        numeratorSum += xVal * yVal
        key1NormSum += xVal * xVal
        key2NormSum += yVal * yVal

    denomVal = math.sqrt(key1NormSum * key2NormSum)
    return numeratorSum/denomVal

