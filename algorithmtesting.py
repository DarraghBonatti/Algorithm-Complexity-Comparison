import time 
from random import randint
import random
import copy
import sys
sys.setrecursionlimit(100000)






################# mergesort ########################

def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

################# heap sort #########################
def heapsort(inlist):
    
    length = len(inlist)
    for i in range(length):
        bubbleup(inlist,i)
     
    length = len(inlist)
    for i in range(length):
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist,0, length-2-i)
def bubbleup(inlist, i):
   
    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            # print('swapping:', inlist[i], 'with its parent:', inlist[parent])
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0
def bubbledown(inlist, i, last):
   
    while last > (i*2):  #so at least one child
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc   # start by assuming left child is the max child
        if last > lc and inlist[rc] > inlist[lc]:  #rc exists and is bigger
            maxc = rc
        if inlist[i] < inlist[maxc]:
            # print('swapping:', inlist[i], 'with its child:', inlist[maxc])
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last






################ Insertion Sort #####################
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# def insertionsort(mylist):
#     n = len(mylist)
#     i = 1
#     while i < n:
#         j = i-1
#         while mylist[i] < mylist[j] and j > -1:
#             j -= 1
#         #insert i in the cell after j
#         temp = mylist[i]
#         k = i-1
#         while k > j:
#             mylist[k+1] = mylist[k]
#             k -= 1
#         mylist[k+1] = temp
#         i += 1


################  Quick Sort Hoare Partition #########################
def quicksort(mylist):
    n = len(mylist)-1
    quick_sort(mylist, 0, n)


def quick_sort(inlist, first, last):
    if first < last:
        pivot = hoare_partition(inlist, first, last)
        quick_sort(inlist, first, pivot)
        quick_sort(inlist, pivot + 1, last)

def hoare_partition(list, first, last):
    pivot = list[first]
    i = first - 1
    j = last + 1
    while True:
        i += 1
        while list[i] < pivot:
            i += 1

        j -= 1
        while list[j] > pivot:
            j -= 1

        if i >= j:
            return j

        list[i], list[j] = list[j], list[i]



############## Quick Sort Hoare Partition Shuffled ##################
def quicksortshuffle(mylist):
    n = len(mylist)-1
    random.shuffle(mylist)
    quick_sortshuffle(mylist, 0, n)


def quick_sortshuffle(inlist, first, last):
    if first < last:
        pivot = hoare_partition(inlist, first, last)
        quick_sortshuffle(inlist, first, pivot)
        quick_sortshuffle(inlist, pivot + 1, last)

def hoare_partition(list, first, last):
    pivot = list[first]
    i = first - 1
    j = last + 1
    while True:
        i += 1
        while list[i] < pivot:
            i += 1

        j -= 1
        while list[j] > pivot:
            j -= 1

        if i >= j:
            return j

        list[i], list[j] = list[j], list[i]


########### Algorithm Testing Function#############
def testonealg(inlist, f):
    start_time = time.perf_counter()
    f(inlist)
    end_time = time.perf_counter()
    checksorted(inlist, f)
    return end_time - start_time

############ Part 1 #######################
def checksorted(list , f):
    
    index = 0
    #for i in range(len(list) - 1):
    while index < len(list)-1:
        if list[index] > list[index + 1]:
            print ( "This List is Not Sorted. Algorithm name:",f.__name__)
            break
        else:
            index +=1

############# Part 2 ################

def randomlist(n,k): #n = length of list, k = number of duplicate entries, n - k = number of distinct entries
    list = []
    for i in range(1, n-k+1):
        list.append(i)


    for x in range(k):
        x = list[randint(0,n-k-1)]
        list.append(x)

    random.shuffle(list)
    
    return list
    



############## Part 3 ###############

def evaluate(n, k, num, f):
    mylists = []
    for i in range(num):
        i = randomlist(n,k)
        mylists.append(i)

    sum = 0
    
    # for i in range(len(mylists)-1):
    # for i in range(num):
    for i in mylists:
    
        times = testonealg(i,f)
        sum += times
    
    print(f"Algorithm:",f.__name__," has an average time of:", sum/num)


################ Part 4 ##################

def evaluateall(n,k,num,funcs):
    lists = []
    for i in range(num):
        j = randomlist(n,k)
        lists.append(j)


    # summ = 0
    for function in funcs:
        summ = 0
        for list in lists:
            list_copy = copy.copy(list)
            average = testonealg(list_copy, function) 
            summ += average
        
        print(f"Average Time Taken for", function.__name__,"was:",summ/num )




################# Part 6######################
def evaluateallpartial(n,k,num,funcs):

    #### makes num number of random lists with lenght n and k copies ####
    lists = []
    for i in range(num):      
        j = randomlist(n,k)     
        lists.append(j)
    #### python sorts the lists ####
    for i in lists:
        i.sort()
    #### swap 2 random elements in each list ####
    for i in lists:
        swap1 = randint(0,len(i)-1)
        swap2 = randint(0,len(i)-1)

        i[swap2] , i[swap1] = i[swap1] , i[swap2]
    #### copies the lists x amount of times where x is the number of functions being passed in ####
    for function in funcs:
        summ = 0
        for list in lists:
            list_copy = copy.copy(list)
            average = testonealg(list_copy, function) 
            summ += average
        
        print(f"Average Time Taken for", function.__name__,"was:",summ/num )

 

# print(evalautescale())


def evaluateall50(n,k,num,funcs):

    #### makes num number of random lists with lenght n and k copies ####
    lists = []
    for i in range(num):      
        j = randomlist(n,k)     
        lists.append(j)
    #### python sorts the lists ####
    for i in lists:
        i.sort()
    #### swap 2 random elements in each list ####


    for i in range(n//2):
        for j in lists:
            swap1 = randint(0,len(j)-1)
            swap2 = randint(0,len(j)-1)

            j[swap2] , j[swap1] = j[swap1] , j[swap2]


    #### copies the lists x amount of times where x is the number of functions being passed in ####
    
    for function in funcs:
        summ = 0
        for list in lists:
            list_copy = copy.copy(list)
            average = testonealg(list_copy, function) 
            summ += average
        
        print(f"Average Time Taken for", function.__name__,"was:",summ/num )


    
    
    


############## Part 5 ###################
def evalautescale():
    parameters = [
                #(100, 10),
                #(1000, 100),
                #(10000, 1000),
                #(100000, 10000),
                #(1000000, 100000)
                
                
                  
                  
                  ]
    functions = [insertion_sort]
    #functions = [ quicksort, mergeSort, heapsort]
    for (n,k) in parameters:
        evaluateallpartial(n,k,20,functions)

