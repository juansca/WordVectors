import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class EmbeddingVectorizer(BaseEstimator, TransformerMixin):

    def __init__(self, filename='vectors/300_3.vec'):
        self._filename = filename
        f = open(filename)
        line0 = f.readline().split()
        self._ndim = int(line0[1])
        self._wv = wv = {}
        for line in f:
            line = line.split()
            word = line[0]
            vec = np.array([float(s) for s in line[1:]])
            wv[word] = vec

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return [self._wv.get(x['w'], np.zeros(self._ndim)) for x in X]
