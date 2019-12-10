'''
This file accompanies other files in the evacuation simulation project.
people: Nick B., Matthew J., Aalok S.

In this file we define a useful class to model bottlenecks, 'Bottleneck'
'''

from queue import Queue


class Bottleneck(Queue):
    loc = None, None

    def __init__(self, loc):
        '''
        constructor method
        ---
        loc (tuple xy): location (coordinates) of this bottleneck
        '''
        super().__init__()
        self.loc = loc
