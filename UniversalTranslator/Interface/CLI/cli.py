import os
import argparse
from nxo_omega_prime import Neurocore, Picrypt, Echoplex, Auroranode, Spectraos, NexarionDB, NexarionAI

def main():
    parser = argparse.ArgumentParser(description='Nexarion Omega Prime CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Translation command
    translate_parser = subparsers.add_parser('translate', help='Translate text from one language to another')
    translate_parser.add_argument('language_from', help='Language to translate from')
    translate_parser.add_argument('language_to', help='Language to translate to')
    translate_parser.add_argument('text', help='Text to translate')

    # Encryption command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt text using Picrypt')
    encrypt_parser.add_argument('text', help='Text to encrypt')

    # Decryption command
    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt text using Picrypt')
    decrypt_parser.add_argument('encrypted_text', help='Encrypted text to decrypt')

    # Message sending command
    send_message_parser = subparsers.add_parser('send_message', help='Send a message using Echoplex')
    send_message_parser.add_argument('message', help='Message to send')
    send_message_parser.add_argument('recipient', help='Recipient of the message')

    # Node management command
    node_management_parser = subparsers.add_parser('node_management', help='Manage nodes using Auroranode')
    node_management_parser.add_argument('action', help='Action to perform on the node (start, stop, restart)')
    node_management_parser.add_argument('node_id', help='ID of the node to manage')

    # OS management command
    os_management_parser = subparsers.add_parser('os_management', help='Manage OS using Spectraos')
    os_management_parser.add_argument('action', help='Action to perform on the OS (start, stop, restart)')
    os_management_parser.add_argument('os_id', help='ID of the OS to manage')

    # AI assistant command
    ai_assistant_parser = subparsers.add_parser('ai_assistant', help='Get assistance from NexarionAI')
    ai_assistant_parser.add_argument('query', help='Query to ask the AI assistant')

    # Database query command
    db_query_parser = subparsers.add_parser('db_query', help='Execute a query on the database using NexarionDB')
    db_query_parser.add_argument('query', help='Query to execute')

    # File upload command
    file_upload_parser = subparsers.add_parser('file_upload', help='Upload a file to the server')
    file_upload_parser.add_argument('file', help='File to upload')

    # File download command
    file_download_parser = subparsers.add_parser('file_download', help='Download a file from the server')
    file_download_parser.add_argument('file_name', help='Name of the file to download')

    args = parser.parse_args()

    if args.command == 'translate':
        neurocore = Neurocore()
        translated_text = neurocore.translate(args.text, args.language_from, args.language_to)
        print(translated_text)

    elif args.command == 'encrypt':
        picrypt = Picrypt()
        encrypted_text = picrypt.encrypt(args.text)
        print(encrypted_text)

    elif args.command == 'decrypt':
        picrypt = Picrypt()
        decrypted_text = picrypt.decrypt(args.encrypted_text)
        print(decrypted_text)

    elif args.command == 'send_message':
        echoplex = Echoplex()
        echoplex.send_message(args.message, args.recipient)
        print('Message sent successfully')

    elif args.command == 'node_management':
        auroranode = Auroranode()
        auroranode.manage_node(args.action, args.node_id)
        print('Node management successful')

    elif args.command == 'os_management':
        spectraos = Spectraos()
        spectraos.manage_os(args.action, args.os_id)
        print('OS management successful')

    elif args.command == 'ai_assistant':
        nexarion_ai = NexarionAI()
        response = nexarion_ai.process_query(args.query)
        print(response)

    elif args.command == 'db_query':
        nexarion_db = NexarionDB()
        results = nexarion_db.execute_query(args.query)
        print(results)

    elif args.command == 'file_upload':
        file = args.file
        file_path = os.path.join(os.getcwd(), file.name)
        file.save(file_path)
        print('File uploaded successfully')

    elif args.command == 'file_download':
        file_name = args.file_name
        file_path = os.path.join(os.getcwd(), file_name)
        if os.path.exists(file_path):
            print('File downloaded successfully')
        else:
            print ('File not found')

if __name__ == '__main__':
    main()
