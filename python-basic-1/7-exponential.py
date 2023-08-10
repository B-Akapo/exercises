# Description: A program that accepts an integer (n) and computes the value of n+nn+nnn.
def main():
    n = int(input("Please enter the value of n: "))
    answer = exponential(n)
    print(answer)

def exponential(n):
    nn = int(str(n) + str(n))
    nnn = int(str(n) + str(n) + str(n))
    result = n + nn + nnn
    return result

if __name__ == "__main__":
    main()

