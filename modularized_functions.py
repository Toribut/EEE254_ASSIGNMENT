import math

def get_coefficients():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    return a, b, c

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def find_roots(a, b, discriminant):
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "real and different", root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return "real and equal", root, None
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return "complex", (real_part, imaginary_part), None

def display_roots(root_type, root1, root2):
    if root_type == "real and different":
        print("Roots are real and different.")
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif root_type == "real and equal":
        print("Roots are real and equal.")
        print("Root:", root1)
    else:
        print("Roots are complex.")
        print("Root 1:", root1[0], "+", root1[1], "i")
        print("Root 2:", root1[0], "-", root1[1], "i")

def main():
    a, b, c = get_coefficients()
    discriminant = calculate_discriminant(a, b, c)
    root_type, root1, root2 = find_roots(a, b, discriminant)
    display_roots(root_type, root1, root2)

if _name_ == "_main_":
    main()