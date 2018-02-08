import fasttext
import os

case_deafault_1 = {
    'output_file': 'vectors/100_1/out',
    'dim': 100,
    'word_ngram': 1,
}

case2 = {
    'output_file': 'vectors/100_2/out',
    'dim': 100,
    'word_ngram': 2,
}

case3 = {
    'output_file': 'vectors/100_3/out',
    'dim': 100,
    'word_ngram': 3,
}


case4 = {
    'output_file': 'vectors/300_1/out',
    'dim': 300,
    'word_ngram': 1,
}


case5 = {
    'output_file': 'vectors/100_1/out',
    'dim': 300,
    'word_ngram': 2,
}

case6 = {
    'output_file': 'vectors/100_1/out',
    'dim': 300,
    'word_ngram': 3,
}


def create_word_vectors(input_file, output_file, dim, word_ngram):

    model = fasttext.skipgram(input_file, output_file,
                              dim=dim, word_ngram=word_ngram)


if __name__ == '__main__':

    input_filename = 'input/input_vect_file.txt'
    out_dir = 'vectors/'

    assert os.path.isfile(input_filename)

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    create_word_vectors(input_filename, **case1)
