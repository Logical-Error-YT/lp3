# Gradient Descent for y = (x + 3)^2, starting at x = 2
def f(x):
    return (x + 3) ** 2

def derivative(x):
    return 2 * (x + 3)

x = 2.0
learning_rate = 0.1
iterations = 100

for i in range(iterations):
    x = x - learning_rate * derivative(x)

print("Local minimum x =", round(x, 6))
print("Minimum y =", round(f(x), 6))
