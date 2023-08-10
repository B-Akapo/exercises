# Description: A program that accepts a filename from the user and prints the extension of the file. 

def main():
    filename = input("Please enter a file name with the extension: ")
    filename = filename.lower()
    file_extention = check_extention(filename)
    print(file_extention)

def check_extention(filename):
    if filename.endswith(".java"):
        return "This is a java document"
    elif filename.endswith(".jpeg"):
        return "This is jpeg document"
    else:
        return "enter a file name with its extension"

if __name__ == "__main__":
    main()