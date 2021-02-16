import csv

def print_file_content(imported_file):
    with open(imported_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def write_lst_to_file(imported_file, lst):
    with open(imported_file, 'w') as file:
        write = csv.writer(file)
        for element in lst:
            file.write(element + "\n")
            print(element)

def write_strings_to_file(imported_file, *strings):
    with open(imported_file, 'w') as file:
        write = csv.writer(file)
        for string in strings:
            file.write(string + "\n")
            print(string)

def csv_to_list(imported_file, my_list):
    with open(imported_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            my_list.append(row)
