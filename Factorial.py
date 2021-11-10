

def factorial(number):
    if number==1:
        return 1
    return number * factorial(number - 1)
# print(factorial(5))
index=1
while(index<5):
    print(factorial(index),end=" ")
    index+=1   
