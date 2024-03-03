def function (List_):
    return max(List_)

List_ = [1,2,3,4]
z = function(List_)
print (z)



def func(x=1,y=1,z=1):
    if x and y and z:
        return x * y * z
    elif x and y:
        return x * y
    return 3.14 * x

print(func(2,3,4))
print(func(3,4))
print(func(5))


def fun(x=0,y=0,z=0):
    d = 0
    if(x != 0 and y == 0 and z == 0):
        d= 22/7*x*x
    elif(x != 0 and y != 0 and z == 0):
        d= x*y
    elif (x != 0 and y != 0 and z != 0):
        d= x*y*z
    return d
    
    
x=10
y=20
z=30
print(fun(x))

def func2(a = 1, b = 1, c = 1):
    if(a != 1 and b != 1 and c != 1):
        return a * b * c
    elif(a != 1 and b != 1):
        return a * b
    
    return 22/7* a * a

print(func2(10, 20, 30))
print(func2(10, 20))
print(func2(10))


def Area(x , y =1 , z =-1):
    if (y == -1 and z == -1):
        return 3.14*x**2
    
    elif(z==-1):
        return x*z
    else:
        return x*y*z

print(Area(10))

def area_volume(x , *arg):
    if (len(arg) == 0):
        print("circle")
        print(arg)
        return (3.14*x**2)
    elif (len(arg) == 1):
        print("rectangle/square")
        print(arg)
        return (x*arg[0])

    elif (len(arg) == 2):
        print("cylinder")
        print(arg)
        return (x*arg[1]*arg[1])


print (area_volume(10))



def factorial_recursion(element):
    if (element >1):
        return element* (factorial_recursion(element-1))
    else:
        return 1
    
print(factorial_recursion(3))

# WHY recusion?


def print_table_3(i=1):
    if i == 11:
        return;
    print(3 * i)
    return print_table_3(i+1)
    
print_table_3()

def tableOf3(n):
    if(n == 0):
        return
    tableOf3(n-1)
    print(3 * n)

print(tableOf3(10))    


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


print("FIBONACCI SERIES \n\n\n\n")

def fibonacci_series(element ):
    print(element)
    if (element <= 1):
        return element
    else:
        return(fibonacci_series(element-1) + fibonacci_series(element-2))
    
print (fibonacci_series (5))

