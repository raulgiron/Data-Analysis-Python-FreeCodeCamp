import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
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
