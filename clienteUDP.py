import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, 0) #udp protocolo de datagrama do usuario

print('Cliente Socket Criado com sucesso.')

host = 'localhost'
porta = 5432
mensagem = 'Olá servidor, belê?'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor =  s.recvfrom(4096)
    dados =  dados.decode()
    print("Cliente: " + dados)

finally:
    print('Cliente: Fechando a conexão')
    s.close()
