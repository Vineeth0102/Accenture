input1= input("Enter the String : ")

input1 = input1.split(".")

print(max([len(i) for i in input1]))