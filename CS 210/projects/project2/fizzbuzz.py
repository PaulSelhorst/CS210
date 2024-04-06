def fb(n):
    if n % 15 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)
def fbloop(n):
    for i in range(1, n + 1):
        print(fb(i))
    print("Game over!")
    

fbloop(15)