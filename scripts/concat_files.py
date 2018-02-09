import os


def concat_files():

    root_clean_dir = 'cleaned_text/'
    output_file = 'input/input_vect_file.txt'
    total_size = 0

    if not os.path.isdir('input'):
        os.mkdir('input')

    assert os.path.isdir(root_clean_dir)

    print("All files are being concatenates...")
    with open(output_file, 'w') as outfile:
        for subdir, dirs, files in os.walk(root_clean_dir):
            for file in files:
                my_file = os.path.join(subdir, file)
                total_size += os.stat(my_file).st_size
                with open(my_file, 'r') as infile:
                    for line in infile:
                        outfile.write(line)

    error_msg = '''Something went wrong! The output file has not the correct total size'''
    assert os.stat(output_file).st_size == total_size, error_msg
    print("Contatenation is complete!")

if __name__ == '__main__':
    concat_files()
