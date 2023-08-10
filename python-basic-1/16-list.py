# Description: A program that counts the number 4 in a given list. 

def main():
    num_list = [1, 2, 4, 19, 4, 23, 4, 3]
    answer = count_fours_in_list(num_list)
    print(answer)

def count_fours_in_list(num_list):
    counter = 0
    for num in num_list:
        if num == 4:
            counter += 1
    return counter

if __name__ == "__main__":
    main()
