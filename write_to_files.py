from read_data import get_price
from act_time import get_string_time, get_minute,get_second


def write_to_files_thread(list_of_files, write_minutes, operation_minutes):
    DONE = False
    CAN_BE_DONE = True

    state = CAN_BE_DONE

    while True:
        if get_minute() == write_minutes and state == CAN_BE_DONE:
            string_time = get_string_time()
            for file in list_of_files:
                data = open('data/' + file + '.txt', 'a+')
                new_line = string_time + ", " + str(get_price(file)) + "\r\n"
                data.write(new_line)
                data.close()
            state = DONE
        elif get_minute() == (write_minutes+operation_minutes)%60 and state == DONE:
            state = CAN_BE_DONE
        else:
            print("Waiting for data")