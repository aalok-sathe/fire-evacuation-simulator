'''
This file accompanies other files in the evacuation simulation project.
people: Nick B., Matthew J., Aalok S.

In this file we define a useful class to model bottlenecks, 'Bottleneck'
'''

from collections import deque

class Bottleneck():
    loc = None, None
    queue = None
    numInQueue = 0

    def enterBottleNeck(self, person, throughput=1):
        self.queue.append(person)
        self.numInQueue = self.numInQueue + throughput

    def exitBottleNeck(self, throughput=1):
        if(len(self.queue) > 0):
            personLeaving = self.queue.pop()
            self.numInQueue = self.numInQueue - throughput
            return personLeaving
        else:
            return None

    def __init__(self, loc):
        '''
        constructor method
        ---
        loc (tuple xy): location (coordinates) of this bottleneck
        '''
        self.loc = loc
        self.queue = deque()
