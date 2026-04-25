n=int(input("enter a number\n"))
m=n
sum=0
while n>0:
    rem=n%10
    sum=sum+rem**len(str(m))
    n=n//10
if m==sum:
    print("arm")
else:
    print("not arm")
