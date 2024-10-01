a=10
b=20
c=30
acount=0
bcount=0
ccount=0
avg=(a+b+c)/3
if a<avg:
 acount=+1
elif b<avg:
 bcount=+1
elif c<avg:
 ccount=+1
elif acount>0 and bcount>0:
 print("a and b are going slower than average")
elif acount>0 and ccount>0:
 print("a and c are going slower than average")
elif bcount>0 and ccount>0:
 print("b and c are going slower than average")
else:
 print("Noone is going slower than average")