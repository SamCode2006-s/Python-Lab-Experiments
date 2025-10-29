import random
wl=[]
d=[]
ca=[]
cs=[]
j=0
with open(r"C:\Users\s35sa\Downloads\5lw.txt") as l:
    words=l.read().splitlines()
word=random.choice(words).strip().upper()
for i in range(0,len(word)):
    wl.append(word[i])
while j<5:
    gl=[]
    caa=[]
    print("Guesses Remaining: ",(5-j))
    guess=input("Enter a 5 letter guess: ").strip().upper()
    if(len(guess)==5):
        for i in range(0,len(guess)):
            gl.append(guess[i])
        print(gl)
    else:
        print("Not a 5 letter word!")
        continue
    
    if(gl==wl):
        print("Correct!\nWord: ",guess)
        break
    

    else:
        for i in range(len(wl)):
            if(gl[i] in wl):
                if(gl[i]==wl[i] and gl[i] not in cs):
                    cs.append(gl[i])
                else:
                    if(gl[i] not in ca and gl[i] not in cs):
                        ca.append(gl[i])
            else:
                if(gl[i] not in d):
                    d.append(gl[i])

            for i in range(len(ca)):
                if(ca[i] not in cs and ca[i] not in caa):
                    caa.append(ca[i])

    print("Almost: ",caa)
    print("Correct: ",cs)
    print("No: ",d)
    j=j+1

if(j==5):
    print("Guesses Over\nThe Correct Answer was: ",word)