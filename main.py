import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return (float('inf'),)
            else:
                return (0,)
        else:
            return (1, -c / b)

    delta = b**2 - 4 * a * c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return (2, min(x1, x2), max(x1, x2))
    elif delta == 0:
        x1 = -b / (2 * a)
        return (1, x1)
    else:
        return (0,)

def print_solution(a, b, c, solution):
    print(f"Equation: ({a:.1f})x^2 + ({b:.1f})x + ({c:.1f}) = 0")

    num_roots = solution[0]

    if num_roots == float('inf'):
        print("Infinite solutions (all real numbers are roots).")
    elif num_roots == 0:
        print("No real roots.")
    elif num_roots == 1:
        print(f"One real root: x = {solution[1]:.1f}")
    elif num_roots == 2:
        print(f"Two real roots: x₁ = {solution[1]:.1f}, x₂ = {solution[2]:.1f}")

a, b, c = 1, -5, 6
solution = solve_quadratic(a, b, c)
print_solution(a, b, c, solution)