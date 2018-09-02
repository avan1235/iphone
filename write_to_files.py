from read_data import get_price
from act_time import get_string_time
from os import path, makedirs

data_dir = 'data'

def write_to_files(list_of_files):
    string_time = get_string_time()
    print("Writing to files...")
    if not path.exists(data_dir):
        makedirs(data_dir)
    for file in list_of_files:
        data = open(data_dir + '/' + file + '.txt', 'a+')
        new_line = string_time + ", " + str(get_price(file)) + "\r\n"
        data.write(new_line)
        data.close()
    print("Writing done")