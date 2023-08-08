R = input()
R = R.lower()
s = ""
L = ['a' , 'e' , 'i' , 'o' , 'u' , 'y']
for i in range(0,len(R)):
    if R[i] not in L:
        s+='.'
        s+=R[i]
        
print (s)