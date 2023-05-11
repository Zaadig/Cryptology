# -*- coding: utf-8 -*-
import common
import rsa


def test_gen_rsa():
    e, d, N = rsa.gen_rsa(512)
    assert e != d, "Public exponent 'e' should not be equal to private exponent 'd'"
    assert e < N, "Public exponent 'e' should be less than the modulus 'N'"
    assert d < N, "Private exponent 'd' should be less than the modulus 'N'"
    assert common.pgcd(e, N) == 1, "Public exponent 'e' and modulus 'N' should be coprime"
    assert common.pgcd(d, N) == 1, "Private exponent 'd' and modulus 'N' should be coprime"


def test_enc_rsa():
    e, d, N = rsa.gen_rsa(512)
    m = 123456789
    c = rsa.enc_rsa(m, e, N)
    assert c != m
    assert c < N

def test_dec_rsa():
    e, d, N = rsa.gen_rsa(512)  # Use the same generated key pair
    m = 123456789
    c = rsa.enc_rsa(m, e, N)
    m2 = rsa.dec_rsa(c, d, N)
    print(c, m, m2)
    assert m == m2

    

def test_RSAcipher():
    e, d, N = rsa.gen_rsa(512)
    m = "ceci est le message de la question"
    c = rsa.RSAcipher(e, N, m)
    assert c != m
    assert c < N

def test_RSAdecipher():
    e, d, N = rsa.gen_rsa(512)
    m = "ceci est le message de la question"
    c = rsa.RSAcipher(e, N, m)
    m2 = rsa.RSAdecipher(d, N, c)
    assert m == m2
    
def test_signature_verification():
    # Generate RSA keys
    e, d, N = rsa.gen_rsa(512)

    # Define two messages
    message1 = "Hello, world!"
    message2 = "This is an invalid message."

    # Sign the first message
    signature = rsa.RSAsignature(d, N, message1)

    # Verify the signature for the first message (should return True)
    is_valid = rsa.RSAverification(e, N, message1, signature)
    assert is_valid, "Signature verification failed for the first message"

    # Verify the signature for the second message (should return False)
    is_valid = rsa.RSAverification(e, N, message2, signature)
    assert not is_valid, "Signature verification succeeded for the second message"



if __name__ == "__main__":
    test_gen_rsa()
    test_enc_rsa()
    test_dec_rsa()
    test_RSAcipher()
    test_RSAdecipher()
    test_signature_verification()
    print("Everything passed")