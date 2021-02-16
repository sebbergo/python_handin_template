import sys
import csv

def write_lst_to_file(imported_file, *lst):
    with open(imported_file, 'w') as file:
        write = csv.writer(file)
        for element in lst:
            file.write(element + "\n")

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    write_lst_to_file(*sys.argv[1:])