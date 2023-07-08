import struct


def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


def sha1(message):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    ml = len(message) * 8
    message += b'\x80'
    while (len(message) % 64) != 56:
        message += b'\x00'
    message += struct.pack('>Q', ml)

    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        w = list(struct.unpack('>16I', chunk) + (None,) * 64)

        for j in range(16, 80):
            w[j] = left_rotate((w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16]), 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for j in range(80):
            if j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + w[j] & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    hash_bytes = bytes([h0 >> 24, h0 >> 16 & 0xff, h0 >> 8 & 0xff, h0 & 0xff,
                       h1 >> 24, h1 >> 16 & 0xff, h1 >> 8 & 0xff, h1 & 0xff,
                       h2 >> 24, h2 >> 16 & 0xff, h2 >> 8 & 0xff, h2 & 0xff,
                       h3 >> 24, h3 >> 16 & 0xff, h3 >> 8 & 0xff, h3 & 0xff,
                       h4 >> 24, h4 >> 16 & 0xff, h4 >> 8 & 0xff, h4 & 0xff])

    return hash_bytes
