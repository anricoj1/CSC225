from random import randint

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
            self.data = newdata
            
    def set_next(self, new_next):
            self.next = new_next    
            
class UnorderedList:
    def __init__(self):
        self.head = None    
 
    def is_empty(self):
        return self.head == None 
 
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
   
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self,item):
        current = self.head
        found = False
       
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
           
        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def get_list(self):
        current = self.head
        count = 0
        array = []

        while current != None and count < self.size():
            array.append(current.get_data())

            current = current.get_next()
            count = count + 1
    
        return array
            
    def replace_element(self,position,newValue):
        current = self.head
        count = 0

        while current != None and count < self.size():
            if count == position:
                current.data = newValue

            current = current.get_next()
            count = count + 1

    def sort(self):
        array = self.get_list()
        for a in range(0,len(array)):
            for b in range(0,len(array)):
                if array[a] < array[b]:
                    temp = array[a]
                    array[a] = array[b]
                    array[b] = temp

        self.head.data = None
        self.head.next = None
        self.remove(None)
        
        for j in reversed(range(len(array))):
            self.add(array[j])
           
    '''
    function that returns the index
    of an item that is inputted
    '''
    def index(self,item):
        current = self.head
        found = False
        count = 0
       
        while current != None and not found:
            # if item has a match break loop and return the index
            if current.get_data() == item:
                return count
                found = True
            # no match? continue cycle
            else:
                current = current.get_next()
                count = count + 1
    '''
    function that deletes last element in the list
    if a position parameter is inputted it
    deletes the element at that position
    '''
    def pop(self,pos=None):
        # if there is no position param
        if pos == None:
            listContents = self.get_list()
            self.remove(listContents[len(listContents)-1])
            return listContents[len(listContents)-1]

        # if there is a position param
        else:
            #remove list item at inputted index
            listContents = self.get_list()
            self.remove(listContents[pos])
            return listContents[pos]

    '''
    returns number of occurrences of an
    inputted item in the list
    '''
    def num_of_occurrences(self,item):
        current = self.head
        count = 0
        occurrence = 0
        
        while current != None and count < self.size():
            # occurrence found increment sightings by 1
            if current.get_data() == item:
                occurrence = occurrence + 1
            
            current = current.get_next()
            count = count + 1

        # return number of item sightings
        return occurrence

    '''
    removes all replica values in the list
    '''
    def delete_replicas(self):
        array = self.get_list()
        newArray = []
        
        for a in array:
            # if element is unique add to array
            if a not in newArray:
               newArray.append(a)
            # if it exists in array remove form list
            else:
                self.remove(a)
        
 
def main():
    #linked list instance
    aList = UnorderedList()

    # generating 15 integers between 1 and 5
    # adding those numbers to linked list
    for i in range(0,15):
        aList.add(randint(1,5))
        aList.sort()

    # display generated linked list items
    print('\n%s'% aList.get_list())

    # pop method
    print('\nThe element "%s" was popped at end of list' % aList.pop())

    # pop method method at index
    index = 5
    print('\nThe element "%s" was popped at the index %s' % (aList.pop(index), index))
    
    # testing index method
    num = 3
    print('\nIndex of "%s" is: %s '%(num,aList.index(num)))
    
    # display generated linked list items
    print('\n%s'%aList.get_list())

    # display number occurrences of each element
    print("\nOccurrences")
    items = aList.get_list()
    exists = []
    for item in items:
        if item not in exists:
            exists.append(item)
            print('%s has %s occurrences.'%(item,aList.num_of_occurrences(item)))
            
    # removing replicas
    print("\nRemoving replicas")
    aList.delete_replicas()
    
    # display generated linked list items
    print('\n%s' % aList.get_list())
        
if __name__ == "__main__":
    main()
