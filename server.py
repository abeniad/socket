import socket
import random
server_number = random.randint(1,100)
server_name = 'desalegn'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('waiting for client...........')
host = socket.gethostname()
port = 5050
s.bind((host,port))
s.listen(3)
while True:

    c, addr = s.accept()
    print(f'connection created from {addr} address\nwaiting for message to be send.......')
    message = c.recv(1024).decode()
    client_name,client_number = message.split('$')
    client_number = int(client_number)
    if 1 > client_number or client_number > 100:
        print(f'the number from the client [{client_number}]is out of range')
        c.close()
        break
    message = []
    print(f'[SERVER NAME]: {server_name}')
    print(f'[CLIENT NAME]: {client_name}')
    
    print(f'[CLIENT CHOSEN NUMBER] {client_number}')
    print(f'[SERVER RANDOMLY CHOSE] {server_number}')
    sum = client_number + server_number
    print(f'[SUM OF CLIENT AND SERVER NUMBER] {sum}')
    message.append(server_name)
    message.append(str(server_number))
    message.append(str(sum))
    data = '#'.join(message)
    c.send(data.encode())
    c.close()
    break
