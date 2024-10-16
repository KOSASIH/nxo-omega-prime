import socket
import threading
import json
import time
import speciesLexicon

class SpeciesNet:
    def __init__(self):
        self.host = 'localhost'
        self.port = 12345
        self.server_socket = None
        self.client_sockets = []
        self.lock = threading.Lock()
        self.species_lexicon = speciesLexicon.SpeciesLexicon()

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
                return self.translate_text(data_dict['text'], data_dict['species'])
            elif data_dict['type'] == 'grammar':
                return self.apply_grammar(data_dict['text'], data_dict['species'])
            elif data_dict['type'] == 'lexicon':
                return self.get_lexicon(data_dict['species'])
            else:
                return "Invalid request"
        except Exception as e:
            print(f"Error processing data: {e}")
            return "Error processing data"

    def translate_text(self, text, species):
        # Call the translation API or module
        return self.species_lexicon.translate_text(text, species)

    def apply_grammar(self, text, species):
        # Call the grammar API or module
        return self.species_lexicon.apply_grammar(text, species)

    def get_lexicon(self, species):
        # Call the lexicon API or module
        return self.species_lexicon.get_lexicon(species)

    def send_data(self, data):
        with self.lock:
            for client_socket in self.client_sockets:
                try:
                    client_socket.sendall(data.encode())
                except Exception as e:
                    print(f"Error sending data to client: {e}")

def main():
    species_net = SpeciesNet()
    species_net.start_server()

if __name__ == "__main__":
    main()
