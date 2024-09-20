import unittest
import os
from picrypt import Picrypt
from picrypt import PicryptConfig
from picrypt import RSAEncryptor
from picrypt import RSADecryptor
from picrypt import AESEncryptor
from picrypt import AESDecryptor
from picrypt import Hasher
from picrypt import DigitalSigner
from picrypt import DigitalVerifier

class TestPicrypt(unittest.TestCase):
    def test_init(self):
        config = PicryptConfig(rsa_key_size=2048, aes_key_size=256, hash_algorithm="SHA256", digital_signature_algorithm="SHA256")
        picrypt = Picrypt(config)
        self.assertIsInstance(picrypt, Picrypt)

    def test_encrypt_decrypt(self):
        config = PicryptConfig(rsa_key_size=2048, aes_key_size=256, hash_algorithm="SHA256", digital_signature_algorithm="SHA256")
        picrypt = Picrypt(config)
        message = b"Hello, World!"
        encrypted_message = picrypt.encrypt(message)
        decrypted_message = picrypt.decrypt(encrypted_message)
        self.assertEqual(decrypted_message, message)

    def test_sign_verify(self):
        config = PicryptConfig(rsa_key_size=2048, aes_key_size=256, hash_algorithm="SHA256", digital_signature_algorithm="SHA256")
        picrypt = Picrypt(config)
        message = b"Hello, World!"
        signature = picrypt.sign(message)
        picrypt.verify(message, signature)
        self.assertTrue(True)

    def test_hash(self):
        config = PicryptConfig(rsa_key_size=2048, aes_key_size=256, hash_algorithm="SHA256", digital_signature_algorithm="SHA256")
        picrypt = Picrypt(config)
        message = b"Hello, World!"
        hashed_message = picrypt.hash(message)
        self.assertIsInstance(hashed_message, bytes)

if __name__ == "__main__":
    unittest.main()
