number1,operator,number2=map(str,input("Enter the expression: ").split())
number1=int(number1) 
number2=int(number2)

def add(n1,n2):
    print("Additon of ",str(n1)," and ",str(n2)," is: ",str(n1+n2))

def subtract(n1,n2):
    print("Subtarction of ",str(n1)," and ",str(n2)," is: ",str(n1-n2))

def division(n1,n2):
    print("Division of ",str(n1)," and ",str(n2)," is: ",str(n1/n2))

def multiply(n1,n2):
    print("Multiplication of ",str(n1)," and ",str(n2)," is: ",str(n1*n2))

def modulus(n1,n2):
    print("Modulus of ",str(n1)," and ",str(n2)," is: ",str(n1%n2))

if operator== '+':
    add(number1,number2)
elif operator=='-':
    subtract(number1,number2) 
elif operator=='/':
    division(number1,number2)
elif operator=='*':
    multiply(number1,number2)
elif operator=='%':
    modulus(number1,number2)
else:
    print("Invalid typo error!!")