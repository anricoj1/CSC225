# Assingment 7
# Jason Anrico
def reverseString(string): #reversed string fucntion
    if len(string) < 1:
        return string
    else:
        reverse = reverseString(string[1:]) + string[0]
        return reverse


def rec_string(string):  #recursive string function 
    if len(string) < 1:
        return string
    else:
        reverse = rec_string(string[1:]) + string[0]
        print(string[0:])
        return reverse

def main():  #main function
    print("==== This program reverses a string from a user input ====")
    userString = input("Enter a string to be reversed: ")  #i used an actual user input for this part i hope thats okay
    print(reverseString(userString))   # reverse string function call
    print('\n')   #i usually perfer to use inputs just so the program can be flexible for the user

    print("recursive function output of 'abcde'")
    rec_string('abcde')   #rec_string function call 
    print('\n')
    print("recursive function output of 'abc'")
    rec_string('abc')
        
if __name__ == "__main__":
    main()
