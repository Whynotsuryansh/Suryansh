n=input("enter a value")
rev=""
for i in range(len(n)):
    rev=n[i]+rev
if rev==n:
    print("palindrom")
else:
    print("not")
