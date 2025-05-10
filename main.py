import sys
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

    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return (2, min(x1,x2), max(x1,x2))
    elif delta == 0:
        x1 = -b / (2*a)
        return (1, x1)
    else:
        return (0,)

def print_results(a, b, c, solution):
    a_f = float(a)
    b_f = float(b)
    c_f = float(c)

    print(f"Equation is: ({a_f:.1f}) x^2 + ({b_f:.1f}) x + ({c_f:.1f}) = 0")

    num_roots = solution[0]

    if num_roots == float('inf'):
        print("Infinite solutions (identity equation).")
    elif num_roots == 0:
        print("There are 0 roots")
    elif num_roots == 1:
        print("There are 1 roots")
        print(f"x1 = {solution[1]:.1f}")
    elif num_roots == 2:
        print("There are 2 roots")
        print(f"x1 = {solution[1]:.1f}")
        print(f"x2 = {solution[2]:.1f}")

def get_valid_float_input(prompt_message, is_coefficient_a=False):
    while True:
        try:
            user_input_str = input(prompt_message).strip()
            value = float(user_input_str)
            if is_coefficient_a and value == 0:
                print("Error. Coefficient 'a' cannot be zero for a quadratic equation.")
                continue
            return value
        except ValueError:
            print(f"Error. Expected a valid real number, got {user_input_str} instead")

def interactive_mode():
    print("Starting interactive mode for quadratic equation solver.")
    
    a = get_valid_float_input("a = ", is_coefficient_a=True)
    b = get_valid_float_input("b = ")
    c = get_valid_float_input("c = ")

    solution = solve_quadratic(a, b, c)
    print_results(a, b, c, solution)

def file_mode(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
            if not lines:
                sys.stderr.write(f"Error: File '{filename}' is empty.\n")
                sys.exit(1)

            coeffs_str = []
            raw_coeffs_str = []

            potential_coeffs = []
            for line in lines:
                potential_coeffs.extend(line.strip().split())
                if len(potential_coeffs) >= 3:
                    break
            
            if len(potential_coeffs) < 3:
                sys.stderr.write(f"Error: File '{filename}' does not contain enough coefficients. Expected 3, got {len(potential_coeffs)}.\n")
                sys.exit(1)

            coeffs_str = potential_coeffs[:3]

            try:
                a = float(coeffs_str[0])
                b = float(coeffs_str[1])
                c = float(coeffs_str[2])
            except ValueError as e:
                sys.stderr.write(f"Error: Invalid number format in file '{filename}'. Could not convert '{e.args[0].split(': ')[-1]}' to float.\n")
                sys.exit(1)
            except IndexError:
                sys.stderr.write(f"Error: Not enough coefficients found in file '{filename}'.\n")
                sys.exit(1)

            if a == 0:
                sys.stderr.write(f"Error: Coefficient 'a' cannot be zero for a quadratic equation. Found a=0 in file '{filename}'.\n")
                sys.exit(1)

            solution = solve_quadratic(a, b, c)
            print_results(a, b, c, solution)

    except FileNotFoundError:
        sys.stderr.write(f"Error: File '{filename}' not found.\n")
        sys.exit(1)
    except IOError:
        sys.stderr.write(f"Error: Could not read file '{filename}'.\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")
        sys.exit(1)

def main():
    args = sys.argv
    if len(args) == 1:
        interactive_mode()
    elif len(args) == 2:
        file_mode(args[1])
    else:
        sys.stderr.write("Usage:\n")
        sys.stderr.write(f"  Interactive mode: {args[0]}\n")
        sys.stderr.write(f"  File mode:        {args[0]} <filepath>\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
