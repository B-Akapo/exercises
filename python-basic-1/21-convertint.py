# Description: A program that concatenates all elements in a list into a string and returns it

def main():
    my_list = [1, 5, 12, 2]
    result = concatenate(my_list)
    print(result)

def concatenate(numbers):
    my_string = ""
    for num in numbers:
        my_string += str(num)
    return my_string
    
if __name__ == "__main__":
    main()
