def sort_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers

if __name__ == "__main__":
    print("Enter 3 numbers to sort:")
    x = int(input("First number: "))
    y = int(input("Second number: "))
    z = int(input("Third number: "))

    result = sort_numbers(x, y, z)
    print("Sorted numbers:", result)
