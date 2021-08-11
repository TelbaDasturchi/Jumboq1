import random
n = 10000000
numbers = list(range(1, n+1))
x = numbers.pop(random.randint(1,n))
print(x)
i = 1
# for num in numbers:
#     if i!=num:
#         break
#     i += 1
# print(i)
print(n*(n+1)/2-sum(numbers))
