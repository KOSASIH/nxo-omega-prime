import os
import argparse
from fabric import Connection

def deploy_node(node_name, node_ip, username, private_key_file):
    conn = Connection(node_name, node_ip, user=username, connect_kwargs={'key_filename': private_key_file})
    conn.run('sudo apt update')
    conn.run('sudo apt install -y docker')
    conn.run('sudo docker run -d --name auroranode auroranode:latest')
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Deploy network')
    parser.add_argument('--node-name', required=True, help='Node name')
    parser.add_argument('--node-ip', required=True, help='Node IP')
    parser.add_argument('--username', required=True, help='Username')
    parser.add_argument('--private-key-file', required=True, help='Private key file')
    args = parser.parse_args()
    deploy_node(args.node_name, args.node_ip, args.username, args.private_key_file)

if __name__ == '__main__':
    main()
