import socket
from TicTacToe import Board, GUI

mi_socket = socket.socket()
mi_socket.bind(('192.168.0.13', 8000))
mi_socket.listen(5)

while True:
	conexion, addr = mi_socket.accept()
	print("Nueva conexión establecida!")
	print(addr)

	peticion = conexion.recv(1024)
	print(addr)

	prueba = GUI()
	MESSAGE = prueba.app.mainloop()
	conexion.send(MESSAGE)
	conexion.close()