#install pycryptodome
from Crypto.Random import get_random_bytes

def generate_IV():
    return None

def main():
    try:
        file = open("cp-logo.bmp", "rb") # gives us raw bytes for encryption
    except FileNotFoundError:
        print("Error: File not found!!!")

    header = file.read(54)

    body = file.read()

    # check the len of the body
    body_len = len(body) 
    print(body_len)

    # apply PKCS#7
    N = 16 - (body_len % 16)

    if (N) != 16:
        padding_bytes = bytes([N]) * N
    else:
        padding_bytes = bytes([16]) * 16

    padded_body = body + padding_bytes

    # print(len(padded_body) % 16)

    # split padded body into 16-byte blocks

    # encrypt blocks using ECB or CBC

    # write original header and encrypted body

    file.close()
    
