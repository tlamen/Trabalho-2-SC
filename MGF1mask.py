from SHA1hash import sha1

def mgf1(seed, mask_len):
    mask = b''
    counter = 0
    while len(mask) < mask_len:
        counter_bytes = counter.to_bytes(4, 'big')
        data = seed + counter_bytes
        hash_output = sha1(data)
        mask += hash_output
        counter += 1
    return mask[:mask_len]