print("Simple calculator\nEnter 2 numbers:")
a=int(input())
b=int(input())
print("Choose:-\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
c=int(input())
if(c==1):
    s=a+b
    print("The answer is: ",s)
elif(c==2):
    if(a>b):
        s=a-b
        print("The answer is: ",s)
    else:
        s=b-a
        print("The answer is: ",s)
elif(c==3):
    s=a*b
    print("The answer is: ",s)
elif(c==4):
    if(b!=0):
        s=a/b
        print("The answer is: ",s)
    else:
        print("Denominator cannot be zero")
else:
   print("Wrong command entered")

    