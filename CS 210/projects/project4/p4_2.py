def encrypt(msg:str)->str:
    text=""
    rail1=""
    rail2=""
    rail3=""

    for i in range(len(msg)):
        if i%3 == 0:
            rail1=rail1+msg[i]
        elif i%3 == 1:
            rail2=rail2+msg[i]
        else:
            rail3=rail3+msg[i]

    text=rail1+rail2+rail3

    return text


def decrypt(msg:str)->str:
    text=""
    third=len(msg)//3
    if len(msg)%3==0:
        rail1=msg[:third]
        rail2=msg[third:third*2]
        rail3=msg[third*2:]
    elif len(msg)%3==1:
        rail1=msg[:third+1]
        rail2=msg[third+1:third*2+1]
        rail3=msg[third*2+1:]
    elif len(msg)%3==2:
        rail1=msg[:third+1]
        rail2=msg[third+1:third*2+2]
        rail3=msg[third*2+2:]
    print(rail1)
    print(rail2)
    print(rail3)

    for i in range(len(rail1)):
        if i<len(rail3):
            text=text+rail1[i]
            text=text+rail2[i]
            text=text+rail3[i]
        elif i<len(rail2):
            text=text+rail1[i]
            text=text+rail2[i]
        else:  
            text=text+rail1[i]
    return text

print(encrypt("The true sign of intelligence is not knowledge but imagination."))
print(decrypt(encrypt("The true sign of intelligence is not knowledge but imagination.")))