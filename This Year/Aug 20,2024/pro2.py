"""
String Decoder

You have provided with the string which has sequence of ones and zeros. This sequence is encoded version of an English word You are supposed to write a programme to decode the provided string and find the original word.Each upper case alphabet is represented by a sequence of ones

input : S = "10111011"
ouput : ACB

"""
def StringDecoder(S:str) -> str:
    res = ''
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    String = S.split("0")
    for i in String:
        res += alphabets[len(i)-1]
    return res


S = input()
print(StringDecoder(S))