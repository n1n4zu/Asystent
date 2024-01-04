import socket


def ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return f'''Hostname: {hostname}
Adres IP: {IPAddr}'''
