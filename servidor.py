import socket

PORTA = 14600

servidor = socket.socket()
servidor.bind(("localhost", PORTA))
servidor.listen(5)
print("Servidor escutando na porta: ", PORTA)
cliente, endereco = servidor.accept()
print("Conexao aceita de: ", endereco)

while True:		
	mensagem = cliente.recv(1024)
	print("Mensagem recebida: ", mensagem.decode())

	mensagem = input("Digite uma mensagem: ")
	cliente.send(mensagem.encode())	
	#cliente.close()
