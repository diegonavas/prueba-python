import socket

mi_socket = socket.socket()
mi_socket.connect(('192.168.0.13', 8000))

MESSAGE = "Hola desde el cliente!"
mi_socket.send(MESSAGE.encode('utf-8'))
respuesta = mi_socket.recv(1024)

print(respuesta)
mi_socket.close()