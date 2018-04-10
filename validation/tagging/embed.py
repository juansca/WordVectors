import fasttext
import numpy as np
import os
from sklearn.base import BaseEstimator, TransformerMixin


class EmbeddingVectorizer(BaseEstimator, TransformerMixin):

    def __init__(self, filename='vectors/100_1.bin', is_bin=True):
        root_dir = os.getcwd()
        filename = os.path.join(root_dir, filename)
        self._is_bin = is_bin
        self._filename = filename
        print("Using vectors from {}".format(filename))
        if is_bin:
            self._wv = fasttext.load_model(filename, encoding='utf-8')
        else:
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
        if self._is_bin:
            return [np.array([float(s) for s in self._wv[x['w']]]) for x in X]
        else:
            return [self._wv.get(x['w'], np.zeros(self._ndim)) for x in X]
