from Crypto.Cipher import XOR
import base64
from django.conf import settings


class SimpleEncryptionDecryption(object):
    key = settings.CLIENT_SECRET_DECRYPTION_KEY

    @classmethod
    def encrypt(cls, plain_text):
        cipher = XOR.new(cls.key)
        return base64.b64encode(cipher.encrypt(plain_text)).decode()

    @classmethod
    def decrypt(cls, cipher_text):
        cipher = XOR.new(cls.key)
        return cipher.decrypt(base64.b64decode(cipher_text)).decode()