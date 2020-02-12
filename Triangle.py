
def classify_triangle(a,b,c):
    """Check the triangle"""

    if a == b == c:
        return 'Equilateral Triangle'

    elif a == b or a == c or b == c:
        return "Isosceles Triangle"

    elif a*a + b*b  == c*c:
        return "Right Angled Triangle"

    elif a != b or b != c:
        return "Scalene Triangle"

def main():
    a = int(input("Enter the length of side 1 : "))
    b = int(input("Enter the length of side 2 : "))
    c = int(input("Enter the length of side 3 : "))

if __name__ == '__main__':
    main()
