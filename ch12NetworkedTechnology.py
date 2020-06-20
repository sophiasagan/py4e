Ch12 Networked Technology

TCP Connections/Sockets
in computer networking, an internet socket or network socket is an endpoint of
of a bidirectional interprocess communication flow across an internet
protocol-based computeer network, such as the internet.

Port 80 - webserver http
port 443 - webserver https

#Sockets in Python
import Sockets
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) #(host,port)

#Hypertext Transfer Protocol (http)
URL - uniform resource locator
#telnet
#nmap

#An http request in Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()#\n-enter in telnet
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

#encode converts utf-8 code
#decode converts internal code
