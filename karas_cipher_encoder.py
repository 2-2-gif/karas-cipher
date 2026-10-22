def karas_cipher_encrypt(text):
    o = ""
    shift = 1 
    text_len = len(text)
    for c in text:
        val = ord(c)
        v = val + shift
        while v > 158900:
            v -= 158900
        o += chr(v)
        shift += 1
        if text_len <= 158900:
            if shift > text_len: shift = 1
        else:
            if shift > 158900: shift = 1
    return o

def karas_cipher_decrypt(text):
    d = ""
    shift = 1
    text_len = len(text)
    for c in text:
        val = ord(c)
        v = val - shift
        while v < 0:
            v += 158900
        d += chr(v)
        shift += 1
        if text_len <= 158900:
            if shift > text_len: shift = 1
        else:
            if shift > 158900: shift = 1
    return d