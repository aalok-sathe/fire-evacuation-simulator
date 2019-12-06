'''
This file accompanies other files in the evacuation simulation project.
people: Nick B., Matthew J., Aalok S.

In this file we define a useful class for the agent, 'Person'
'''

import random

class Person: 
    rate = None # how long it takes to move one unit distance
    strategy = None # probability with which agent picks closes exit
    loc = None, None # variable tracking this agent's location (xy coordinates)

    alive = True # TODO get rid of this variable? we don't really need this
    safe = False # mark safe once successfully exited. helps track how many
                 # people still need to finish

    exit_time = 0 # time it took this agent to get to the safe zone from its
                  # starting point


    def __init__(self, rate:float=1.0, strategy:float=.7, loc:tuple=None):
        '''
        constructor method
        ---
        rate
        strategy
        loc
        '''
        self.rate = rate
        self.strategy = strategy
        self.loc = loc


    def move(self, graph, sim):
        '''
        when this person has finished their current movement, we must schedule
        the next one
        ---
        graph (dict): a dictionary-like graph storing the floor plan according
                      to our specification
        sim: instance of a simulus simulator

        return: tuple, location the agent decided to move to 
        '''

        return None, None



