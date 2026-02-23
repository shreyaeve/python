import socket
import sys
import time
import random
SERVER_IP="localhost"
SERVER_PORT=54321
BUFFER= 1024
FORMAT ="utf-8"

try:
    #create a socket
    client_sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_sock.connect((SERVER_IP,SERVER_PORT))
    
    print("Client is connected with the server ")
except Exception as e:
    print(f"Error 1:{e}")
    sys.exit()  
try:
    while True:
        temp= round(random.uniform(20,40))
        client_sock.send(str(temp).encode(FORMAT))
        ack_msg=client_sock.recv(BUFFER).decode(FORMAT)
        if not ack_msg:
            print("server maybe down")
            break
        print("server response ", ack_msg)    
        time.sleep(2)

except Exception as e:
    print(f"Error 2:{e}")

    #thonny will use KyboardInterrupt to stop the server
except KeyboardInterrupt:
    print("server is closed")
    client_sock.close()
    sys.exit()