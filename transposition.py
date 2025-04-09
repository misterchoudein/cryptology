def encrypt_message(message, key):
    #  padding
    padding = (key - (len(message) % key)) % key
    message += '_' * padding
    
    # matrix creation
    chunks = [message[i:i+key] for i in range(0, len(message), key)]
    
    # filling the matrix
    encrypted = ''
    for col in range(key):
        for row in chunks:
            if col < len(row):
                encrypted += row[col]
    
    return encrypted

def decrypt_message(encrypted, key):
    rows = len(encrypted) // key
    
    # matrix creation
    matrix = [['' for _ in range(key)] for _ in range(rows)]
    
    # filling the matrix
    pos = 0
    for col in range(key):
        for row in range(rows):
            matrix[row][col] = encrypted[pos]
            pos += 1
    
    # br
    decrypted = ''
    for row in matrix:
        decrypted += ''.join(row)
    
    return decrypted.rstrip('_')

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Transposition cipher v2')
    parser.add_argument('text', help='Text to encrypt/decrypt')
    parser.add_argument('key', type=int, help='Number of columns')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt mode')
    
    args = parser.parse_args()
    
    if args.decrypt:
        result = decrypt_message(args.text, args.key)
    else:
        result = encrypt_message(args.text, args.key)
    
    print(f"Result: {result}")