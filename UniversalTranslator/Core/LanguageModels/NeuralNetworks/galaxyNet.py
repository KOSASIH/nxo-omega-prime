import socket
import threading
import json
import time

class GalaxyNet:
    def __init__(self):
        self.host = 'localhost'
        self.port = 12345
        self.server_socket = None
        self.client_sockets = []
        self.lock = threading.Lock()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connected to {address}")
            self.client_sockets.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received data from client: {data.decode()}")
                response = self.process_data(data.decode())
                client_socket.sendall(response.encode())
            except Exception as e:
                print(f"Error handling client: {e}")
                break
        self.client_sockets.remove(client_socket)
        client_socket.close()

    def process_data(self, data):
        try:
            data_dict = json.loads(data)
            if data_dict['type'] == 'translation':
                return self.translate_text(data_dict['text'])
            elif data_dict['type'] == 'grammar':
                return self.apply_grammar(data_dict['text'])
            else:
                return "Invalid request"
        except Exception as e:
            print(f"Error processing data: {e}")
            return "Error processing data"

    def translate_text(self, text):
        # Call the translation API or module
        return "Translated text"

    def apply_grammar(self, text):
        # Call the grammar API or module
        return "Text with applied grammar"

    def send_data(self, data):
        with self.lock:
            for client_socket in self.client_sockets:
                try:
                    client_socket.sendall(data.encode())
                except Exception as e:
                    print(f"Error sending data to client: {e}")

def main():
    galaxy_net = GalaxyNet()
    galaxy_net.start_server()

if __name__ == "__main__":
    main()
