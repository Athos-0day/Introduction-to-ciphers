import random, sys, os, PrimeNumber, CryptoMath

def createKey(keysize : int) :

    #First step : generate two prime number with keysize
    p,q = 0,0

    while p==q :
        p = PrimeNumber.generateLargePrimeNumber(keysize)
        q = PrimeNumber.generateLargePrimeNumber(keysize)
    
    n = p*q

    #Second step : create e which is relatively prime to (p-1)*(q-1)
    e = random.randrange(2**(keysize-1),2**(keysize))

    while CryptoMath.gcd(e,(p-1)*(q-1))!=1 :
        e = random.randrange(2**(keysize-1),2**(keysize))
    
    #Third step : calculate d
    d = CryptoMath.modInverse(e,(p-1)*(q-1))

    PublicKey = (n,e)
    PrivateKey = (n,d)

    return PublicKey,PrivateKey

def MakeKeyFiles(name,keySize) :

    publicKey,privateKey = createKey(keySize)

    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()

