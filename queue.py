import sys
class Queue:
    def __init__(self, queueSize):
        self.size = queueSize
        self.queueList = []  # queue created

    def isFull(self):
        if len(self.queueList) == self.size:
            return True
        else:
            return False
        
    def Enqueue(self, value):
        if self.isFull():
            print("Queue is full, cannot push element")
        else:
            self.queueList.append(value)  # add element in queue

    def displayQueue(self):
        print("-------------------------")
        print(self.queueList)  # display queue
        print("-------------------------")
    
    def isEmpty(self):
        if self.queueList == []:
            return True
        else:
            return False
        
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot dequeue element")
        else:
            return self.queueList.pop(0)  # remove element from front of queue
        
    def deleteQueue(self):
        self.queueList = []  # delete queue by reassigning empty list
        return "Queue is deleted"
    
    def peek(self):     #It returns first element of a queue
        if self.isEmpty():
            print("Queue is empty, cannot peek element")
        else:
            return self.queueList[0]  # return first element of queue without removing it


size = int(input("Enter the size of queue : "))
queueObj  = Queue(size)

while True:
    print("=============================")
    print("1. Enqueue Element in Queue : ")
    print("2. Display Queue : ")
    print("3. Check isEmpty : ")
    print("4. Dequeue Element from Queue : ")
    print("5. Delete Queue : ")
    print("6. Peek Element from Queue : ")
    print("7. Exit : ")

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        val = int(input("Enter a value to enqueue in Queue : "))
        queueObj.Enqueue(val)
    elif choice == 2:
        queueObj.displayQueue()
    elif choice == 3:
        print("Check isEmpty : ",queueObj.isEmpty())
    elif choice == 4:
        print("Dequeued element is : ",queueObj.Dequeue())
    elif choice == 5:
        print(queueObj.deleteQueue())
    elif choice == 6:
        print("Top element of queue is : ",queueObj.peek()) 
    elif choice == 7:
        sys.exit()
    else:
        print("Invalid Choice!")