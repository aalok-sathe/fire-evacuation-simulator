#!/usr/bin/env python3

'''
This is the main file in the evacuation simulation project.
people: Nick B., Matthew J., Aalok S.

In this file we define a useful class to model the building floor, 'Floor'

Also in this file, we proceed to provide a main method so that this file is
meaningfully callable to run a simulation experiment
'''

# stdlib imports
import simulus 
import sys
import pickle
import random
import pprint
# from floorplan.floorplan import FloorGUI
from argparse import ArgumentParser
try:
    from randomgen import PCG64, RandomGenerator as Generator
except ImportError:
    from randomgen import PCG64, Generator

# local project imports
from person import Person
from bottleneck import Bottleneck


pp = pprint.PrettyPrinter(indent=4).pprint

class Floor:
    sim = None
    graph = None
    gui = None
    r = None
    c = None

    numpeople = 0

    bottlenecks = []
    people = []

    def __init__(self, graph, n, location_sampler=random.sample,
                 strategy_generator=lambda: random.uniform(.5, 1.),
                 rate_generator=lambda: abs(random.normalvariate(1, .5)),
                 uniform_generator=random.uniform):
        '''
        constructor method
        ---
        graph (dict): a representation of the floor plan as per our
                      specification
        n (int): number of people in the simulation
        '''
        self.sim = simulus.simulator()
        self.graph = graph
        self.numpeople = n

        self.location_sampler = location_sampler
        self.strategy_generator = strategy_generator
        self.rate_generator = rate_generator
        self.uniform_generator = uniform_generator

        self.setup()


    def setup(self):
        '''
        once we have the parameters and random variate generation methods from
        __init__, we can proceed to create instances of: people and bottlenecks
        '''
        
        av_locs = []
        bottleneck_locs = []
        # W, F, S, B, P, N = 'WFSBPN'
        r, c = 0, 0
        for loc, attrs in self.graph.items():
            r = max(r, loc[0])
            c = max(c, loc[1])
            if attrs['P']: av_locs += [loc] 
            elif attrs['B']: bottleneck_locs += [loc]

        for i in range(self.numpeople):
            p = Person(self.rate_generator(),
                       self.strategy_generator(),
                       self.location_sampler(av_locs))
            self.people += [p]

        for loc in bottleneck_locs:
            b = Bottleneck(loc)            
            self.bottlenecks += [b]
        
        self.r, self.c = r+1, c+1
        
        # self.gui = FloorGUI(self.r, self.c)
        # self.gui.setup()
        # self.gui.window.Read(timeout=0)
        # self.gui.load(self.graph)
        # self.gui.window.Read(timeout=1000)

        print(
              '='*79,
              'initialized a {}x{} floor with {} people in {} locations'.format(
                    self.r, self.c, len(self.people), len(av_locs)
                  ),
              'initialized {} bottleneck(s)'.format(len(self.bottlenecks)),
              '='*79, sep='\n'
             )


    def update_bottlenecks(self):
        '''
        handles the bottleneck zones on the grid, where people cannot all pass
        at once. for simplicity, bottlenecks are treated as queues
        '''
        raise NotImplementedError


    def update_people(self):
        '''
        handles scheduling an update for each person, by calling move() on them.
        move will return a location decided by the person, and this method will
        handle the simulus scheduling part to keep it clean
        '''
        raise NotImplementedError
       

    def simulate(self, *args):
        '''
        '''
        raise NotImplementedError



def main():
    '''
    driver method for this file
    '''
    # set up and parse commandline arguments
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='floor.txt.pkl',
                        help='input floor plan file (default:floor.txt.pkl)')
    parser.add_argument('-n', '--numpeople', type=int, default=10,
                        help='number of people in the simulation (default:10)')
    parser.add_argument('-s', '--random_state', type=int, default=8675309,
                        help='aka. seed (default:8675309)')
    args = parser.parse_args()
    # output them as a make-sure-this-is-what-you-meant
    print('commandline arguments:', args, '\n')


    # load the graph representation of some floor plan
    with open(args.input, 'rb') as f:
        graph = pickle.load(f)

    # set up random streams
    streams = [Generator(PCG64(args.random_state, i)) for i in range(4)]
    loc_strm, strat_strm, rate_strm, inst_strm = streams
    
    location_sampler = loc_strm.choice
    strategy_generator = lambda: strat_strm.uniform(.5, 1)
    rate_generator = lambda: abs(rate_strm.normal(1, .5))
    uniform_generator = lambda: inst_strm.uniform()

    # create an instance of Floor
    floor = Floor(graph, args.numpeople, location_sampler, strategy_generator,
                  rate_generator, uniform_generator)

    # call the simulate method to run the actual simulation
    # floor.simulate() 


if __name__ == '__main__':
    main()
