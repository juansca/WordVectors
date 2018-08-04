import os
import re
import sys


def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


def format_sentence(sent, abr_reg):
    def to_format(line):
        return not line.isspace()

    sent = re.sub(abr_reg, " ABREVIATION ", sent.replace("...", ""))
    sentenceSplit = filter(to_format, sent.split("."))
    return sentenceSplit


def clean_raw_sent(sent, years_pattern, days_pattern, date_pattern,
                   float_pattern, number_pattern, na_ws_wn_pattern):
    """Clean the raw sentence
    - NUMBER (1, 2, 3, 49045)
    - NFLOAT (1.2, 5.222)
    - NDATE (fechas y años)
    delete non-alphanumeric symbols and replace all the multiple
    whitespaces with only one whitespace.
    """


    # Replace numbers with the corresponding token

    # numbers after 'en', 'entre', 'y', 'año', 'años', 'el' words and the same
    # numbers closed by parenthesis, that are between 1000 and 2999 will be
    # considerated years tokens (NDATE)
    # Number corresponding to days will be considerated days tokens (NDATE)
    clean_sent = re.sub(date_pattern, ' NDATE ', sent)
    # years_pattern = r'''(?<=n|y|e|o|s|l|a) ((?:1[0-9]|2[0-9])\d\d)|(?<=[(])((?:1[0-9]|2[0-9])\d\d)'''
    clean_sent = re.sub(years_pattern, ' NDATE ', clean_sent)

    # days_pattern = r'''(?<=l|a|s) ((?:[1-2][0-9]|3[0-1]|[0-9]))'''
    clean_sent = re.sub(days_pattern, ' NDATE ', clean_sent)

    # All the floats number will be replaced with NFLOAT token
    # float_pattern = r'\d+\.\d+|\d+\,\d+'
    clean_sent = re.sub(float_pattern, ' NFLOAT ', clean_sent)

    # All the integer numbers (except years and dates) will be replaced with
    # NUMBER token
    # number_pattern = r'\d+'
    clean_sent = re.sub(number_pattern, ' NUMBER ', clean_sent)

    # Remove non-alphanumeric symbols
    # Remove multiple whitespaces and replace with single whitespace
    # na_ws_wn_pattern = r'[^0-9a-zA-Záéíóú]+|\s+|\n+'
    clean_sent = re.sub(na_ws_wn_pattern, ' ', clean_sent)

    return clean_sent


if __name__ == '__main__':


    ## Preparing regex

    # YEARS
    years_pattern = r'''(?<=n|y|e|o|s|l|a) ((?:1[0-9]|2[0-9])\d\d)|(?<=[(])((?:1[0-9]|2[0-9])\d\d)'''
    years_pattern = re.compile(years_pattern)

    # DAYS
    days_pattern = r'''(?<=l|a|s) ((?:[1-2][0-9]|3[0-1]|[0-9]))'''
    days_pattern = re.compile(days_pattern)

    # DATES
    date_pattern = r'''((?:[1-2][0-9]|3[0-1]|[0-9]))\/(?:1*[0-2]|[1-9])\/((?:[1-2][0-9])\d\d)'''
    date_pattern = re.compile(date_pattern)

    # FLOATS
    float_pattern = r'\d+\.\d+|\d+\,\d+'
    float_pattern = re.compile(float_pattern)

    # NUMBERS
    number_pattern = r'\d+'
    number_pattern = re.compile(number_pattern)

    # non-alphanumeric symbols, multiple whitespaces and multiple newlines
    na_ws_wn_pattern = r'[^0-9a-zA-ZáéíóúÁËÍÓÚñ]+|\s+|\n+'
    na_ws_wn_pattern = re.compile(na_ws_wn_pattern)

    # Abreviations
    abr_pattern = r'([A-Z]{1,2}\.)+|[A-Z]+[a-z]{1,2}\.'
    abr_pattern = re.compile(abr_pattern)


    root_cleaned_filename = 'cleaned_text/cleaned_text_'
    nfiles_processed = 0
    cleaned_filename = root_cleaned_filename + str(nfiles_processed)
    clean_sentences = list()
    if not os.path.isdir('cleaned_text'):
        os.mkdir('cleaned_text')

    root_raw_dir = 'raw_data/sbwce/'

    assert os.path.isdir(root_raw_dir)

    nfiles_cleaned = 0
    nfiles = 0

    for subdir, dirs, files in os.walk(root_raw_dir):
        for file in files:
            nfiles += 1

    for subdir, dirs, files in os.walk(root_raw_dir):
        for file in files:
            raw_file = os.path.join(subdir, file)

            with open(raw_file, 'r') as rfile:

                with open(cleaned_filename, 'w') as cleaned_file:
                    for line in rfile.readlines():
                        sentences = format_sentence(line, abr_pattern)
                        clean_sents = [clean_raw_sent(sentence, years_pattern, days_pattern, date_pattern,
                                       float_pattern, number_pattern, na_ws_wn_pattern).rstrip() + '\n'
                                       for sentence in sentences]
                        cleaned_file.write(' '.join(clean_sents))
                        del(sentences)
                        del(clean_sents)

                nfiles_processed += 1
                cleaned_filename = root_cleaned_filename + str(nfiles_processed)
            nfiles_cleaned += 1
            progress("""{} is cleaning.
                     {} from {} files cleaned""".format(raw_file,
                                                        nfiles_cleaned,
                                                        nfiles))
