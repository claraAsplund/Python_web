def plus(a=1,b=1):
    print(a+b)

plus(5,5) 
plus()

def minus(a = 1, b=1):
    print(a - b)

minus(10,4)
minus()


def division(a=1, b=1):
    print(a/b)


division(10,2)
division()

def multiple(a=1, b=1):
    print(a*b)

multiple(4,9)
multiple()



def power(a=1, b=1):
    print(a ** b)

power(2,3)
power()


"""
def say_hello(user_name="anonymous"):
    print("hello", user_name)

say_hello("nico")
say_hello()

def say_hello(user_name="anonymous"):
user_name=" " is a default parameter, so instead of casuing error 
when the parameter is empty, function get the data "anonymous", handling
empty argument case.
"""