from Task import Task

class List:
    def __init__(self):
        self.start = None
        self.size = 0

    def addTask(self, task):
        if self.start:
            aux = self.start
            while aux.next:
                aux = aux.next
            aux.next = task
        else:
            self.start = task
        self.size += 1
    
    def getList(self, listType):
        aux = self.start
        count = 0
        print(f"\nTO DO LIST {listType}")
        print(10*"-")
        while(aux):
            count += 1
            print(f"{count} - {aux.text}")
            aux = aux.next
    
    def getTask(self, position):
        position = int(position)
        # print('position', position)
        if position < 0 or position > self.size:
            print ("This position doesn't exist.")
            return
        else:
            startPosition = 0
            currentNode = self.start
            while True:
                if startPosition == (position-1):
                    # print('currentNode.text', currentNode.text)
                    return currentNode.text
                currentNode = currentNode.next
                startPosition += 1
    
    def updateTask(self, position, newText):
        task = self.start
        while task:
            if task.__id__ == int(position):
                task.text = newText
                return
            task = task.next
    
    def deleteTask(self, position):
        position = int(position)
        if position < 0 or position > self.size:
            print ("This position doesn't exist.")
            return
        elif position == 1:
            start = self.start
            self.start  = self.start.next
            start.next = None
            self.size -= 1
            return
        else:
            startPosition = 0
            currentNode = self.start
            while True:
                if startPosition == (position-1):
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    self.size -= 1
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                startPosition += 1
    
        
