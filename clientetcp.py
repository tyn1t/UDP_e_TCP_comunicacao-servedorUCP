import socket
import sys

# para criar um cliente TCP
def main():
       try:
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
       except socket.error as e:
           print("A Conexão falhou")
           print(f"Error: {e}")
           sys.exit()

       print("Socket criado com sucesso")


       HostaAlvo = input("Digite o Host ou Ip a ser conetado: ")
       PortaAlvo = int(input("Digite a porta a ser conectado: "))

       try:
           s.connect((HostaAlvo, PortaAlvo))
           print(f"Cliente TCP conectado com Sucesso no Host: {HostaAlvo} e na porta: {PortaAlvo}")
           s.shutdown(2)
       except socket.error as e:
           print(f"Não foi possivel conectar no Host: {HostaAlvo} - Porta {PortaAlvo}")
           print(f"Erro: {e}")
           sys.exit()

if __name__== "__main__":
    main()

     
          
          
    
