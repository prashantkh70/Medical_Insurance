print('This is calculation file')
student name =[]
def multiplication(a=10,b=20):
    print('We are in Multiplication Function')
    mul = a*b
    print(f'Multiplication of {a} and {b} is {mul}')
    return mul

def addition(a=100,b=200):
    print('We are in Addition Function')
    add = a+b
    print(f'Addition of {a} and {b} is {add}')
    return add

print('Value in __name__ variable in calculation file is: ',__name__)

if __name__ =='__main__':   #true >> __main__
    multiplication(20,30)
    addition(20,30)
    
