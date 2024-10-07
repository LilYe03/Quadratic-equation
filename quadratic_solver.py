import cmath  # For handling complex numbers

def solve_quadratic(a, b, c):
    # Case 1: Handle linear equation when a = 0
    if a == 0:
        if b != 0:
            root = -c / b
            print(f"Since a = 0, it's a linear equation. The solution is: x = {root}")
        else:
            if c == 0:
                print("The equation is indeterminate (0 = 0).")
            else:
                print("No solution exists for this equation.")
        return

    # Case 2: Calculate discriminant for quadratic equation
    discriminant = b**2 - 4*a*c

    # Case 3: Check if roots are real or imaginary
    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print(f"The roots are real and different: x1 = {root1.real}, x2 = {root2.real}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The roots are real and identical: x1 = x2 = {root}")
    else:
        # Roots are complex (imaginary)
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print(f"The roots are imaginary: x1 = {root1}, x2 = {root2}")

# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

solve_quadratic(a, b, c)
