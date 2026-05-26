def karas_cipher_encrypt(text):
    file_bytes = bytes.fromhex("025F8D1C4EA239BB741A5C990D2F41")
    hash_val = bytes.fromhex("9A6EC012E1A7DA9DBE34194d478AD7C0DB1822FB071DF12981496ED104384113")
    h_int = int.from_bytes(hash_val, 'big')
    f_int = int.from_bytes(file_bytes, 'big')
    combined_constants = sorted([h_int, f_int], reverse=True)
    encrypted_text = ""
    for char in text:
        shifted_char = ord(char) + 2
        for const in combined_constants:
            shift_amount = (const % 8) + 1
            shifted_char = ((shifted_char << shift_amount) | (shifted_char >> (8 - shift_amount))) & 0xFF
        if not (32 <= shifted_char <= 126):
            shifted_char = 32 + (shifted_char % 95)
        encrypted_text += chr(shifted_char)
    return encrypted_text

def karas_cipher_decrypt(text):
    file_bytes = bytes.fromhex("025F8D1C4EA239BB741A5C990D2F41")
    hash_val = bytes.fromhex("9A6EC012E1A7DA9DBE34194d478AD7C0DB1822FB071DF12981496ED104384113")
    h_int = int.from_bytes(hash_val, 'big')
    f_int = int.from_bytes(file_bytes, 'big')
    combined_constants = sorted([h_int, f_int], reverse=True)
    decrypted_text = ""
    for char in text:
        shifted_char = ord(char)
        if not (32 <= shifted_char <= 126):
             shifted_char = 32 + (shifted_char % 95)
        for const in reversed(combined_constants):
            shift_amount = (const % 8) + 1
            shifted_char = ((shifted_char >> shift_amount) | (shifted_char << (8 - shift_amount))) & 0xFF
        decrypted_text += chr(shifted_char - 2)
    return decrypted_text
