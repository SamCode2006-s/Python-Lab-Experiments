import re
import sys
def sp(filename,patstr):
    try:
        compat=re.compile(patstr)
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        return
    try:
        with open(filename,'r') as file:
            ln=0
            flag=0
            for line in file:
                ln+=1
                if compat.search(line):
                    print(f"Line {ln}: {line.strip()}")
                    flag=flag+1
        if(flag==0):
            print("Text not found!")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")
if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Usage: python patsch.py <filename> <patstr>")
    else:
        filename=sys.argv[1]
        pat_str=sys.argv[2]
        sp(filename,pat_str)
