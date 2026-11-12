# Recursive and iterative Fibonacci; time and space complexity
def fib_rec(n):
    return n if n < 2 else fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(input("n: "))
print("Recursive:", fib_rec(n))
print("Non-recursive:", fib_iter(n))
print("Recursive: Time O(2^n), Space O(n)")
print("Iterative: Time O(n), Space O(1)")
