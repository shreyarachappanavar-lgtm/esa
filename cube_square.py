import sys
def cube_square(num):
    square = num ** 2
    cube = num ** 3
    return square, cube

if __name__ == "__main__":
    sys.argv(cube_square)
    num = int(input("Enter a number: "))
    square, cube = cube_square(num)
    print("Square:", square)
    print("Cube:", cube)

