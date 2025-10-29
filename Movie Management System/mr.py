movie=[]
print("Welcome to Movie System!\n1: Enter Movie Details\n2: Print Movies List\n3: Search by Genre\n4: Search by Min Rating\n5: Movie Recommendations\n6: Top 10\n7: Watch History\n8: Exit")
while True:
    c=int(input("Choose:"))
    if(c==1):
        title=input("Enter title of Movie: ")
        genre=input("Enter genre of Movie: ")
        rating=int(input("Enter rating of Movie: "))
        my=int(input("Enter release year of Movie: "))
        wc=int(input("How many times have you watched the Movie?: "))
        movie.append([title,genre,rating,my,wc])
        print(f"'{title}' Added Successfully!")
    elif(c==2):
        for m in movie:
            print(m)
    elif(c==3):
        v=0
        g=input("Enter genre of choice: ")
        for m in movie:
           if(g is m[1]):
               print(m)
               v+=1
        if(v==0):
            print("No movies in specific genre found!")
    elif(c==4):
        v=0
        r=int(input("Enter minimum rating required: "))
        for m in movie:
            if(m[2]>=r):
                print(m)
                v+=1
        if(v==0):
            print("No movies in this rating range found!")
    elif(c==5):
        rec=[]
        for m in movie:
            if(m[4]>0):
                rec.append[m[1]]
        print("Movie Recommendations:")
        for m in movie:
            if(m[1] in rec and m[4]==0):
                print(m)
    elif(c==6):
        ch=[]
        for i in range(10):
            max=movie[0]
            for m in movie:
                if(max[2]<m[2] and m[2] not in ch):
                    max=m[2]
            print(f"{i+1}: {max[0]}")
            ch.append(max)
    elif(c==7):
        mw=[]
        print("Watch History: ")
        for m in movie:
            if(m[4]>0):
                mw.append([m[4],m[0]])
        mw.sort(reverse=True)
        for m in mw:
            print(f"{m[1]} --> {m[0]}")
    elif(c==8):
        break
    else:
        print("Wrong input entered!")
        
