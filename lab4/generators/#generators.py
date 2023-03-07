#generators
n = int(input("give the n number:"))

a = [i for i in range(1,n+1)]

for num in a:
    print(num*num)

#2
def check_to_even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i


n = int(input())
for num in check_to_even(n):
    print(num, end =',')
print('\n')
a = [i for i in range(n+1)]

for num in a:
    if num % 2 == 0:
        print(num, end =',')


#3
def lol(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in lol(n):
    print(num, end =' ')

#4
def squares(a,b):
    for i in range(a, b+1):
        yield i*i

a = int(input())
b = int(input())
for i in squares(a,b):
    print(i)

#5
n = int(input())
a = [i for i in range(n,-1,-1)]

for i in a:
    print(i)