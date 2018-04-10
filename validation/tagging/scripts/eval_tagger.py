"""Evaulate a tagger.

Usage:
  eval.py -m <yn> -i <file>
  eval.py -h | --help

Options:
  -m <yn>       If you want to generate the confusion matrix ('y') or not ('n')
  -i <file>     tagg model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import sys
from collections import Counter
import numpy as np
import os
from time import time
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from corpus.ancora import SimpleAncoraCorpusReader

def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


def plot_confusion_matrix(cm, classes, filename="cnf_matrix.png",
                          normalize=False,
                          title='Confusion matrix',
                          ylabel='True label', xlabel='Predicted label'):
    """
    This function plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    np.set_printoptions(precision=2)

    # Plot non-normalized confusion matrix
    plt.figure(figsize=(15, 10), dpi=80)

    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Oranges)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90, fontsize=8)
    plt.yticks(tick_marks, classes, fontsize=8)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.tight_layout()
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    filename = filename.split('/')
    root_out_dir = filename[0] + '/Matrices/'
    if not os.path.isdir(root_out_dir):
        os.mkdir(root_out_dir)

    new_filename = root_out_dir + filename[1]
    plt.savefig(new_filename)


def evaluate(model=None, matrix='n'):
    '''
    model --   The model trained that has been evaluated
    matrix --  If you want to generate the confusion matrix ('y') or not ('n')

    '''
    start = time()
    if model is None:
        opts = docopt(__doc__)
        matrix = opts['-m'] == 'y'

        # load the model
        filename = opts['-i']
        filename = 'Models/' + filename
        f = open(filename, 'rb')
        model = pickle.load(f)
        f.close()

    # load the data
    files = '3LB-CAST/.*\.tbf\.xml'
    actual_dir = os.path.dirname(os.path.abspath(__file__))

    corpus = SimpleAncoraCorpusReader(actual_dir + '/corpus/ancora/', files)
    sents = list(corpus.tagged_sents())
    n = len(sents)

    # tag
    hits, total = 0, 0
    hits_known, hits_unknown = 0, 0
    total_known, total_unknown = 0, 0
    are_known = []

    # confusion matrix
    test = []
    prediction = []

    for i, sent in enumerate(sents):
        word_sent, gold_tag_sent = zip(*sent)
        model_tag_sent = model.tag(word_sent).tolist()
        assert len(model_tag_sent) == len(gold_tag_sent), i
        # For confusion matrix
        test += list(gold_tag_sent)
        prediction += model_tag_sent

        # global score
        hits_sent = [m == g for m, g in zip(model_tag_sent, gold_tag_sent)]
        hits += sum(hits_sent)
        total += len(sent)
        total_acc = float(hits) / total

        # known words score
        for j in range(len(hits_sent)):
            # using the Counter method, descripted later, we have to asign
            # some values if are known or unknown and if are hit or not.
            if not model.unknown(word_sent[j]):
                are_known += [hits_sent[j] + 1]
            else:
                are_known += [hits_sent[j] - 2]

        progress('{:3.1f}% (Total: {:2.2f}%)'.format(float(i) * 100 / n,
                                                     total_acc * 100))

    # For eficiency we will use the Counter object from collections
    # library.
    # We redefine some things to look for them later
    known = 2
    fail_known = 1
    unknown = -1
    fail_unknown = -2

    # Counter creates a dictionary whose keys are known, fail_known, unknown
    # and fail_unknown.
    counter = Counter(are_known)
    # Now get the values that represent how many times does apears each one
    hits_known += counter[known]
    total_known += counter[known] + counter[fail_known]

    hits_unknown += counter[unknown]
    total_unknown += counter[unknown] + counter[fail_unknown]

    # Compute accuracy
    total_acc = float(hits) / total
    known_acc = float(hits_known) / total_known
    unknown_acc = float(hits_unknown) / total_unknown
    finish = time() - start
    print('')
    print('Total accuracy: {:2.2f}%'.format(total_acc * 100))
    print('Known accuracy: {:2.2f}%'.format(known_acc * 100))
    print('Unknown accuracy: {:2.2f}%'.format(unknown_acc * 100))
    print('Time running: {:2.2f}seconds'.format(finish))

    if matrix:
        matrix = confusion_matrix(test, prediction)
        classes = list(set(test) | set(prediction))
        classes.sort()
        plot_confusion_matrix(matrix, classes,
                              filename.split('.')[0]+'.png')


if __name__ == '__main__':
    evaluate()
