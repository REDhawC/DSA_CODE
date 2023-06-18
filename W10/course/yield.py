def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


for fn in fib():
    print(fn)
    if fn > 100000:
        break
