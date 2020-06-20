12.3 Unicode
ASCII - American Standard code for information interchange 128
Representing simple strings
print(ord('H'))
72
print(ord('e'))
101
print(ord('\n'))
10

Unicode - universal code all characters
multi-byte characters
UTF-16 2bytes per character
UTF-32 4bytes per character
UTF-8 1,2,3 or 4 characters overlaps with ASCII - best practice when using file
    or network data between two systems.
Python Strings to 2bytes
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    mystring = data.decode
    print(mystring)

    An http request in python
    import sockets

    mysock = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())
    mysock.close()
