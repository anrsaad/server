import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = socket.gethostname()
port = 12345

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)

while True:
    # Receive a message from the client
    message = client_socket.recv(1024).decode("utf-8")
    print("Client:", message)

    # Send a response to the client
    response = input("Server: ")
    client_socket.send(response.encode("utf-8"))

    # Check if the conversation is over
    if response.lower() == "bye":
        break

# Close the connection
client_socket.close()
server_socket.close()
