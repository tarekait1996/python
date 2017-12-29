import random
#problem 1
def gensquares(N):
    for number in range(N):
        yield number**2

for x in gensquares(10):
    print(x)
print()
#problem 2
def rand_num(low,high,n):
    for _ in range(n):
        yield random.randint(low,high)
for num in rand_num(1,10,12):
    print(num)
#problem 3
s = 'hello'

s_iter = iter(s)
print(next(s_iter))

#problem 4

'''
Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator. 

'''