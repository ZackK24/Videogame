def recursive(x):
    if x > 13:
        return x * 2
    else:
        print(x)
        return x * recursive(x+1)
print(recursive(1))