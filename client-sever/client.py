import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
x=input("Enter the data to send or type exit:- ")
while x!="exit":
    client.send(x.encode())
    x=input("Enter the data to send or type exit:- ")
if(x=="exit"):
    client.send(x)
    client.close()
    print("Connection closed")
else:
    print("Unexpected error!!")
#print(from_server)