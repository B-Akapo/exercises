# Description: A program that will accept the base and height of a triangle and compute its area. 

def main():
    try:
        base = int(input("Please enter the value of the base: "))
        height = int(input("Please enter the value of the height: "))
        
        if input_validation(base, height):
            answer = triangle_area(base, height)
            print(answer)
        else:
            print("Invalid input, please enter positive values for base and height.")
    except ValueError:
        print("Invalid input, please enter valid integer values for base and height.")

def input_validation(base, height):
    if base < 0 or height < 0:
        return False
    return True

def triangle_area(base, height):
    area = 0.5 * base * height
    return area        

if __name__ == "__main__":
    main()
