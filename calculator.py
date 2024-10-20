
'''
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
ty=input("enter an option(+ - * / %):")
def calc(num1,num2,ty):
    if ty=='+':
        return num1+num2
    elif ty=='-':
        return num1-num2
    elif ty=='*':
        return num1*num2
    elif ty=='/':
        return num1/num2
    if ty=='%':
        return num1%num2

print(calc(num1,num2,ty))

'''
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def trueDiv(num1,num2):
    return num1/num2
def rem(num1,num2):
    return num1%num2
print('1.Addition')
print('2.Subtract')
print('3.Multiply')
print('4.Division')
print('5.Remainder')
operation=input('Enter any number  1  2  3  4  5:')
if operation=='1':
    return add(num1,num2)
    
