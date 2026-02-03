import socket
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename="honeypot_logs.txt", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def log_attempt(ip, port, data):
    logging.info(f"Connection attempt from IP: {ip}, Port: {port}, Data Received: {data}")

def honeypot_server(host="0.0.0.0", port=8080):
    # Set up a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)  # Listen for incoming connections
        print(f"Honeypot running on {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            ip, client_port = client_address
            print(f"Connection from {ip}:{client_port}")
            
            # Capture any data sent by the client
            try:
                data = client_socket.recv(1024).decode('utf-8').strip()
                log_attempt(ip, client_port, data)
                # Respond to the client (simulating an open service)
                client_socket.sendall(b"Unauthorized access detected.\n")
            except Exception as e:
                logging.error(f"Error handling client {ip}:{client_port} - {str(e)}")
            finally:
                client_socket.close()

if __name__ == "__main__":
    honeypot_server()
