a=int(input("Enter a year!"))
if(a%400==0):
    print(a,"is a leap year.")
else:
    print(a,"is not a leap year.")

#2
print("Enter length and breadth")
a=int(input())
b=int(input())
if(a==b):
    print("It's a square.")
else:
    print("It's a rectangle.")

#3
print("Input the ages of three persons A,B and C")
A=int(input())
B=int(input())
C=int(input())
if(A>B and A>C):
    print("A is the oldest")
    if(B>C):
        print("C is the youngest.")
    else:
        print("B is the youngest.")
if(B>A and B>C):
    print("B is the oldest")
    if(A>C):
        print("C is the youngest.")
    else:
        print("A is the youngest.")
if(C>B and C>A):
    print("C is the oldest")
    if(B>A):
        print("A is the youngest.")
    else:
        print("B is the youngest.")

#4
print("Enter age, sex(m/f), and marital status(y/n)")
age=int(input())
sex=input()
ms=input()
if(type(age)!="int" and sex not in ['m','f'] and ms not in ['y','n']):
    print("INVALID INPUT!")
    exit()
if(sex == "f" or (sex=="m" and age>=40 and age<=60)):
    print("You will work in urba areas")
else:
    print("You can work anywhere!")

#5
a=int(input("Enter th enumber of quantity purchased."))
cost=100*a
if(cost>=1000):
    cost = cost - 0.1*cost
print("Yayy you get a discount of 10% on this purchase. Bill amount:",cost)