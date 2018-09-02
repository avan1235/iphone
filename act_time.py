import time

def get_string_time():
    current_time = time.localtime()
    string_time = time.strftime('%H:%M %d.%m.%y', current_time)
    return string_time
