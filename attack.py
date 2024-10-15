from typing import List, Tuple
import base64
from aes_cbc import AES_CBC, xor

global_cipher = AES_CBC()


def split_blocks(data: bytes) -> List[bytes]:
    return [data[i:i+16] for i in range(0, len(data), 16)]


def find_bytes(blocks: Tuple[bytes, bytes]) -> str:
    c_prime = bytearray(blocks[0])
    plaintext_bytes = bytearray(16)
    
    for i in range(16):
        expected_padding = bytes([0] * (16 - i) + [i+1] * i)
        c_prime = bytearray(xor(xor(expected_padding, plaintext_bytes), blocks[0]))
    
        for byte in range(256):
            c_prime[15-i] = byte
            to_test = base64.b64encode(bytes(c_prime) + blocks[1])
            
            try:
                global_cipher.decrypt(to_test)
                plaintext_bytes[15-i] = byte ^ (i+1) ^ blocks[0][15-i]
                break
            except ValueError:
                pass
    
    return ''.join(chr(b) for b in plaintext_bytes if b > 16)


def find_plaintext(ciphertext: bytes) -> None:
    ciphertext = base64.b64decode(ciphertext)
    blocks = split_blocks(ciphertext)
    
    plaintext = ""
    
    for i in range(len(blocks) - 1):
        plaintext += find_bytes((blocks[i], blocks[i+1]))
        
    print(plaintext)


if __name__ == "__main__":
    plaintext = "Dit is dus echt super duper geheim!"
    ciphertext = global_cipher.encrypt(plaintext)
    
    find_plaintext(ciphertext)