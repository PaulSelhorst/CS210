# Pizza calculator example code
import math
import doctest
def pizza_CPSI(diameter, cost):
    '''
    (int, num) -> float
    Calculates and returns the cost per square inch,
    given the diameter and cost of a pizza.
    Examples:
    >>> pizza_CPSI(14, 18)
    0.117
    >>> pizza_CPSI(14, 20.25)
    0.132
    '''

    cost_per_inch = cost / circle_area(diameter)
    cost_per_inch = round(cost_per_inch, 3)
    return cost_per_inch

def circle_area(diameter):
    '''
    (num) -> float
    Calculates and returns the area of a circle,
    given the radius.
    Examples:
    >>> circle_area(1)
    0.7853981633974483
    >>> circle_area(2)
    3.141592653589793
    '''
    radius = diameter / 2
    area = math.pi * radius**2
    area = area
    return area

#print(doctest.testmod())
print(circle_area(1))
print(circle_area(2))