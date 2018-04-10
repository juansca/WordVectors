"""Train a sequence tagger.

Usage:
  train.py [-m <model> [-c <clasifier>]] -i <file> [-b <yn> -M <yn>] -o <file>
  train.py -h | --help

Options:
  -m <model>    Model to use [default: ct]
  -i <file>     File containing word embeddings
  -b <yn>       To say if the file is a fasttext binary model ('y')
                or vector's text file ('n')
  -M <yn>       If you want to generate the confusion matrix ('y') or not ('n').
                That is only on the case that a binary file was given

  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import os

from corpus.ancora import SimpleAncoraCorpusReader
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

from tagging.classifier import ClassifierTagger
from eval_tagger import evaluate


models = {
    'ct': ClassifierTagger,
}

clasifiers = {
    'multinomial': MultinomialNB,
    'linear': LinearSVC,
    'LogisticRegression': LogisticRegression
}

if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    actual_dir = os.path.dirname(os.path.abspath(__file__))
    corpus = SimpleAncoraCorpusReader(actual_dir + '/corpus/ancora/', files)
    sents = list(corpus.tagged_sents())

    # train the model
    if opts['-n'] is not None:
        n = int(opts['-n'])
    m = opts['-m']
    c = opts['-c']
    wv_file = opts['-i']
    b = opts['-b'] == 'y'
    if m == 'ct':
        print("Model", m, "Training")
        model = models[m](wv_file=wv_file, is_bin=b)
        model.fit(sents)

    # save it
    root_out_dir = 'Models/'
    if not os.path.isdir(root_out_dir):
        os.mkdir(root_out_dir)

    if b:
        matrix = opts['-M']
        evaluate(model, matrix)
    else:
        filename = opts['-o']
        filename = root_out_dir + filename
        f = open(filename, 'wb')
        pickle.dump(model, f)
        f.close()
