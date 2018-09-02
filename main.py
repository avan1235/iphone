from write_to_files import write_to_files
from plot import create_plot
from send_ftp import send_file

shops_list = ['MediaExpert', 'MediaMarkt', 'morele', 'RTVEuroAGD', 'Sferis', 'Vobis', 'XKOM']
image_name = "plot.png"

write_to_files(shops_list)
create_plot(shops_list, image_name)
send_file(image_name)
