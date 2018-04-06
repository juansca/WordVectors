from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion

from tagging.embed import EmbeddingVectorizer


classifiers = {
    'logreg': LogisticRegression,
    'svm': LinearSVC,
}


def sent_feature_dicts(sent):
    X = [feature_dict(sent, i) for i in range(len(sent))]
    return X


def feature_dict(sent, i):
    w = sent[i]
    fs = {
        'w': w.lower(),
        'p': w[:2],
        's': w[-2:],
    }
    if i > 0:
        pw = sent[i-1]
        fs.update({
            'pw': pw.lower(),
            'pwp': pw[:2],
            'pws': pw[-2:],
        })
    return fs


class ClassifierTagger:
    """Simple and fast classifier based tagger.
    """

    def __init__(self, clf='svm'):
        """
        clf -- classifying model, one of 'svm', 'maxent' (default: 'svm').
        """
        self._clf = clf

        # build the pipeline
        vect = DictVectorizer()
        evect = EmbeddingVectorizer()
        clf = classifiers[clf]()
        self._pipeline = Pipeline([
            #('vect', vect),
            ('fu', FeatureUnion([
                ('vect', vect),
                ('evect', evect),
            ])),
            ('clf', clf),
        ])

    def fit(self, tagged_sents):
        """
        Train.

        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        # build feature dictionaries
        X, y = [], []
        for sent in tagged_sents:
            if sent:
                words, tags = zip(*sent)
                X += sent_feature_dicts(words)
                y += tags

        # train it
        print('Training classifier...')
        self._pipeline.fit(X, y)

        # build known words set:
        self._words = words = set()
        for sent in tagged_sents:
            if sent:
                word_sent, _ = zip(*sent)
                words.update(word_sent)

    def tag_sents(self, sents):
        """Tag sentences.

        sent -- the sentences.
        """
        X = []
        for sent in sents:
            X += sent_feature_dicts(sent)
        tags = self._pipeline.predict(X)

        result = []
        i = 0
        for sent in sents:
            j = i + len(sent)
            result.append(list(zip(sent, tags[i:j])))
            i = j
        return result

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        X = sent_feature_dicts(sent)
        result = self._pipeline.predict(X)
        return result

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return w not in self._words
