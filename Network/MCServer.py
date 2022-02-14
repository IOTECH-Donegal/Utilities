'''
Multicast Server by: JOR
Reads multicast packets from a particular address and port.

Alpha: 13FEB22
'''
import socket
import struct
import settings.mc as settings

# Set multicast information
MCAST_GRP = settings.MCSERVER["MCAST_GROUP"]
SERVER_ADDRESS = ('', settings.MCSERVER["PORT"])
MCAST_IF_IP = settings.MCSERVER["IP_ADDRESS"]

print(f'Make sure this server IP address matches {MCAST_IF_IP} in settings')
print('This script has no error handling, by design')


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(SERVER_ADDRESS)
    group = socket.inet_aton(MCAST_GRP)
    mreq = struct.pack('4s4s', group, socket.inet_aton(MCAST_IF_IP))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        print('Waiting to receive message')
        data, address = s.recvfrom(1024)
        print(f'received {len(data)} bytes from {address}')
        print(data)
