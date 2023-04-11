import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5050
s.connect((host,port))
client_name = 'sihne'
client_number =  input('Enter a number between 1 and 100: ')
data = []
data.append(client_name)
data.append(client_number)
data = '$'.join(data)
s.send(data.encode())
try:
    message = s.recv(1024).decode()
    server_name, server_number, sum = message.split('#')
    print(f'[SERVER NAME]: {server_name}')
    print(f'[CLIENT NAME]: {client_name}')
    print(f'[SERVER NUMBER] {server_number}')
    print(f'[SUM OF CLIENT AND SERVER NUMBER] {sum}')
except:
    print('No response from the server connection lost')
s.close()
