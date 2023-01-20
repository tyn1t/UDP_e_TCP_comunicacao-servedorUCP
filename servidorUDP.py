import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado co sucesso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = '\nServidor: Oláaaaa cliente e ai beleza'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)
