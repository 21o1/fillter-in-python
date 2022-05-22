from time import sleep
import sys
print("""
 ██████╗ ██╗  ██╗██████╗ ██╗  ██╗██████╗ 
██╔═████╗╚██╗██╔╝██╔══██╗██║  ██║██╔══██╗
██║██╔██║ ╚███╔╝ ██████╔╝███████║██║  ██║
████╔╝██║ ██╔██╗ ██╔══██╗╚════██║██║  ██║
╚██████╔╝██╔╝ ██╗██████╔╝     ██║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═╝╚═════╝ 
coding by @i0xb4d , @21o1
""")
file1= ""
ui = ""
try:
    file1+=sys.argv[1]
    ui+=sys.argv[2]
except:
    file1 = input("enter the file path?\n>")
    ui = input("Enter The Word?\n>")
file = open(file1, 'r', encoding="utf-8")
ss = str(file.read())
a=0
b=1
c=0
fo = 0
pl=0
whe = 0
lnd=0
lines=1
pi=len(ui) 
da = ["0","x","b","4","d"]
as2=1
dw = 0
wrd=[]
places=[]
flen = len(ss)
print(f"Seaching About '{ui}' In '{file1}' File Len Is {flen}\n")
while a <len(ss) and as2 !=2:
    if dw == 5:
        dw=0
    print(f"Searching ...\032{da[dw]}\033...",end="\r")
    a1=a+pi
    if ui[0] == ss[a]:
        if a != len(ss)-1:
            if ui == ss[a:a1]:
                fo = 1
                places.append(ss[a-30:a]+ss[a:a+30]+"\n\nLetter number: "+str(a+1)+"\nLine Number: "+str(lines)+"\n"+"-"*100)
                
                
                
        else:
            if ui[1] == ss[a]:
                if ui == ss[a:a1]:
                   fo = 1
                   places.append(ss[a-50:a]+ss[a:a+100]+"\n\nLetter number: "+str(a)+"\nLine Number: "+str(lines)+"\n"+"-"*100)
                   
                   

    if ss[a:a+1] == "\n":
        lines+=1        
    if len(ss) <70:
        sleep(0.1)
    elif len(ss) > 1000:
        sleep(0)
    a+=1
    dw +=1
    if a == len(ss):
        as2+=1
    
dasd=0
asda=1    
da = a-20
da1 = a+20

if fo == 1:
    
    print("Proccess Done[+]")
    print(f"\nWord found[+]")
    
    for i3 in range(len(places)):
        print( str(asda)+": "+places[dasd]+"\n") 
        asda+=1
        dasd+=1
    
if fo == 0:
    
    print("Proccess Done[+]")
    print("\nWord dont found[-]")
    
    