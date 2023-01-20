text = 'AAAABBBBBBBBBCCCCCCCC'
def rle_encode(decod):
    enstring = ''
    count = 1
    char = decod[0]
    for el in decod:
        if el == char:
            count +=1
        else:
            enstring = enstring+str(count)+char
            char = el
            count = 1
    enstring = enstring + str(count)+char       
    return enstring
print(rle_encode(text))  

def rle_decode(encod):
    destring = ''
    char = ''
    for i in range(len(encod)):
        if encod[i].isdigit():
            char+=encod[i]
        else:
            destring +=encod[i] * int(char)
            char = ''
    return destring
print(rle_decode(rle_encode(text)))                