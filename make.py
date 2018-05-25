#!/usr/bin/env python3

# Source: https://stackoverflow.com/a/30375198

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


# Source: https://stackoverflow.com/a/9758173

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def asnlen(data):
    n = len(data)

    if n <= 127:
        return bytes([n])
    else:
        out = int_to_bytes(n)
        out = bytes([0x80 | len(out)]) + out
        return out


# Source: https://primes.utm.edu/largest.html

p = 2**77232917 - 1 # First prime
q = 2**74207281 - 1 # Second prime

n = p * q           # Modulus
e = 65537           # Public exponent
phi = (p-1) * (q-1) # Euler's totient
d = modinv(e, phi)  # Private exponent
dp = d % (p-1)      # CRT exponent 1
dq = d % (q-1)      # CRT exponent 2
crt = modinv(q, p)  # CRT coefficient


items = [0, n, e, d, p, q, dp, dq, crt]

out = b''

for item in items:
    data = int_to_bytes(item)
    dlen = asnlen(data)
    out += b'\x02' + dlen + data

out = b'\x30' + asnlen(out) + out

with open('key.der', 'wb') as f:
    f.write(out)
