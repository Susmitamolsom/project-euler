i=1
a=0
sum=0
c=1
while i<=100:
    sum=sum+i
    a=c+a
    i=i+1
    c=i**2
print(sum**2-a)