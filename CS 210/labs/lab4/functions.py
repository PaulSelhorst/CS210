def hello(first_name):
    '''
    Function that prints "Hello, " + first_name + "!"
    Input: first_name (string)
    Output: None
    '''
    print("Hello, " + first_name + "!")
    return None

def ciao(first_name):
    '''
    Function that prints "Ciao, " + first_name + "!"
    Input: first_name (string)
    Output: None
    '''
    print("Ciao, " + first_name + "!")
    return None

def greeting(f, s):
    print(f"Calling {f.__name__}")
    f(s)

def add_3(a, b, c):
    return a + b + c
def mult_3(a, b, c):
    return a * b * c

def higher_order(f, a, b, c):
    print(f"Function: {f.__name__}")
    print(f"{f.__name__} ({a}, {b}, {c}) = {f(a, b, c)}")
    print (f(a, b, c))

higher_order(add_3, 1, 2, 3)

