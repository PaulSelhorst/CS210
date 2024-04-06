import p4_1
import p4_2
import p4_3

def crypt(msg:str, mode:str)->str:
    if mode== p4_1.encrypt:
        return p4_1.encrypt(msg)
    elif mode== p4_2.encrypt:
        return p4_2.encrypt(msg)
    elif mode== p4_3.encrypt:
        return p4_3.encrypt(msg)
    elif mode== p4_1.decrypt:
        return p4_1.decrypt(msg)
    elif mode== p4_2.decrypt:
        return p4_2.decrypt(msg)
    elif mode== p4_3.decrypt:
        return p4_3.decrypt(msg)

    
print(crypt("There is no reason anyone would want a computer in their home.", p4_2.encrypt))

print(crypt("Trinrs yeoda cpeitihehesoeoao u naournhro.e   annnwlwt mt  e m", p4_2.decrypt))