from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def split_blocks(data, block_size=16):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

def encrypt(data, key):
    padded_key = pad(key, AES.block_size)
    print('\n[🔐] padded_key         :', padded_key.hex())

    cipher = AES.new(padded_key, AES.MODE_ECB)

    padded_data = pad(data, AES.block_size)
    print('[📦] padded_data        :', padded_data.hex())
    print('[📦] padded_data (text) :', padded_data.decode(errors='ignore'))

    encrypted_data = cipher.encrypt(padded_data)
    print('[🔒] encrypted_data     :', encrypted_data.hex())

    return encrypted_data, padded_key, padded_data

def decrypt(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    print('[🔓] decrypted (raw)    :', decrypted_data.hex())
    unpadded_data = unpad(decrypted_data, AES.block_size)
    print('[✅] unpadded_data      :', unpadded_data.decode())
    return unpadded_data

def main():
    data = b"Mister Alexander owes 10000E to Mister Christian"
    key = b"1234567890"

    # 🔐 Encryption and display
    encrypted_data, padded_key, padded_data = encrypt(data, key)

    # Decryption of original message
    print("\n[ℹ️] Decryption of original message:")
    decrypt(encrypted_data, padded_key)

    # ✂️ Block splitting
    plain_blocks = split_blocks(padded_data)
    cipher_blocks = split_blocks(encrypted_data)

    print('\n[🔍] Encrypted blocks:')
    for i, (plain, cipher) in enumerate(zip(plain_blocks, cipher_blocks), 1):
        print(f'  Block {i}: {cipher.hex()}  <-- "{plain.decode(errors="ignore")}"')

    # 🔁 Modifying block order: [3,2,1]
    modified_blocks = [cipher_blocks[2], cipher_blocks[1], cipher_blocks[0]]
    modified_encrypted_data = b''.join(modified_blocks)

    print('\n[🚨] Modified block order:')
    print(f'  Block 1: {cipher_blocks[2].hex()}  <-- "{plain_blocks[2].decode(errors="ignore")}"')
    print(f'  Block 2: {cipher_blocks[1].hex()}  <-- "{plain_blocks[1].decode(errors="ignore")}"')
    print(f'  Block 3: {cipher_blocks[0].hex()}  <-- "{plain_blocks[0].decode(errors="ignore")}"')
    print('[🚨] Modified encrypted_data (hex):', modified_encrypted_data.hex())

    # Attempt to decrypt modified message (usually causes padding error)
    print("\n[ℹ️] Attempting to decrypt message with modified blocks:")
    try:
        decrypt(modified_encrypted_data, padded_key)
    except Exception as e:
        print("Decryption error on modified message:", str(e))

if __name__ == "__main__":
    main()