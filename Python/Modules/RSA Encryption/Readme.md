## RSA Encryption

### Table of Content
- What is Asymmetric Encryption
- What is Digital Signatures?
- What is RSA?
- RSA in Data Encryption
- Advantage of RSA

### What is Asymmetric Encryption

Two different keys are used in Asymmetric Encryption.
Private key is used for encrypting the data, and pubic key is used for decrypting the data.

`Sender` **encrypt** text with `public key` of `receiver`
encryted text(cipher text) is then transmitted to receiver,and **decrypt** by `receiver private key`.

public keys are publically avaiable to everyone
and private keys are keep private.

### What is Digital Signatures?

- Mechanism to determine autenticity of a document file
- Uses public key cryptography mechansim
- Helpful to authenticate long distance official communication channels.

Maintain Integrity, is document is altered during transmission
is check digital signatures and public key cryptography.

private key and public keys are linked together.

system uses private key to encrypt and uses
public key to decrypt.

document is passwd through hash function, return hash digest
then it bundle with file and encrypting using
private key of sender, and receiver decrypt
file with sender public key and check for hash digest, receiver passed to hash function,
and compare the both hash digest, to verfy 
integrity of document, if it match then document is from sender and not been change during tranfer. if not match then 
data is alter, not from sender.

sender signed the file when encryptiion
with private key, so who created file and

### Types of Implementation

- RSA(Rivest-Shamir-Adieman)
- DSA

### What is RSA

- Rivest-Shamir-Adieman algorithm, named after it's 3 founders.
- First published 1977
- Along with signature verification, it can be used for encryption an ddecryption of standard data.

plain text is passed through hash function return hash digest and
encrypted using sender private key, once receiver receive
the bundle plain text passed on hash function then output of hash function with compare with 
hash digest which sender sends data.

### RSA in Data Encryption

- key scope is reserved.
- public key of receiver is used to encrypt data.
- private key of receiver is used to decrypt data.
- key exchange not necessary.

**Two Components**
- key generation
- encryption/decryption

### Steps in RSA

**Key Generation**
1. Two large prime numbers are chosen (`p` and `q`).
2. compute `n = p * q` and `z = (p-1)(q-1)`.
3. choose a number `e` where `1 < e < (p-1)(q-1)`.
4. A number `d` is selected so that `ed mod z = 1` and 
calculated as `d = e^-1 mod (p-1)(q-1)`.
5. public key is `(n, e)` and private key is `(n, d)`

**Encryption and decryption**

if the plaintext is **m**, encrypted ciphertext c is
calculated as:
```
c = m^e mod n
```

Under similiar assumptions, the plaintext can be
calculated as:
```
m = c^d mod n
```

**Data Encryption Example**
1. Choose p and q as 7 and 13 respectively,
so that `n=p*q=91`.
2. We can select value of e to be 5 since it satisfies 
`1<e<(p-1)(q-1)`.
3. Value of **d** = `e^-1 mod(p-1)(q-1) = 29`.
4. public key = `(91, 5)`, private key = `(91, 29)`
5. let plaintext **m** be **10**.

ciphertext(c) = `m^e mod n = 82`
plaintext = `c^d mod n = 10`.

### Advantages of RSA

- No need of sharing secret keys
- proof of owner's authenticity
- faster encryption than DSA
- Data can't be modified in transmit
