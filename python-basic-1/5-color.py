# Description: A program that displays the first and last colors from a list

def main():
    color_list = ["Red", "Green", "White", "Black"]
    if not color_list:
        print("The color list is empty.")
    else:
        first = first_color(color_list)
        last = last_color(color_list)
        print("First color:", first)
        print("Last color:", last)

def first_color(color_list):
    if not color_list:
        return None
    return color_list[0].lower()

def last_color(color_list):
    if not color_list:
        return None
    return color_list[-1].lower()

if __name__ == "__main__":
    main()
