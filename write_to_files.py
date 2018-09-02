from read_data import get_price
from act_time import get_string_time


def write_to_files(list_of_files):
    string_time = get_string_time()
    print("Writing to files...")
    for file in list_of_files:
        data = open('data/' + file + '.txt', 'a+')
        new_line = string_time + ", " + str(get_price(file)) + "\r\n"
        data.write(new_line)
        data.close()
    print("Writing done")