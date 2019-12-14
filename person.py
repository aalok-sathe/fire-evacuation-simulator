'''
This file accompanies other files in the evacuation simulation project.
people: Nick B., Matthew J., Aalok S.

In this file we define a useful class for the agent, 'Person'
'''

import random

class Person:
    id = None
    rate = None # how long it takes to move one unit distance
    strategy = None # probability with which agent picks closes exit
    loc = None, None # variable tracking this agent's location (xy coordinates)

    alive = True # TODO get rid of this variable? we don't really need this
    safe = False # mark safe once successfully exited. helps track how many
                 # people still need to finish

    exit_time = 0 # time it took this agent to get to the safe zone from its
                  # starting point


    def __init__(self, id, rate:float=1.0, strategy:float=.7, loc:tuple=None):
        '''
        constructor method
        ---
        rate
        strategy
        loc
        '''
        self.id = id
        self.rate = rate
        self.strategy = strategy
        self.loc = tuple(loc)


    def move(self, nbrs, rv=None):
        '''
        when this person has finished their current movement, we must schedule
        the next one
        ---
        graph (dict): a dictionary-like graph storing the floor plan according
                      to our specification

        return: tuple, location the agent decided to move to
        '''
        nbrs = [(loc, attrs) for loc, attrs in nbrs
                if not(attrs['F'] or attrs['W'])]
        if not nbrs: return None
        loc, attrs = min(nbrs, key=lambda tup: tup[1]['distS'])
        # print('Person {} at {} is moving to {}'.format(self.id, self.loc, loc))
        # print('Person {} is {} away from safe'.format(self.id, attrs['distS']))
        self.loc = loc
        if attrs['S']:
            self.safe = True
        elif attrs['F']:
            self.alive = False

        return loc
