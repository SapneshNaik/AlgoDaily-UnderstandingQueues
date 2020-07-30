# Understanding Queues

**Queue** is a collection of items wherein the operations work in *FIFO - First In First Out* manner. The two primary operations associated with them are; *enqueue* and *dequeue*.

> **Lesson Objectives**
> At the end of this lesson, you will be able to:
> 1. Know what *Queue* as a data structure is and appreciate it's real-world use cases.
> 2. Learn how queues work and their operations.
> 3. Know and implement queues with two different approaches using python language.

I'm sure all of us have been in queues may be at billing counters, shopping centers, or cafes. The first person in the line is serviced first, then the second and so forth. 
Now, we have this concept in computer science as well. Take the example of a printer. Suppose we have a shared printer, and several jobs are to be printed at once. The printer maintains a print-queue internally and prints the jobs in the sequence of which came first.

![Example printer](https://github.com/SapneshNaik/AlgoDaily-UnderstandingQueues/blob/master/example%20printer.png)

Another instance where queues are extensively used is, in the operating system of our machines. An OS maintains several queues such as job queue, ready queue, device queue for each of the processes. If you're interested, refer to this [link](https://www.tutorialspoint.com/operating_system/os_process_scheduling.htm) to know more about them. 

I hope we've got a brief idea about queues. Let's go ahead and understand how they work!

## How do queues work?

Consider a pipe; naturally, it has two open ends. Imagine we have some elements in the pipe, and we're trying to get them out. There will be one end through which we have inserted the elements, and there's another end from which we're getting them out. Like we can see in the figure below, which is precisely how the queue data structure works!

![Queue Illustration](https://github.com/SapneshNaik/AlgoDaily-UnderstandingQueues/blob/master/Queue%20Illustration.png)

Unlike the stack with one open end, the queue has two open ends; *front* and *rear*. With **rear** being the point of insertion and **front** that of removal. However, internally, the front and rear are treated as pointers. We'll learn them in the subsequent section programmatically.

> Note that the element that got inside first is the first one to be serviced and removed from the queue. Hence the name: First In First Out (FIFO).

## Queue operations and Implementation of queues using python
Like a stack has push and pop operations, a queue has **two** operations :
1. Enqueue: To add elements 
2. Dequeue: To remove elements.

> Click here to check out our lesson on [Stacks](https://algodaily.com/lessons/the-gentle-guide-to-stacks)!

### 1. Enqueue
Enqueue, as said earlier, is adding elements to your queue from the *rear* end. Initially, when the queue is empty, both our *front* and *rear* pointers are `NULL`.

![Step one](https://github.com/SapneshNaik/AlgoDaily-UnderstandingQueues/blob/master/step1.png)

Now, we add an element say, 'a' to the queue. Both our *front* and *rear* now point to 'a.'

![Step two](https://github.com/SapneshNaik/AlgoDaily-UnderstandingQueues/blob/master/step2.png)

Let's add another element to our queue say, 'b.' Now, our *front* pointer remains the same, whereas the *rear* pointer points to 'b.' We'll add another item 'c' and you'll see that elements are added at the *rear* end.

![Step 3 and so on](https://github.com/SapneshNaik/AlgoDaily-UnderstandingQueues/blob/master/step3step4.png)

### 2. Dequeue
Dequeue means to remove/delete elements from the queue; this happens from the front end of the queue. A particular element is removed from a queue after it is being serviced. We cannot delete an empty queue, and we require at least one element to be present in the queue when we want to dequeue. The following figure explains the dequeuing of our previous queue.

![Dequeue](https://github.com/SapneshNaik/AlgoDaily-UnderstandingQueues/blob/master/dequeue.png)

### Implementation using python
In python, queues can be implemented using three different modules from the python library.

 - list
 - collections.deque
 - queue.Queue

Using list class can be a costly affair since it involves shifting of elements for every addition or deletion of elements, which requires O(n) time. Instead, we can use the 'deque' class, which is a shorthand for 'Double-ended queue' and requires O(1) time, which is a lot more efficient. 

#### Implementation of queue using *deque* class
Let's go ahead and implement a queue along with its operations in python language using the deque class!

The deque class is imported from the collections module. We use `append()` function to add elements to the queue and `popleft()` function to remove elements from the queue.

    # Python program to demonstrate queue implementation using collections.dequeue 
    
    from collections import deque 
    
    # Initializing a deque with deque() constructor
    q = deque() 
    
    # Adding/Enqueueing elements to a queue 
    q.append('a') 
    q.append('b') 
    q.append('c') 
    q.append('d')
    
    print("Initial queue:") 
    print(q) 
    
    # Removing/Dequeuing elements from a queue 
    print("\nElements dequeued from the queue:") 
    print(q.popleft()) 
    print(q.popleft()) 
    print(q.popleft()) 
    
    print("\nFinal queue") 
    print(q) 

We can see that after enqueuing, our initial queue looks like this: 
> Initial queue:
deque(['a', 'b', 'c', 'd'])


And after dequeuing, our final queue looks something like this:
>Final queue
deque(['d'])

You can find more functions on deque collections [here](https://docs.python.org/2/library/collections.html#collections.deque).

#### Implementation of queue using *queue* class
Another way of implementing queues in python is by the *queue* class available in **Queue** module. It has numerous functions and is widely used along with threads for multi-threading operations. It further has FIFO, LIFO, and priority types of queues. However, we'll implement a simple queue using the *queue* class of python library.

The queue class is imported from the Queue module. The queue is initialized using the `Queue()` constructor. Note that it accepts a `maxsize()` argument, specifying an upper boundary of queue size to throttle memory usage.

We use `put()` function to add elements to the queue and `get()` function to remove elements from the queue. Since we have a maxsize check here, we have the other two functions to check empty and full conditions. Function `empty()` returns a boolean *true* if the queue is empty and *false* if otherwise. And function `full()` returns a boolean *true* if the queue is full and *false* if otherwise. 

    # Python program to demonstrate the implementation of a queue using the queue module 
    
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

Here, we added elements to the queue and checked for the full condition using `q.full().` Since the maxsize is four and we added four elements, the boolean is set to true. 

Later, we removed three elements, leaving one element in the queue. Hence the `q.empty()` function returned boolean false. 

You can find more functions on deque collections [here](https://docs.python.org/3/library/queue.html).

## Conclusion

In this article, we began right from the basics of queues then learned the queue operations later scaled to two different approaches in implementing queues using python. We saw how the FIFO approach works in queues and how using collections is effective in terms of time complexity. I recommend you to go through the resources linked in-line with the article for further reading on queues. 




