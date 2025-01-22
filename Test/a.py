# print("Greatest of three")
n1=float(input("enter a number"))
n2=float(input("enter a number"))
n3=float(input("enter a number"))
if n1>n2 and n1>n3:
    print(n1,"is greater" )
elif n2>n1 and n2>n3:
    print(n2,"is greater")
else:
    print(n3,"is greater")


print("question 5")
n=5
def fibonocci(n):
    if n<=1:
        return 1
    return fibonocci(n-1)+fibonocci(n-2)
print('0')
for i in range(1,n):
    print(fibonocci(i))

print("question 6")
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuZZ")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

print('question 7')
n=int(input('enter a number'))
for i in  range(1,n+1):
    if n%i==0:
        print(i)

print('question 8')
n=int(input('enter a number: '))
n1=str(n)
count=0
sum=0
product=1
for i in range(0,len(n1)):
    count+=1
    sum+=int(n1[i])
    product=product*int(n1[i])
print(count,'count of digits')
print(sum,'sum')
print(product,'product')

print('question 10')
n=int(input('enter a number'))
sum=0
for i in range(1,n):
    if n%i==0 :
        sum+=i
if n==sum:
    print('perfect number')
else:
    print('not a perfect number')

print('question 1')
n=int(input('enter a number'))
if n<=100:
    print((n*5)+50,'rupees')
elif n>100 and n<=200:
    print((n*7)+50,'rupees')
elif n>200:
    print((n*10)+50,'rupees')
else:
    print('enter units between 1 to 200')

print('question 4')
fact=int(input('enter a number'))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(fact)) 


   
print('question 11')
n=int(input('enter a number'))
count=0
def CC(n):
    if n==1:
       return 
    if n%2==0:
      n1=n/2
      n=n1
      count+=1
      return CC(n)
    else:
     n2=3*n+1
     n=n2
     count+=1
     return CC(n)
print(CC(n))


print('Question 3')
while True:
    n = input('Enter 1-add, 2-sub, 3-mul, 4-div, or "exitCode" to exit: ')
    
    if n == 'exitCode':
        print("Exiting the program. Goodbye!")
        break 
    n1=int(n)
    while(n1!=0):  
        n = int(n)
        if n == 1:
            n1 = float(input('Enter n1: '))
            n2 = float(input('Enter n2: '))
            print(n1 + n2, 'Sum')
        elif n == 2:
            n1 = float(input('Enter n1: '))
            n2 = float(input('Enter n2: '))
            print(n1 - n2, 'Difference')
        elif n == 3:
            n1 = float(input('Enter n1: '))
            n2 = float(input('Enter n2: '))
            print(n1 * n2, 'Product')
        elif n == 4:
            n1 = float(input('Enter n1: '))
            n2 = float(input('Enter n2: '))
            print(n1 / n2, 'Division')
         else:
            print('Enter a valid input (1-4 or "exitCode").')
    else:
        print('Enter a valid number')
