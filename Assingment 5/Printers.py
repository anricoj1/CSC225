class Queue: # i decided to jsut write the Queue class instead of importing
   def __init__(self):
      self.items = []

   def is_empty(self):
      return self.items == []

   def enqueue(self, item):
      self.items.insert(0,item)

   def dequeue(self):
      return self.items.pop()

   def size(self):
      return len(self.items)

class Printer:   # Created the rest of the classes
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time,minSize,maxSize):
        self.timestamp = time
        self.pages = random.randrange(minSize,maxSize)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(numberOfIterations, numSeconds, pagesPerMinute, minSize, maxSize,file):
    total = 0
    printContent = []

    for i in range(numberOfIterations):
        labprinter = Printer(pagesPerMinute)    
        printQueue = Queue()
        waitingtimes = []

        for currentSecond in range(numSeconds):
            if newPrintTask():
                task = Task(currentSecond,minSize,maxSize)
                printQueue.enqueue(task)

            if not labprinter.busy() and not printQueue.is_empty():
                nexttask = printQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter.startNext(nexttask)

            labprinter.tick()

        averageWait = sum(waitingtimes)/len(waitingtimes)
        total = total + averageWait
        file.write("Average Wait %6.2f secs %3d tasks remaining.\n" % (averageWait,printQueue.size()))

    averagetotal = total/numberOfIterations
    file.write('Total average wait time: %.2f secs\n' % averagetotal)

def simulationTwoPrinters(numberOfIterations, numSeconds, pagesPerMinute,pagesPerMinute2, minSize, maxSize,file):
    total = 0
    printContent =[]
 
    for i in range(numberOfIterations):
        labprinter = Printer(pagesPerMinute)
        labprinter2 = Printer(pagesPerMinute2) 
        
        printQueue = Queue()
        waitingtimes = []

        for currentSecond in range(numSeconds):
            if newPrintTask():
                task = Task(currentSecond,minSize,maxSize)
                printQueue.enqueue(task)

            if not labprinter.busy() and not printQueue.is_empty():
                nexttask = printQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter.startNext(nexttask)

            if not labprinter2.busy() and not printQueue.is_empty():
                nexttask = printQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter2.startNext(nexttask)

            if not labprinter.busy() and not labprinter2.busy() and not printQueue.is_empty():
                if pagesPerMinute > pagesPerMinute2:       
                    nexttask = printQueue.dequeue()
                    waitingtimes.append(nexttask.waitTime(currentSecond))
                    labprinter.startNext(nexttask)
                elif pagesPerMinute2 > pagesPerMinute:
                    nexttask = printQueue.dequeue()
                    waitingtimes.append(nexttask.waitTime(currentSecond))
                    labprinter2.startNext(nexttask) 

            labprinter.tick()
            labprinter2.tick()

        averageWait = sum(waitingtimes)/len(waitingtimes)
        total = total + averageWait
        file.write("Average Wait %6.2f secs %3d tasks remaining.\n" % (averageWait,printQueue.size()))

    averagetotal = total/numberOfIterations
    file.write('Total average wait time: %.2f secs\n' % averagetotal)

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

# from sim_config.txt file
def getConfigurations():
    configs = []
    config = dict()
    
    keys = ['simTime','simExperiments','minTask','maxTask','numOfPrinters','ppmPrintOne','ppmPrintTwo']

    
    inFile = open('sim_config.txt','r')
    filecontent = inFile.readlines()
    
    counter = 0
    for content in filecontent:
        if content == '\n':
            #push configurations to list
            configs.append(config)
            
            
            counter = 0
            config = dict()
        else:
            config[keys[counter]] = content.replace('\n','')
            counter = counter + 1

    return configs

def runProject(config,file):
    configs = getConfigurations()
    numOfPrinters = int(config['numOfPrinters'])
    
    try:
        if numOfPrinters <= 2:
            if numOfPrinters == 1:
                simulation(int(config['simExperiments']),
                           int(config['simTime']),
                           int(config['ppmPrintOne']),
                           int(config['minTask']),
                           int(config['maxTask']),fout)
                file.write('\n')
            if numOfPrinters == 2:
                simulationTwoPrinters(int(config['simExperiments']),
                                      int(config['simTime']),
                                      int(config['ppmPrintOne']),
                                      int(config['ppmPrintTwo']),
                                      int(config['minTask']),
                                      int(config['maxTask']),fout)
                file.write('\n')
               
        else:
            file.write('No valid printers. Exiting\n')
        
        
    except ValueError:
        file.write('Format error. Exiting\n')

def main(): # main program
    configs = getConfigurations()
    file = open("sim_out.txt",'w')
    
    print("===== Processing ====== ")
    for config in configs:
        runProject(config,file)
    file.close()
    print('Complete! wrote to sim_out.txt')
        
  
if __name__ == "__main__":
    main()
