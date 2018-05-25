# meRSAnne: the largest RSA key in the world!

This, at the time of publishing, is the largest RSA key in the world, built from two largest Mersenne primes found so far. The modulus is 151440198 bits long.

Included is the compressed DER-encoded private and public key files, as well as a Python program to generate a private key file given two primes (the latter is probably the only useful thing in here). *Calculating CRT exponents is what took most time in my case.*

## FAQ

**Why?** I was bored.

**Does it have any practical use?** Not really, the key size is too big for any practical use. Besides, since both primes are publicly known, it doesn't provide any level of security whatsoever.

## Acknowledgements

* [Top primes by length — Prime Pages](https://primes.utm.edu/largest.html)
* [Modular multiplicative inverse in Python](https://stackoverflow.com/a/9758173)
* [Convert integer to bytes in Python](https://stackoverflow.com/a/30375198)
