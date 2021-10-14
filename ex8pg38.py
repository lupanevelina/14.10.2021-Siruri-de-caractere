a=str(input("Introdu sirul de caractere: "))
#1
a1=""
for i in a:
    if (ord(i)>=65) and (ord(i)<=89) :
        a1+=chr(ord(i)+1)
    else:
        a1+=i
print("a)",a1)
#2 
a2=""       
for i in range(0,len(a)) :
    a2=a.replace("Z","A")
print("b)",a2)
#3
a3=""
for i in range(0,len(a)) :
    a3=a.replace(" ","-")
print("c)",a3)



