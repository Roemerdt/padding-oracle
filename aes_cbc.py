import base64
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from typing import List


def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])


class AES_CBC:
    def __init__(self, key: bytes = get_random_bytes(32)):
        self.key = key
        self._cipher = AES.new(key, AES.MODE_ECB)
        
    def _add_padding(self, data: bytes) -> bytes:
        padding = 16 - (len(data) % 16)
        return data + bytes([padding] * padding)
    
    def _check_and_strip_padding(self, data: bytes) -> bytes:
        expected_padding = data[-1]
        if not all(byte == expected_padding for byte in data[-expected_padding:]):
            raise ValueError("incorrect padding")
        return data[:-expected_padding]
        
    def _split_blocks(self, data: bytes) -> List[bytes]:
        return [data[i:i+16] for i in range(0, len(data), 16)]
    
    def encrypt(self, plaintext: str) -> bytes:
        plaintext = self._add_padding(plaintext.encode())
        plaintext_blocks = self._split_blocks(plaintext)
        
        iv = get_random_bytes(16)
        ciphertext_blocks = [iv]
        
        for i, block in enumerate(plaintext_blocks):
            if i == 0:
                ciphertext_blocks.append(self._cipher.encrypt(xor(iv, block)))
            else:
                ciphertext_blocks.append(self._cipher.encrypt(xor(ciphertext_blocks[i], block)))
                
        return base64.b64encode(b''.join(ciphertext_blocks))
    
    def decrypt(self, ciphertext: bytes) -> str:
        ciphertext = base64.b64decode(ciphertext)
        ciphertext_blocks = self._split_blocks(ciphertext)
        
        plaintext_blocks = []
        
        for i, block in enumerate(ciphertext_blocks[1:], 1):
            plaintext_blocks.append(xor(self._cipher.decrypt(block), ciphertext_blocks[i - 1]))
            
        return self._check_and_strip_padding(b''.join(plaintext_blocks)).decode()