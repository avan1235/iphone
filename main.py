import threading
from write_to_files import write_to_files_thread
from plot import create_plot_thread
from send_ftp import send_file_thread

shops_list = ['MediaExpert', 'MediaMarkt', 'morele', 'RTVEuroAGD', 'Sferis', 'Vobis', 'XKOM']

write_every_minute = 30
write_time_spend = 2

plot_every_minute = 35
plot_time_spend = 1

send_every_minute = 40
send_time_spend = 10


arguments_write = (shops_list, write_every_minute, write_time_spend)
arguments_plot = (shops_list, "plot.png", plot_every_minute, plot_time_spend)
arguments_send = ("plot.png", send_every_minute, send_time_spend)


thread_write_to_file = threading.Thread(target=write_to_files_thread, args=arguments_write)
thread_plot = threading.Thread(target=create_plot_thread, args=arguments_plot)
thread_send = threading.Thread(target=send_file_thread, args=arguments_send)

thread_write_to_file.start()
thread_plot.start()
thread_send.start()