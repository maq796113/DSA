import random
def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)): # from 1 to n-1
        cur = A[k] # current element to be inserted
        j=k # find correct index j for current
        while j > 0 and A[j-1] > cur: # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur # cur is now in the right place
    return A
x = [2,4,1,64,93,0,3,-1,34,5,9,6,8,10]
print("Original List:",x)
print("Usinging Insertion Sort:",insertion_sort(x))


import math 
def merge(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2 inc] into result."""
    end1 = start+inc # boundary for run 1
    end2 = min(start+2*inc, len(src)) # boundary for run 2
    x, y, z = start, start+inc, start # index into run 1, run 2, result
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x];x += 1 # copy from run 1 and increment x
        else:
            result[z] = src[y];y += 1 # copy from run 2 and increment y
        z += 1 # increment z to reflect new result
    if x < end1:
        result[z:end2] = src[x:end1] # copy remainder of run 1 to output
    elif y < end2:
        result[z:end2] = src[y:end2] # copy remainder of run 2 to output

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    logn = math.ceil(math.log(n,2))
    src, dest = S, [None]*n # make temporary storage for dest
    for i in (2**k for k in range(logn)): # pass i creates all runs of length 2i
        for j in range(0, n, 2*i): # each pass merges two length i runs
            merge(src, dest, j, i)
        src, dest = dest, src # reverse roles of lists
    if S is not src:
        S[0:n] = src[0:n] # additional copy to get results to S
    return S
print("Using bottom-up MergeSort:",merge_sort(x))


def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: return #range is trivially sorted
    pivot = S[b] # last element of range is pivot
    left = a #will scan rightward
    right = b-1 #will scan leftward
    while left <= right:
        #scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        #scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right: # scans did not strictly cross
            S[left], S[right] = S[right], S[left] # swap values
            left, right = left + 1, right-1 # shrink range

    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left + 1, b)
    return S

print("Using Inplace Quick Sort",inplace_quick_sort([1,5,22,5,55,2,6],2,5))

print("-"*5+"Task 4"+"-"*5)
y=random.randint(11, 80)
lst= []
for i in range(5, y, 3):
    lst.append(random.randrange(10, 80))
print("Original List:",lst)
if len(lst)<50:
    print("Using Insertion Sort:", insertion_sort(lst))
else:
    print("Using bottom-up MergeSort:", merge_sort(lst))




class LinkedQueue:
    # FIFO queue implementation using a singly linked list for storage.

    class _Node:

        _slots_ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node’s fields
            self._element = element  # reference to user’s element
            self._next = next

    def init(self):

        self._head = None
        self._tail = None
        self._size = 0  # number of queue elements

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def first(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element  # front aligned with head of list

    def dequeue(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had been the tail
        return answer

    def enqueue(self, e):

        newest = self._Node(e, None)  # node will be new tail node
        if self.is_empty():
            self._head = newest  # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest  # update reference to tail node
        self._size += 1

def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return # list is already sorted
    # divide
    p = S.first() # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty(): # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else: #S.first() must equal pivot
            E.enqueue(S.dequeue())
    #conquer (with recursion)
    quick_sort(L) # sort elements less than p
    quick_sort(G) # sort elements greater than p
    #concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

print("-"*5+"Task 5"+"-"*5)

lst2 = []
z=random.randint(11, 80)
for i in range(5, z, 3):
    lst2.append(random.randrange(10, 80))
print("Original List:", lst2)
if len(lst)<50:
    print("Using Insertion Sort:", insertion_sort(lst2))
else:
    print("Using Quicksort:", merge_sort(lst2))

print("-"*5+"Task 6"+"-"*5)



randlist = []
for i in range(0,1000):
    n = random.randint(1,30)
    randlist.append(n)


import time

start = time.time()
insertion_sort(randlist)

end = time.time()
print("Time Elapsed (Task 1):", end - start)


start1 = time.time()
merge_sort(randlist)

end1 = time.time()
print("Time Elapsed (Task 2):", end1 - start1)

start2 = time.time()
inplace_quick_sort(randlist, 2, 800)

end2 = time.time()
print("Time Elapsed (Task 3):", end2 - start2)

start3 = time.time()
if len(randlist)<50:
    insertion_sort(randlist)
else:
    merge_sort(randlist)

end3 = time.time()
print("Time Elapsed (Task 4):", end3 - start3)

start4 = time.time()
if len(randlist)<50:
    insertion_sort(randlist)
else:
    merge_sort(randlist)

end4 = time.time()
print("Time Elapsed (Task 5):", end4 - start4)