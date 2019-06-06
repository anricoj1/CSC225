import Deque

def arrange(aList):
    arranged = []

    d = Deque.Deque()

    for item in aList:
        if item < 0:
            d.add_rear(item)
        else:
            d.add_front(item)

    while not d.is_empty():
        arranged.append(d.remove_rear())

    return arranged
print(arrange([-3,12,6,-7]))

    
arrange()
