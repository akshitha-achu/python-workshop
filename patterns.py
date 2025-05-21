def left_and_right_triangles(n):
    for i in range(1, n + 1):
        left = "*" * i                   
        right = "*" * i                 
        print(left.ljust(n) + " " + right.rjust(n))

left_and_right_triangles(5)
print("\n")



def l_shape_triangle(height, width):
    for i in range(height - 1):
        print("*")
    print("*" * width)

l_shape_triangle(height=5, width=5)
print("\n")

def inverted_full_pyramid(n):
    for i in range(n, 0,-1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print()
inverted_full_pyramid(5)
print("\n")


def full_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print()
full_pyramid(5)
print("\n")



