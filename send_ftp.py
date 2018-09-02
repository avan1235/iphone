import ftplib


def send_file(name_file):
    print("Sending...")
    session = ftplib.FTP('files.000webhost.com', 'username', 'password')
    file = open("server/"+name_file, 'rb')
    session.storbinary('STOR ' + "public_html/" + name_file, file)  # send the file
    file.close()
    session.quit()
    print("Sent")