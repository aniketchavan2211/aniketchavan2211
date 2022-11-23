## Openssl

Install OpenSSL 

```bash
apt install openssl openssl-tool
```

```bash
sudo apt install openssl openssl-tool
```

**all ciphers***

```bash
openssl enc -ciphers
```


### Encrypting

```bash
openssl enc -aes-256-cbc -md sha512 -pbkdf2 -iter 10000 -salt -in <Message file> -out <Encrypted file.enc> 
```

### Decrypting

```bash
openssl enc -aes-256-cbc -md sha512 -pbkdf2 -in <encrypted file.enc> -out <decrypted file> -d
```
