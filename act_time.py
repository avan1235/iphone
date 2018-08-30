import time

def get_string_time():
    current_time = time.localtime()
    string_time = time.strftime('%H:%M:%S %d/%m/%Y', current_time)
    return string_time


def get_hour():
     current_time = time.localtime()
     string_time = time.strftime('%H', current_time)
     return int(string_time)


def get_minute():
    current_time = time.localtime()
    string_time = time.strftime('%M', current_time)
    return int(string_time)


def get_second():
    current_time = time.localtime()
    string_time = time.strftime('%S', current_time)
    return int(string_time)

