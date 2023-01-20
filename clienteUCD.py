import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket Criado com Sucesso!!!")

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor firmeza'

try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(),  (host, 5432))
    
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente:  {dados}")  
finally:
    print(f'Cliente: Fechando a Conexão')
    s.close()
