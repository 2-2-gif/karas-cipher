KARAS_MAP = r' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def karas_to_code(char):
    for i, c in enumerate(KARAS_MAP):
        if c == char:
            return i + 33
    return 33

def code_to_karas(code):
    index = code - 33
    if 0 <= index < len(KARAS_MAP):
        return KARAS_MAP[index]
    return KARAS_MAP[0]

def karas_cipher_encrypt(text):
    o = ""
    shift = 1 
    for c in text:
        val = karas_to_code(c)
        v = val + shift
        while v > 126:
            v -= 94
        o += code_to_karas(v)
        shift += 1
        if shift > 94: shift = 1
    return o

def karas_cipher_decrypt(text):
    d = ""
    shift = 1
    for c in text:
        val = karas_to_code(c)
        v = val - shift
        while v < 33:
            v += 94
        d += code_to_karas(v)
        shift += 1
        if shift > 94: shift = 1
    return d
    
