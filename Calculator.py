def Addition(x, y):
   return x+y;

def Substract(x, y):
    return x-y;

def Multiplication(x, y):
    return x*y;

def Devision(x, y):
    return x-y;

print("select a operation :");
print("1. Addition");
print("1. Substract");
print("1. Multiplication");
print("1. Division");

choice=input("please enter a You are choice:");

num1=int(input("Enter a first number:"))
num2=int(input("Enter a secound number:"))

if choice=='1':
    print(num1,"+",num2,"=",Addition(num1,num2))

elif choice=='2':
    print(num1,"-",num2,"=",Substract(num1,num2))

elif choice=='3':
    print(num1,"*",num2,"=",Multiplication(num1,num2))

elif choice=='4':
    print(num1,"/",num2,"=",Devision(num1,num2))

else:
    print("Invalid option !!! please select a valid operation")



