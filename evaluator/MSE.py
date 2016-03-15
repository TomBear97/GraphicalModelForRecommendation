#!usr/bin/env python
#coding: utf-8


import numpy as np
from scipy.sparse import isspmatrix_dok

class MSE:
    def __init__(self):
        pass

    @staticmethod
    def ComputeMeanSquareError(recommendation, testRatings):
        ''''''
        if (not isspmatrix_dok(recommendation)) or (not isspmatrix_dok(testRatings)):
            assert('The recommendation matrix or test ratings is not a sparse matrix.')
            return 0.0
        loss = 0.0
        number = 0
        for r, c in recommendation:
            rating_post = recommendation[r, c]
            rating = testRatings[r, c]
            error = rating_post - rating
            loss += error * error
            number += 1
        if number == 0:
            return 0.0
        else:
            return loss / number

