i=1
a=1
c=0
sum=0
l=4000000
while i<l:  
    if i%2==0:
        sum=sum+i
    c=i+a
    i=a
    a=c
print(sum)