def encrypt(msg: str) -> str:
    even = ""
    odd = ""
    for i in range(len(msg)):
        if i % 2 == 0:
            even += msg[i]
        else:
            odd += msg[i]
    encrypted = odd + even
    return encrypted

def decrypt(msg: str) -> str:
    half = len(msg) // 2
    odd = msg[:half]
    even = msg[half:]
    msg = ""
    for i in range(half):
        msg += even[i]
        msg += odd[i]
    if len(even) > len(odd):
        msg += even[-1]
    return msg
