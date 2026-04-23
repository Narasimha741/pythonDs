s="abbaaabb"
c=1
f=0
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c=c+1
        if c>=3:
            f=1
            break
    else:
        c=1
if f==1:
    print("spam")
else:
    print("not a spam")         
