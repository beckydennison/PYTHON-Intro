#4x(1-1/3+1/5-1/7+1/9-1/11)

def pi_approx(num_iterations):
    k = 3.0
    s = 1.0

    for i in range(num_iterations):
        s = s-((1/k) * (-1)**i)
        k += 2

    return 4 * s
print(pi_approx(6))

print(pi_approx(8))

