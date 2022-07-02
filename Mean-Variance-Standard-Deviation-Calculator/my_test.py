import sys
import numpy as np


def calculate(list):
    """Mean-Variance-Standard Deviation Calculator.
    Output the mean, variance, standard deviation,
    max, min, and sum of the rows, columns, and
    elements in a 3 x 3 matrix.
    :argument = list
    :returns = dict
    """
    try:
        if len(list) != 9:
            raise ValueError("List must contain nine numbers.")
    except ValueError:
        print("List must contain nine numbers.")
        sys.exit(1)
    try:
        for i in list:
            if type(i) == str:
                raise TypeError("List must contain only numbers not letters.")
    except TypeError:
        print("List must contain only numbers...")
        sys.exit(1)
    else:
        np_data = np.reshape(list, (1, 3, 3))
        calculations = {
            'mean': [
                (np.mean(np_data[0], axis=0).tolist()),
                (np.mean(np_data[0], axis=1).tolist()),
                np.mean(np_data)],
            'variance': [
                (np.var(np_data[0], axis=0).tolist()),
                (np.var(np_data[0], axis=1).tolist()),
                np.var(np_data)],
            'standard deviation': [
                (np.std(np_data[0], axis=0).tolist()),
                (np.std(np_data[0], axis=1).tolist()),
                np.std(np_data)],
            'max': [
                (np.max(np_data[0], axis=0).tolist()),
                (np.max(np_data[0], axis=1).tolist()),
                np.max(np_data)],
            'min': [
                (np.min(np_data[0], axis=0).tolist()),
                (np.min(np_data[0], axis=1).tolist()),
                np.min(np_data)],
            'sum': [
                (np.sum(np_data[0], axis=0).tolist()),
                (np.sum(np_data[0], axis=1).tolist()),
                np.sum(np_data)]
        }

    return calculations


# print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
# print(calculate([1, 2, 3, 4, 5, 6, 7, 8]))
# print(calculate([0, 'one', 2, 3, 4, 'five', 6, 7, 'eight']))
