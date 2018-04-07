"""Create word embeddings using Fasttext model

Usage:
  create_vectors.py [-d <dim>] [-w <wngram>]
  create_vectors.py -h | --help

Options:
  -d <dim>      Dimension of word embeddings [default: 100]
  -w <wngram>   Word ngram Length [default: 1]
  -h --help     Show this screen.
"""
import fasttext
import os
from docopt import docopt


def create_word_vectors(input_file, output_dir, dim, word_ngram):

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    filename = output_dir.split('/')[-2]
    output_file = os.path.join(output_dir, filename)

    fasttext.skipgram(input_file, output_file,
                      dim=dim, word_ngrams=word_ngram)


if __name__ == '__main__':
    opts = docopt(__doc__)

    dim = int(opts['-d'])
    wngram = int(opts['-w'])
    case = {
        'output_dir': 'vectors/{}_{}/'.format(str(dim), str(wngram)),
        'dim': dim,
        'word_ngram': wngram,
    }

    input_filename = 'input/input_vect_file.txt'
    root_out_dir = 'vectors/'

    assert os.path.isfile(input_filename)

    if not os.path.isdir(root_out_dir):
        os.mkdir(root_out_dir)

    print("""Fasttext Word embeddings are trainning:
             Dimension: {}
             Word ngrams length: {}
             Input filename: {}
             Output path: {}""".format(dim,
                                       wngram,
                                       input_filename,
                                       case['output_dir']))

    create_word_vectors(input_filename, **case)
