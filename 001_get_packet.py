'''
if it needs permission, run vscode as administrator.
'''


import socket
import os


def parsing(host):
    if os.name == 'nt':
        sock_protocol = socket.IPPROTO_IP
    else:
        sock_protocol = socket.IPPROTO_ICMP
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_RAW,
                         sock_protocol)
    sock.bind((host, 0))
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_HDRINCL,
                    1)

    if os.name == 'nt':
        sock.ioctl(socket.SIO_RCVALL,
                   socket.RCVALL_ON)

    data = sock.recvfrom(65535)
    print(data[0])

    if os.name == 'nt':
        sock.ioctl(socket.SIO_RCVALL,
                   socket.RCVALL_OFF)

    sock.close()


if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())
    print(f'listening at [{host}]')
    parsing(host)
