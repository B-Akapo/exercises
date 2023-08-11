# Description: A program that creates a histogram from a given list of integers

"""
The code snippet is a standalone program that creates a histogram from a given list of integers. It starts by defining a `main` function, which is the entry point of the program. Inside the `main` function, a list of numbers `[2, 3, 6, 5]` is created and assigned to the variable `histogram_list`. Then, the `create_histogram` function is called with `histogram_list` as an argument.

The `create_histogram` function takes a list of numbers as input and iterates over each number using a `for` loop. For each number, it prints a line of '#' characters equal to the value of the number. This creates a visual representation of the numbers as a histogram.

Finally, the program checks if the `__name__` variable is equal to `"__main__"`, which indicates that the script is being run directly and not imported as a module. If this condition is true, the `main` function is called, executing the program.
"""

def main():
    histogram_list = [2, 3, 6, 5]
    create_histogram(histogram_list)

def create_histogram(numbers):
    for num in numbers:
        print("#" * num)

if __name__ == "__main__":
    main()
