import csv
def write_and_read_text_file(filename="example.txt"):
    print(f"---Working with a text file ({filename})---")
    with open(filename,'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line.\n")
        print("Successfully wrote to the text file.")
    with open(filename,'r') as file:
        content=file.read()
        print("\nContent of the text file:")
        print(content)
def write_and_read_csv(filename="data.csv"):
    print(f"---Working with a CSV file ({filename})---")
    data=[['Name','Age','City'],['ABC',20,'MUMBAI'],['DEF',25,'BADLAPUR'],['EFG',35,'KHARGHAR']]
    with open(filename,'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerows(data)
        print("Successfully wrote to the csv file.")
    with open(filename,'r') as file:
        reader=csv.reader(file)
        print("\nContent of the csv file:")
        for row in reader:
            print(row)

write_and_read_text_file()
print("\n"+"="*40+"\n")
write_and_read_csv()