import socket

SERVER_NAME = ""
SERVER_PORT = 8800


def start_server():
    users = set()

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((SERVER_NAME, SERVER_PORT))
    print("The server is ready")

    while True:
        message, clientAddress = serverSocket.recvfrom(1024)
        print(clientAddress)
        users.add(clientAddress)
        decodedMessage = message.decode()

        print(decodedMessage)

        for user in users:
            if user == clientAddress:
                continue
            try:
                serverSocket.sendto(decodedMessage.encode(), user)
            except Exception as error:
                print(error)
                print(f"Failed to send to {user}")


start_server()
