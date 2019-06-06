def count_down(n):
    if n == 0:
        print("0")
    else:
        count_down(n-1)
        print(n)
        

count_down(5)


def backwards_alphabet(curr_letter):
    if curr_letter ==  'a':
        print(curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = 'f'


backwards_alphabet(starting_letter)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

n = input(i
