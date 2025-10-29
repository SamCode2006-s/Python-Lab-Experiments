import re
pattern=r"\w+"
try:
    with open("mystory.txt",'r') as s:
        l=s.read()
        count=re.findall(pattern,l)
    print(len(count))
except FileNotFoundError:
    print("Error: File not found!")

    