import re
import sys
def extract_emails(filename):
    try:
        with open(filename,'r') as file:
            text=file.read()
            pattern=r'\b[A-Za-z0-9._%#+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails=re.findall(pattern,text)
            return emails
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        return[]
    except Exception as e:
        print(f"An error occured: {e}")
        return[]

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: python rela.py <filename>")
    else:
        filename=sys.argv[1]
        extracted_emails=extract_emails(filename)
        if extracted_emails:
            print("Extracted Email Addresses")
            for i in extracted_emails:
                print(i)
        else:
            print("No email addresses found!")
