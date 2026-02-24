#tcp client
import socket
import time
import json
import sys
import random

#server credentials
SERVER_IP="localhost"
SERVER_PORT=54321

#variables
BUFFER= 1024
FORMAT ="utf-8"

#client id
CLIENT_ID="Shreya"

READ_INTERVAL=1 #seconds
BATCH_DURATION=10 #seconds



#creating a client socket
def send_to_server(avg_value):
    try:
        client_sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_sock.settimeout(5)  # Set a timeout for the connection
        client_sock.connect((SERVER_IP,SERVER_PORT))
        payload = {
            "client_id": CLIENT_ID,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "avg_temp": round(avg_value, 2),
             # Send the latest temperature reading
        }
        client_sock.send(json.dumps(payload).encode(FORMAT))
        response = client_sock.recv(BUFFER).decode(FORMAT)
        if response=="ok":
            print("data sent to server")
        client_sock.close()
        
    except Exception as e:
        print(f"Error sending data to server: {e}")
    finally:
        client_sock.close()

#main loop

while True:
    readings = []
    start_time = time.time()
    print("Collecting 10sec sampling... ")
    while time.time() - start_time < BATCH_DURATION:
        temp = round(random.uniform(20, 40), 2)
        readings.append(temp)
        print(f"Collected temperature: {temp}°C")
        time.sleep(READ_INTERVAL)
    #calculate average and send to server
    avg_temp = round(sum(readings) / len(readings), 2)
    print(f"Average temperature: {avg_temp}°C")

    send_to_server(avg_temp)
    print(f"disconnecting from server, next batch in 10 seconds...\n")
    
    
# # TCP Client

# import socket
# import json
# import time
# import random
# import sys

# # server credentials 
# SERVER_IP = "localhost"   # Raspberry Pi IP
# SERVER_PORT = 54321

# # variables 
# FORMAT = "utf-8"
# BUFFER = 1024

# # client ID
# CLIENT_ID = "ESP32_01"

# READ_INTERVAL = 1      # seconds
# BATCH_DURATION = 10    # seconds


# def send_to_server(avg_value):
#     try:
#         client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_sock.settimeout(5)
#         client_sock.connect((SERVER_IP, SERVER_PORT))
#         payload = {
#             "client_id": CLIENT_ID,
#             "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
#             "average_value": round(avg_value, 2)
#         }
#         message = json.dumps(payload).encode(FORMAT)
#         client_sock.send(message)
#         ack = client_sock.recv(BUFFER).decode(FORMAT)
#         if ack == "OK":
#             print("Data sent successfully:", payload)
#         client_sock.close()
#     except Exception as e:
#         print("Transmission error:", e)


# while True:
#     readings = []
#     start_time = time.time()
#     print("Starting 10-second sampling...")
#     # Collect data for 10 seconds
#     while time.time() - start_time < BATCH_DURATION:
#         sensor_value = round(random.uniform(20.0, 40.0), 2)
#         readings.append(sensor_value)
#         print("Reading:", sensor_value)
#         time.sleep(READ_INTERVAL)
#     # Calculate average
#     avg_value = sum(readings) / len(readings)
#     print("Average of last 10 seconds:", round(avg_value, 2))
#     # Send to server
#     send_to_server(avg_value)
#     print("Disconnected from server\n")



