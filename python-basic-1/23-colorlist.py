# Description - A program that prints out all colors from color_list_1 that are not present in color_list_2. 

def main():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    result = compare_list(color_list_1, color_list_2)
    print(result)

def compare_list(list1, list2):
    unique_colors = list1 - list2
    return list(unique_colors)

if __name__ == "__main__":
    main()