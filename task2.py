# 1.Create a simple function that takes 2 numbers and print their values
x =input('enter num1 : ')
y =input('enter num2 : ')

def func(x,y):
    print('the first value:',int(x))
    print('the second value:',int(y))

func(x,y)

print('\n -----------------')
#2.In the above return function,use keyword arguments when calling the function


func(x=2,y=5)

print('\n -----------------')
'''3.In the above return function , give x and y default values of 0 and call the
function with no arguments'''

def func(x =0,y =0):
    print('the first value:',int(x))
    print('the second value:',int(y))

func()


print('\n -----------------')

#5.Create the same sum function using the lambda
myadd = lambda x,y: x+y

print(myadd(int(x),int(y)))

print('\n -----------------')

#6.Call the lambda function at the same definition line

z=(lambda x,y : x+y )(int(x),int(y))
print(z)
