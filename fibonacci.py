a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
n = int(input("Input the number of items: "))

print("The values of a and b are:",a,b,end="")

while(n-2):
    c=a+b
    print("The value of c is: ",c)
    a=b
    print("The value of a is: ",a)
    b=c
    print("The value of b is: ",b)
    print(c,",",end=" ")
    n=n-1