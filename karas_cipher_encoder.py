def karas_cipher_encrypt(text):
    file_bytes = bytes.fromhex("025F8D1C4EA239BB741A5C990D2F41")
    hash_val = bytes.fromhex("9A6EC012E1A7DA9DBE34194d478AD7C0DB1822FB071DF12981496ED104384113")
    h_int = int.from_bytes(hash_val, 'big')
    f_int = int.from_bytes(file_bytes, 'big')
    combined_constants = sorted([h_int, f_int], reverse=True)
    encrypted_text = ""
    for char in text:
        val = ord(char)
        for const in combined_constants:
            shift = (const % 7) + 1
            val = ((val << shift) | (val >> (8 - shift))) & 0xFF
        encrypted_text += chr(val)
    return encrypted_text

def karas_cipher_decrypt(text):
    file_bytes = bytes.fromhex("025F8D1C4EA239BB741A5C990D2F41")
    hash_val = bytes.fromhex("9A6EC012E1A7DA9DBE34194d478AD7C0DB1822FB071DF12981496ED104384113")
    h_int = int.from_bytes(hash_val, 'big')
    f_int = int.from_bytes(file_bytes, 'big')
    combined_constants = sorted([h_int, f_int], reverse=True)
    decrypted_text = ""
    for char in text:
        val = ord(char)
        for const in reversed(combined_constants):
            shift = (const % 7) + 1
            val = ((val >> shift) | (val << (8 - shift))) & 0xFF
        decrypted_text += chr(val)
    return decrypted_text
    
