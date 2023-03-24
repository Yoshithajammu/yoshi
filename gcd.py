 
def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
a = int(input())
b = int(input())
 
print ("The gcd of a and b is : ",end="")
print (computeGCD(a,b))
