# Description: A program that creates a histogram from a given list of integers

def main():
    histogram_list = [2, 3, 6, 5]
    create_histogram(histogram_list)

def create_histogram(numbers):
    for num in numbers:
        print("#" * num)

if __name__ == "__main__":
    main()
