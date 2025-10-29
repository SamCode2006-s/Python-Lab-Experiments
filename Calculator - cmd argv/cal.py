import sys

def cal(ch,n1,n2):
    if(ch=='+'):
        print(n1+n2)
    elif(ch=='-'):
        print(n1-n2)
    elif(ch=='*'):
        print(n1*n2)
    elif(ch=='/'):
        try:
            print(n1/n2)
        except ZeroDivisionError:
            print("Error: Cannot divide by 0!")
    else:
        print("Wrong operation!")

if __name__=="__main__":
    if len(sys.argv)!=4:
        print("Incorrect format of command line!!!")
    else:
        num1=sys.argv[1]
        num2=sys.argv[2]
        ch=sys.argv[3]
        try:
            n1=int(num1)
            n2=int(num2)
            cal(ch,n1,n2)
        except ValueError:
            print("Please enter integers!!!")
        