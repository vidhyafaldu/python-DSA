#Write a function to print "Hello, World!".

def hello():
   print("hello world")
hello()

#Write a function that takes a name and prints a greeting.
def greet(name):
    print("hello",name)
greet("abc")

#Write a function to add two numbers.
def sum(a,b):
    return a + b;
res=sum(2,3);
print(res)

#Write a function to find the square of a number.
def squ(n):
    return n*n;
res=squ(5)
print(res)

#or
a=int(input("enter number"))
def squ():
     res= a * a;
     print(res)
squ()

#Write a function to check whether a number is even or odd.
def odevn():
    a=int(input("enter number"))
    if(a % 2== 0):
       print("number is even")
    else:
       print("number is odd")

odevn()

#Write a function to find the maximum of two numbers.
def max():
    a=int(input("enter a number "))
    b=int(input("enter b number "))
    if(a>b):
        print("a is big ")
    else:
        print("b is max")
max()

#Write a function to convert Celsius to Fahrenheit.
def celtofr(c):
    fer=(c * 1.8) + 32
    return fer

c=float(input("enter a Celsius "))
fer=celtofr(c)
print("cel is ",c , "fernhit is ",fer)


#Write a function to calculate the area of a circle.

 
PI=3.14
def aoc():
    area=PI *r *r
    return area
r=int(input("enter a numebr"))
area=aoc()
print(area)

#Write a function to calculate the factorial of a number.

a=int(input("enter number "))

def factno(a):
    fact=1
    for i in range(1,a+1):
       fact =fact * i
    return fact
print("factorial number ", factno(a) )

#Write a function to check whether a number is positive, negative, or zero.

a=int(input("enter number "))
if a>0:
    print("number is positive",a)
elif(a<0):
    print("number is negative",a)
else:
    print("number is zero",a)
    

#Write a function to find the maximum of three numbers.

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print("max number is ",max(a,b,c))
      

#Write a function to count vowels in a string
text=input("enter string")
def vowel_dm(text):
    count=0
    for i in text:
        if i in "aeiouAEIOU":
            count +=1
    return count
print(vowel_dm(text))
        


#13.Write a function to reverse a string.
str=input("enter name")
def rev_str(text):
    return text[::-1]
print("reverse is",rev_str(text))
    
#Write a function to check whether a string is a palindrome.
a=input("enter string")
def palin_str(text):
    if text == text[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
print(palin_str(a))
        
    
#Write a function to find the sum of all elements in a list.
def sum_num(number):
    return sum(number)
print(sum_num([10,20,30]))


#Write a function to find the largest element in a list

a=[10,70,65,80]
def large_my(numbers):
    large=numbers[0]
    for n in numbers:
        if n> large:
            large=n
    return large
print(large_my(a))



#Write a function to remove duplicate elements from a list.

a=[10,78,98,78,10,20,30,20]
def dul_val(number):
    new_val =[]
    for n in number:
        if n not in new_val:
            new_val.append(n)
    return new_val
print(dul_val(a))


#Write a function to count how many times an element appears in a list.

a=[10,20,30,10,10]
def ele_count(num,element):
    count=0
    for n in num:
        if n == element:
            count +=1
    return count
print(ele_count(a,10))


#Write a function to check whether a number is prime.

n=int(input("enter number"))
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i== 0:
            return False
    return True
if is_prime(n):
    print("prime")
else:
    print("not prime")


#Write a function to return all prime numbers between two numbers. 
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i==0:
           return False
    return True
def prime_btw(start, end):
    primes=[]
    for n in range(start,end+1):
        if is_prime(n):
            primes.append(n)
    return primes
print(prime_btw(10,20))

#Write a function to calculate Fibonacci numbers.
n=int(input("enter number"))
def fibonaci_ser(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a,b=b,a+b
fibonaci_ser(n)
#Write a function to find the second-largest number in a list.
a=[10,20,30,40]
def sec_larg(a):
    largest=max(a)
    a.remove(largest)
    return max(a)
print(sec_larg(a))
#Write a function to sort a list without using sort().
a=[20,10,11,32,12]
def sort_list(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]> a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
print(sort_list(a))
#Write a function to merge two lists and remove duplicates.
list1=[10,20,30]
list2=[23,30,20]
def merge_list(list1,list2):
    result=[]
    for n in list1+list2:
        if n not in result:
            result.append(n)
    return result
print(merge_list(list1,list2))

            
        
















    
