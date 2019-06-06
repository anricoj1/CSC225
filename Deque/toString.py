def to_str(n, base):
    convert_string = input("Enter a number: ")
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]

print(to_str(10, 2))
