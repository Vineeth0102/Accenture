input1 = input("Ente the string : ")
input1 = input1.lower()
res = 1
val = 1
for i in input1 :
    if not (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ):
        res *= val
        val+=1
print(res)    
