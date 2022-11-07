# iterative
for i in range(3):
    x = i
    print(x+x*i)

# Recurssion
def factorial(x):
    if x == 1:
        return x

    return (x * factorial(x-1))

num = 4

print("The factorial of", num, "is", factorial(num))