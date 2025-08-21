n = int(input("Enter a number: "))
x = n
sum = 0
while x!=0:
    s=x%10
    sum+=s
    x=x//10
if n%sum==0:
    print("Harshad no.")
else:
    print("Not a harshad no.")