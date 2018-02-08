import os


def concat_files():

    root_clean_dir = 'cleaned_text/'
    output_file = 'input/input_vect_file.txt'

    if not os.path.isdir('input'):
        os.mkdir('input')

    assert os.path.isdir(root_clean_dir)

    with open(output_file, 'w') as outfile:
        for subdir, dirs, files in os.walk(root_clean_dir):
            for file in files:
                with open(file) as infile:
                    for line in infile:
                        outfile.write(line)
