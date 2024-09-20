import os
import argparse
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_keypair(key_size=2048):
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    return key

def save_keypair(key, private_key_file, public_key_file):
    private_key_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key_pem = key.public_key().public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
    )
    with open(private_key_file, 'wb') as f:
        f.write(private_key_pem)
    with open(public_key_file, 'wb') as f:
        f.write(public_key_pem)

def main():
    parser = argparse.ArgumentParser(description='Generate keypair')
    parser.add_argument('--key-size', type=int, default=2048, help='Key size')
    parser.add_argument('--private-key-file', required=True, help='Private key file')
    parser.add_argument('--public-key-file', required=True, help='Public key file')
    args = parser.parse_args()
    key = generate_keypair(args.key_size)
    save_keypair(key, args.private_key_file, args.public_key_file)

if __name__ == '__main__':
    main()
