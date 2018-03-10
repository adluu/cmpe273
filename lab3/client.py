import zmq
import sys
import time

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"

sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:1234")
socket.setsockopt_string(zmq.SUBSCRIBE, "")


# Send a "message" using the socket
name = " ".join(sys.argv[1:])
print("User[" + name + "] Connected to the chat server. Tap Enter to refresh chat")

while True:
    msg = input("[{}] > ".format(name))
    if msg != "quit" and msg!="": 
        sm = "[{}] : ".format(name)+msg
        sock.send_string(sm)
        stri = sock.recv()
    if msg=="":
        sm=""
        sock.send_string(sm)
        stri=sock.recv()    
    reply = socket.recv()
    reply = reply.decode()
    if reply!=sm and reply!="":
        print(reply)
