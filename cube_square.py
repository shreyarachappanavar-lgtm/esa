def cube_square(num):
    cube = num ** 3
    square = num ** 2
    return square, cube

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    square, cube = cube_square(num)
    print("Square:", square)
    print("Cube:", cube)

       