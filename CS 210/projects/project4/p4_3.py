alphabet = "abcdefghijklmnopqrstuvwxyz"
rot13 = "nopqrstuvwxyzabcdefghijklm"

def encrypt(msg: str) -> str:
    encrypted = ""
    msg = msg.lower() 
    for i in range(len(msg)):
        if msg[i] in alphabet:
            encrypted += rot13[alphabet.index(msg[i])]
        else:
            encrypted += msg[i]
    return encrypted

def decrypt(msg: str) -> str:
    decrypted = ""
    for i in range(len(msg)):
        if msg[i] in alphabet:
            decrypted += alphabet[rot13.index(msg[i])]
        else:
            decrypted += msg[i]
    return decrypted
