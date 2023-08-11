# Description: A program that prints all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence. 

def main():
    num_list = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
    check_list(num_list)

def check_list(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)
        elif num == 237:
            print(num)
            break

if __name__ == "__main__":
    main()