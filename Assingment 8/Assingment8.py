# program executes 4 algorithms with different time efficiencies (Selection, bubble
# merge and tree) and measures execution time as a function of input size.
import time
import random
import math

def selection_sort(a_list):
  for fill_slot in range(len(a_list) - 1, 0, -1):
     pos_of_max = 0
     for location in range(1, fill_slot + 1):
        if a_list[location] > a_list[pos_of_max]:
           pos_of_max = location
     temp = a_list[fill_slot]
     a_list[fill_slot] = a_list[pos_of_max]
     a_list[pos_of_max] = temp
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)



def main():
    list_sizes1 = [x for x in range(10000, 50001, 5000)]
    exec_times_select = []
    exec_times_bubble = []
    exec_merge = []
    
    # run experiment to measure execution time as a function of 
    # input size.  
    for list_size in list_sizes1:
        # create list of random ints of size list_size
        numbers = random.sample(range(1,1000000), list_size)
        # start the clock
        start = time.time()
        # perform some operation on each list element
        for num in numbers:
            result = math.sqrt(num) * math.sqrt(num)
        # stop the clock
        end = time.time()
        # save the execution time
        .append(end-start)
    
    print("\n\n\tExecution Time (s)")
    print("Input size \tSelection \tBubble \tMerge \tTree")
    for i in range(len(list_sizes1)):
         print("%d \t\t %.5f" % (list_sizes1[i], exec_times_linear[i]))
    
   

if __name__ == "__main__":
    main()
