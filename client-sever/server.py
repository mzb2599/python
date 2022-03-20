import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8080))
serv.listen(5)
while True:
    print("Server started")
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        data=data.decode()
        if(data!="exit"):
            print(data)
        else:
            conn.close()
            print("client disconnected")
            exit()