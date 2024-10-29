import threading
import socket

SERVER_NAME = ""
SERVER_PORT = 8800


def start_client():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    username = input("Enter your username: ").strip().lower()

    clientSocket.sendto(f"{username} connected.".encode(), (SERVER_NAME, SERVER_PORT))

    def receive():
        while True:
            message, serverAddress = clientSocket.recvfrom(1024)
            print(message.decode())

    def send():
        while True:
            message = input()
            clientSocket.sendto(
                f"{username}: {message}".encode(), (SERVER_NAME, SERVER_PORT)
            )

    st = threading.Thread(target=receive)
    rt = threading.Thread(target=send)

    st.start()
    rt.start()


start_client()
