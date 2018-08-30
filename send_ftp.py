import ftplib
from act_time import get_minute

def send_file(name_file):
    session = ftplib.FTP('files.000webhost.com', '''username''', '''password''')
    file = open("server/"+name_file, 'rb')
    session.storbinary('STOR ' + "public_html/" + name_file, file)  # send the file
    file.close()
    session.quit()


def send_file_thread(name_file, write_minutes, operation_minutes):
    DONE = False
    CAN_BE_DONE = True

    state = CAN_BE_DONE

    while True:
        if get_minute() == write_minutes and state == CAN_BE_DONE:
            send_file(name_file)
            state = DONE
        elif get_minute() == (write_minutes + operation_minutes) % 60 and state == DONE:
            state = CAN_BE_DONE
        else:
            print("Waiting for send")