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

if __name__ == '__main__':
    contactTracer = ContactTracer()
    while True:
        try:
            line = input()
            if line == 'Q1':
                print(contactTracer.getHighestNumberOfContacts())
            else:
                contactTracer.processLine(line)
        except:
            break
