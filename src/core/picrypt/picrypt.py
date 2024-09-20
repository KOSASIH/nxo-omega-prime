import os
import hashlib
import hmac
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class PicryptConfig:
    def __init__(self, rsa_key_size, aes_key_size, hash_algorithm, digital_signature_algorithm):
        self.rsa_key_size = rsa_key_size
        self.aes_key_size = aes_key_size
        self.hash_algorithm = hash_algorithm
        self.digital_signature_algorithm = digital_signature_algorithm

class PicryptException(Exception):
    pass

class RSAEncryptor:
    def __init__(self, public_key):
        self.public_key = public_key

    def encrypt(self, message):
        encrypted_message = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

class RSADecryptor:
    def __init__(self, private_key):
        self.private_key = private_key

    def decrypt(self, encrypted_message):
        original_message = self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return original_message

class AESEncryptor:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(b'\0' * 16), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_message = padder.update(message) + padder.finalize()
        encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
        return encrypted_message

class AESDecryptor:
    def __init__(self, key):
        self.key = key

    def decrypt(self, encrypted_message):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(b'\0' * 16), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded_message = decryptor.update(encrypted_message) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        message = unpadder.update(decrypted_padded_message) + unpadder.finalize()
        return message

class Hasher:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def hash(self, message):
        if self.algorithm == "SHA256":
            return hashlib.sha256(message).digest()
        elif self.algorithm == "SHA512":
            return hashlib.sha512(message).digest()
        else:
            raise PicryptException(f"Unknown hash algorithm: {self.algorithm}")

class DigitalSigner:
    def __init__(self, private_key, algorithm):
        self.private_key = private_key
        self.algorithm = algorithm

    def sign(self, message):
        if self.algorithm == "SHA256":
            signature = self.private_key.sign(
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return signature
        elif self.algorithm == "SHA512":
            signature = self.private_key.sign(
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA512()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA512()
            )
            return signature
        else:
            raise PicryptException(f"Unknown digital signature algorithm: {self.algorithm}")

class DigitalVerifier:
    def __init__(self, public_key, algorithm):
        self.public_key = public_key
        self.algorithm = algorithm

    def verify(self, message, signature):
        if self.algorithm == "SHA256":
            self.public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        elif self.algorithm == "SHA512":
            self.public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA512()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA512()
            )
        else:
            raise PicryptException(f"Unknown digital signature algorithm: {self.algorithm}")

class Picrypt:
    def __init__(self, config):
        self.config = config
        self.rsa_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=config.rsa_key_size,
            backend=default_backend()
        )
        self.aes_key = os.urandom(config.aes_key_size // 8)
        self.rsa_encryptor = RSAEncryptor(self.rsa_key.public_key())
        self.rsa_decryptor = RSADecryptor(self.rsa_key)
        self.aes_encryptor = AESEncryptor(self.aes_key)
        self.aes_decryptor = AESDecryptor(self.aes_key)
        self.hasher = Hasher(config.hash_algorithm)
        self.digital_signer = DigitalSigner(self.rsa_key, config.digital_signature_algorithm)
        self.digital_verifier = DigitalVerifier(self.rsa_key.public_key(), config.digital_signature_algorithm)

    def encrypt(self, message):
        encrypted_message = self.rsa_encryptor.encrypt(message)
        return encrypted_message

    def decrypt(self, encrypted_message):
        original_message = self.rsa_decryptor.decrypt(encrypted_message)
        return original_message

    def sign(self, message):
        signature = self.digital_signer.sign(message)
        return signature

    def verify(self, message, signature):
        self.digital_verifier.verify(message, signature)

    def hash(self, message):
        hashed_message = self.hasher.hash(message)
        return hashed_message
