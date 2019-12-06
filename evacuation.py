'''
This is the main file in the evacuation simulation project.
people: Nick B., Matthew J., Aalok S.

In this file we define a useful class to model the building floor, 'Floor'

Also in this file, we proceed to provide a main method so that this file is
meaningfully callable to run a simulation experiment
'''

import simulus 
import sys
#import random
from randomgen import PCG64
from argparse import ArgumentParser

# local project imports
from person import Person
from bottleneck import Bottleneck

class Floor:
    sim = None
    graph = None

    numpeople = 0

    bottlenecks = []
    people = []

    def __init__(self, graph, n, location_sampler=random.sample,
                 strategy_generator=lambda: random.uniform(.5, 1.)):
        '''
        constructor method
        ---
        graph (dict): a representation of the floor plan as per our
                      specification
        n (int): number of people in the simulation
        '''
        self.sim = simulus.simulation()
        self.graph = graph
        self.numpeople = n

        setup()


    def setup(self):
        '''
        '''

        pass


    def update_bottlenecks(self):
        '''
        handles the bottleneck zones on the grid, where people cannot all pass
        at once. for simplicity, bottlenecks are treated as queues
        '''
            sim.sched(updateBottleNecks, offset = 1)
            pass


positions = []
bottlenecks = []
for i in numPeople:
	people.append(person.Person(
		random.uniform(0.5, 4), 
		random.uniform(0.5, 1.0), 
		*random.sample(positions, 1))


#start simulation (simulus)

#update bottlenecks 
sim.sched(updateBottleNecks, offset = 1)

#schedule initial movements for each Person() using their rate 
for i in numPeople:
	sim.sched(people[i].move, graph, sim, offset = people[i].rate)


def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='floor.txt.pkl',
                        help='input floor plan file')
    parser.add_argument('-n', '--numpeople', type=int, default=1000,
                        help='number of people in the simulation')
    parser.add_argument('-s', '--random_state', type=int, default=8675309,
                        help='aka. seed')
    args = parser.parse_args()


    strat_strm, loc_strm, inst_strm = [PCG64(args.random_state, i) 
                                       for i in range(3)]
    strategy_generator = lambda: strat_strm.uniform(.5, 1)
    location_sampler = loc_strm.choice
    uniform_generator = lambda: inst_strm.uniform()

    floor = Floor()


if __name__ == '__main__':
    main()
