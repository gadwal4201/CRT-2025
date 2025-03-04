import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add = "127.0.0.1"    # ipconfig     -->in cmd
port = 1234
complete = (ip_add,port)
s.bind(complete)
while(True):
    msg = s.recvfrom(1024)
    print(msg[0].decode("ascii"))