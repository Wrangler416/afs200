#create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.

def func_compute(num):
 return lambda x : x * num
result = func_compute(2)
print("Double the number  =", result(30))

