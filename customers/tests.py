from django.test import TestCase

# Create your tests here.
def fun(x, y):
    total = x+y
    if x:
        return x
    return total

t = fun(5,6)  #11
print("t is ", t)
