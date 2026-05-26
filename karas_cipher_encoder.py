file_bytes = bytes.fromhex("025F8D1C4EA239BB741A5C990D2F41")
hash_val = bytes.fromhex("9A6EC012E1A7DA9DBE34194d478AD7C0DB1822FB071DF12981496ED104384113")
h_int = int.from_bytes(hash_val, 'big')
f_int = int.from_bytes(file_bytes, 'big')
rol_const = (((h_int ^ f_int) << 5) | ((h_int ^ f_int) >> 155)) & 0xFF

def karas_cipher_encrypt(text):
    o = ""
    for c in text:
        v = (((ord(c) + 2) & 0xFF) << 1 | ((ord(c) + 2) & 0xFF) >> 7) & 0xFF
        v = v ^ rol_const
        if v < 32: v += 32
        elif v > 126: v -= 32
        o += chr(v)
    return o

def karas_cipher_decrypt(text):
    d = ""
    for c in text:
        v = ord(c)
        if v < 64: v -= 32
        else: v += 32
        v = v ^ rol_const
        v = ((v >> 1) | (v << 7)) & 0xFF
        d += chr((v - 2) & 0xFF)
    return d
    
