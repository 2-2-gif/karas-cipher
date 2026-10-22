KARAS_SIGNATURE = 0x476D05EC2E77D80DF6D38E
BITS = 32
MASK = (1 << BITS) - 1

def rol(val, shift, bits=BITS):
    shift %= bits
    return ((val << shift) | (val >> (bits - shift))) & MASK

def ror(val, shift, bits=BITS):
    shift %= bits
    return ((val >> shift) | (val << (bits - shift))) & MASK

def derive_karas_delta(text_len, index):
    sig_32 = KARAS_SIGNATURE & MASK
    
    new_const = rol(sig_32, text_len)
    new_const_2 = ror(sig_32, text_len)
    
    term1 = rol(new_const, index)
    term2 = ror(new_const, index)
    term3 = rol(new_const_2, index)
    term4 = ror(new_const_2, index)
    
    return term1 ^ term2 ^ term3 ^ term4

def karas_cipher_encrypt(text):
    o = ""
    shift = 1
    text_len = len(text)
    
    for idx, c in enumerate(text):
        val = ord(c)
        delta = derive_karas_delta(text_len, idx + 1)
        
        v = val + shift + delta
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
    
    for idx, c in enumerate(text):
        val = ord(c)
        delta = derive_karas_delta(text_len, idx + 1)
        
        v = val - shift - delta
        while v < 0:
            v += 158900
            
        d += chr(v)
        
        shift += 1
        if text_len <= 158900:
            if shift > text_len: shift = 1
        else:
            if shift > 158900: shift = 1
            
    return d