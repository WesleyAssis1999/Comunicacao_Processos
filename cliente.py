import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 15000))

while True:    
    mensagem = input("Digite uma mensagem: ")
    cliente.send(mensagem.encode())

    mensagem = cliente.recv(1024)
    print("Mensagem recebida: ", mensagem.decode())
    #cliente.close()
