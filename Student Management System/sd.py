sd=[]
print("Welcome to Student Management System!\n1: Enter Student Details\n2: Print Student List\n3: Average of Class and Top Performers\n4: Low Marks and Attendance Students\n5: Groups\n6: Exit")
while True:
    c=int(input("Choose: "))
    if(c==1):
        name=input("Enter name of student: ")
        marks=int(input("Enter student marks: "))
        att=int(input("Enter attendance: "))
        sd.append([name,marks,att])
    elif(c==2):
        for s in sd:
            print(s,"\n")
    elif(c==3):
        su=0
        ch=[]
        for s in sd:
            su+=s[1]
        avg=su/len(sd)
        print(f"Average of class: {avg}")
        print("Top Performers:\n")
        for i in range(3):
            max=sd[0]
            for s in range(len(sd)):
                if(max[1]<sd[s][1] and sd[s] not in ch):
                    max=sd[s]
            ch.append(max)
            print(max)
    elif(c==4):
        for s in sd:
            if(s[2]<=75 and s[1]<=40):
                print(f"Student '{s[0]}' has low attendance ({s[2]}) and low marks ({s[1]})")
    elif(c==5):
        exc=[]
        go=[]
        av=[]
        ni=[]
        for s in sd:
            if(s[1]>=90):
                exc.append(s[0])
            elif(s[1]>=75):
                go.append(s[0])
            elif(s[1]>=40):
                av.append(s[0])
            else:
                ni.append(s[0])
        print(f"Excellent: {exc}\nGood: {go}\nAverage: {av}\nNeeds Improvement: {ni}")
    elif(c==6):
        break
    else:
        print("Wrong Input Entered!!!")
        
    