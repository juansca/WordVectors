import os
from gensim.models import KeyedVectors
import sys

word_vector_files = ['vectors/100_1/out.vec', 'vectors/100_2/out.vec',
                     'vectors/100_3/out.vec', 'vectors/300_1/out.vec']
#                     'vectors/300_2/out.vec', 'vectors/300_3/out.vec']

#word_vector_files = ['vectors/100_1/out.vec', 'vectors/100_2/out.vec']



def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


if __name__ == '__main__':

    print("""Starting to calculate models accuracies.
          {} models on the evaluation pool""".format(len(word_vector_files)))

    accuracy_dir = 'validation/accuracies/'

    if not os.path.isdir(accuracy_dir):
        os.mkdir(accuracy_dir)

    n_files_evaluated = 0
    for wv_filename in word_vector_files:
        remain = len(word_vector_files) - n_files_evaluated
        print("{} is going on! {} remaining".format(wv_filename, remain))

        to_save = dict()
        wv = KeyedVectors.load_word2vec_format(wv_filename, binary=False)
        accuracy = wv.accuracy('validation/questions-words_sp.txt')
        acc_filename = os.path.join(accuracy_dir, wv_filename.split('/')[1])
        for my_acc in accuracy:
            section = my_acc['section']
            n_correct = len(my_acc['correct'])
            n_total = n_correct + len(my_acc['incorrect'])
            acc = n_correct / n_total
            to_save[section] = acc
        with open(acc_filename, 'w') as af:
            af.write(str(to_save))
        del(wv)
        n_files_evaluated += 1

    print("Evaluation models completed!")
