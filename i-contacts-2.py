from queue import Queue

class ContactTracer:
    def __init__(self):
        self.contacts = {}
        self.counts = {}
    
    def addContact(self, num1, num2):
        if num1 not in self.contacts:
            self.contacts[num1] = {num2}
            self.counts[num1] = 1
        else:
            if num2 not in self.contacts[num1]:
                self.contacts[num1].add(num2)
                self.counts[num1] += 1
    
    def processLine(self, line):
        num1, num2 = line.split('-')
        self.addContact(num1, num2)
        self.addContact(num2, num1)
        
    def getHighestNumberOfContacts(self):
        if not self.counts:
            return 0
        return max(self.counts.values())
    
    def getNumberOfClusters(self):        
        numClusters = 0
        visited = {c: False for c in self.contacts.keys()}
        
        # Iterate through each number
        for num in visited.keys():
            # If not yet visited, traverse graph to visit all connected nodes 
            if not visited[num]:
                visited[num] = True
                numClusters += 1
                
                # Construct queue
                q = Queue()
                for n in self.contacts[num]:
                    q.put(n)
                
                # Traverse graph while queue is not empty
                while not q.empty():
                    n = q.get()
                    visited[n] = True
                    for m in self.contacts[n]:
                        if not visited[m]:
                            q.put(m)
            
        return numClusters

if __name__ == '__main__':
    contactTracer = ContactTracer()
    while True:
        try:
            line = input()            
            if line == 'Q1':
                print(contactTracer.getHighestNumberOfContacts())
            elif line == 'Q2':
                print(contactTracer.getNumberOfClusters())
            else:
                contactTracer.processLine(line)
        except:
            break
