import fasttext
import os

case_default_1 = {
    'output_dir': 'vectors/100_1/',
    'dim': 100,
    'word_ngram': 1,
}

case2 = {
    'output_dir': 'vectors/100_2/',
    'dim': 100,
    'word_ngram': 2,
}

case3 = {
    'output_dir': 'vectors/100_3/',
    'dim': 100,
    'word_ngram': 3,
}


case4 = {
    'output_dir': 'vectors/300_1/',
    'dim': 300,
    'word_ngram': 1,
}


case5 = {
    'output_dir': 'vectors/300_2/',
    'dim': 300,
    'word_ngram': 2,
}

case6 = {
    'output_dir': 'vectors/300_3/',
    'dim': 300,
    'word_ngram': 3,
}


def create_word_vectors(input_file, output_dir, dim, word_ngram):

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    output_file = os.path.join(output_dir, 'out')

    model = fasttext.skipgram(input_file, output_file,
                              dim=dim, word_ngrams=word_ngram)


if __name__ == '__main__':

    input_filename = 'input/input_vect_file.txt'
    root_out_dir = 'vectors/'

    assert os.path.isfile(input_filename)

    if not os.path.isdir(root_out_dir):
        os.mkdir(root_out_dir)

    create_word_vectors(input_filename, **case5)
