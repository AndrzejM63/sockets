# Socket client example in python
import argparse
import os
import socket   # for sockets
import sys  # for exit

import psutil as psutil
import time

from datetime import datetime


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ho", "--host",
                        action="store", dest="host",
                        help="host name")
    parser.add_argument("-p", "--port",
                        action="store", dest="port",
                        help="port number")
    options = parser.parse_args()
    return options


def solution(options):
    # create an INET, STREAMing socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()

    print 'Socket Created'

    host = options.host  # 'www.google.com'
    try:
        port = int(options.port)  # 80

    except ValueError:
        print 'port must be integer value, not: ' + options.port + ' Exiting'
        sys.exit()

    try:
        remote_ip = socket.gethostbyname(host)

    except socket.gaierror:
        # could not resolve
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    # Connect to remote server
    try:
        s.connect((remote_ip, port))

    except socket.error:
        print 'Connection refused. Try on another port. Exiting'
        sys.exit()

    reply = s.recv(4096)  # recieveing welcome string
    print 'Socket Connected to ' + host + ' on ip ' + remote_ip
    print reply

    # Send some data to remote server
    message = str(socket.gethostbyname(socket.gethostname()))  # get local IP: TBD client or server has to resolve it
    p = psutil.Process(os.getpid())
    message += '|' + str(p.cpu_percent())
    message += '|' + str(p.memory_info()[0]/1024) # get memory usage in KB
    message += '|' + str(datetime.now())

    try:
        # Set the whole string
        s.sendall(message)
    except socket.error:
        # Send failed
        print 'Send failed'
        sys.exit()

    print 'Message send successfully'

    # Now receive data
    reply = s.recv(4096)

    print reply

    s.close()


if __name__ == "__main__":
    options = set_options()
    print(options)
    solution(options)
