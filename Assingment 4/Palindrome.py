class Stack(object):  # created stack object
    def __init__(self,items):     #created my empty stack list
        self.items=[]
        for e in items:
            self.push(e)

    def push(self,item):     # append the items 
        self.items.append(item)

    def pop(self):          # pop them to bring them foward and remove
        return self.items.pop()

    def __repr__(self):
        return str(self.items)  

    def isPalindrome(self):      # isPalindrome is a function i created to determine
        tr=Stack([])             # if the user input in the main function is True or False
        t=Stack(self.items)
        while t.items:
            tr.push(t.pop())
        t=Stack(self.items)    
        while t.items and tr.items:
            c1=t.pop()
            c2=tr.pop()
            print(c1,c2)
            if c1!=c2: return False
        return True    

def main():           # main function for user input 
    a = input("Enter a string: ")
    s = Stack(a)
    print(s.isPalindrome())


main()      # called my main function 
