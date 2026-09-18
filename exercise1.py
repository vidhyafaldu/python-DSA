#Create variables to store name, age, and city and display them.

name=input("enter name")
age=int(input("enter age"))
city=input("enter city")
print(name)
print(age)
print(city)

#Swap the values of two variables.

a=12
b=10
print("before swaping")
print("a:",a)
print("b:",b)

temp=a
a=b
b=temp
print("after swaping")
print("a:",a)
print("b:",b)


#Calculate the area of a rectangle using variables.

length=10.5
width=12.2
area=length * width
print("area of reactangle:",area)
#print(f"area of reactangle:{area}")

#Calculate simple interest using variables.
p=float(input("enter principal"))
r=float(input("enter rate"))
t=float(input("enter time"))
interest=p*r*t/100
print("interest of simple interest",interest)



#Convert Celsius temperature to Fahrenheit.

celsius=float(input("enter celsius "))
fer=(celsius * 1.8)+32
print("celsius to ",celsius)
print("fahrenheit",fer)
