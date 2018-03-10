import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")


socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:1234")

# Run a simple "Echo" server
while True:
    message = sock.recv()
    message = message.decode()
    sock.send_string(message)
    socket.send_string(message)
    if(message!=""):
        print("[Server] Echo: "+message)
