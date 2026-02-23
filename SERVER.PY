import socket
import sys
SERVER_IP="localhost"
SERVER_PORT=54321
BUFFER= 1024
FORMAT ="utf-8"

try:
    #create a socket
    server_sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_sock.bind((SERVER_IP,SERVER_PORT))
    server_sock.listen(2)
    print("server is running")
except Exception as e:
    print(f"Error 1:{e}")
    sys.exit()  
try:
    while True:
        client_sock, client_addr = server_sock.accept()
        print(f"client connected from {client_addr[0]}:{client_addr[1]}")
        #ye wala loop connected rakhega 
        while True:
            data= client_sock.recv(BUFFER).decode(FORMAT)
            if not data:
                print("client disconnected")
                break
            
            print(f"received data from client: {data}")
            client_sock.send("data received".encode(FORMAT))

except Exception as e:
    print(f"Error 2:{e}")

    #thonny will use KyboardInterrupt to stop the server
except KeyboardInterrupt:
    print("server is closed")
    server_sock.close()
    sys.exit()