# Python program to demonstrate implementation of queue using queue module 

from queue import Queue 

# Initializing a queue with maxsize 4 
q = Queue(maxsize = 4) 

# Add/enqueue elements to queue 
q.put('a') 
q.put('b') 
q.put('c') 
q.put('d')

# Return Boolean for Full Queue 
print("\nFull: ", q.full()) 

# Remove/dequeue elements from queue 
print("\nElements dequeued from the queue") 
print(q.get()) 
print(q.get()) 
print(q.get()) 

# Return Boolean for Empty Queue 
print("\nEmpty: ", q.empty()) 
print("\nQueue size:", q.qsize()) #prints size of the queue


