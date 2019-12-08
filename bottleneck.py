'''
This file accompanies other files in the evacuation simulation project.
people: Nick B., Matthew J., Aalok S.

In this file we define a useful class to model bottlenecks, 'Bottleneck'
'''

from queue import Queue
from collections import deque

class Bottleneck(Queue):
    loc = None, None
    queue = None
    numInQueue = 0

    def enterBottleNeck(self, person):
        self.queue.append(person)
        self.queue.numInQueue = self.queue.numInQueue + 1
        print(self.queue)

    def exitBottleNeck(self, sim):
        if(len(self.queue) > 0):
            newSafePerson = self.queue.pop()
            self.queue.numInQueue = self.queue.numInQueue - 1
            newSafePerson.safe = True
            newSafePerson.exit_time = sim.now
            print(self.queue)

    def __init__(self, loc):
        '''
        constructor method
        ---
        loc (tuple xy): location (coordinates) of this bottleneck
        '''
        super().__init__()
        self.loc = loc
        queue = deque()
