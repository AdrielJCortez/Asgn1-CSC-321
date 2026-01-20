# install install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def generate_IV():
    return None

def main():
    try:
        file = open("cp-logo.bmp", "rb") # gives us raw bytes for encryption
    except FileNotFoundError:
        print("Error: File not found!!!")
        return

    header = file.read(54)
    body = file.read()
    file.close()

    # check the len of the body

    body_len = len(body) 
    print(body_len)

    # 1) apply PKCS#7 (ensures that the body is in correct size)
    N = 16 - (body_len % 16)

    if (N) != 16:
        padding_bytes = bytes([N]) * N
    else:
        padding_bytes = bytes([16]) * 16

    padded_body = body + padding_bytes

    # 2) key generation + cipher
    key = get_random_bytes(16) 

    # each block of text in ECB will use the same cipher
    cipher = AES.new(key, AES.MODE_ECB) 

    # 3) encrypt blocks using ECB or CBC
    encrypted_body = b""

    # encrypt using ECB using the same cipher as stated before
    for i in range(0, len(padded_body), 16):
        block = padded_body[i:i+16]
        ciphertext_block = cipher.encrypt(block)
        encrypted_body += ciphertext_block 


    # 4) write original header and encrypted body
    with open("encrypted.bmp", "wb") as out_file:
        out_file.write(header)
        out_file.write(encrypted_body)

if __name__ == "__main__":
    main()
