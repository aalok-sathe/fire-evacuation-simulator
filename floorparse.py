#!/usr/bin/env python3

from collections import defaultdict

class FloorParser:

    def __init__(self):
        pass

    def parse(self, floor):
        '''
        parses a txt floor
        '''
        grid = []

        for row in floor.split('\n'):
            if not row: continue
            sqs = row.split(';')
            rowattrs = [set(sq.strip().split(',')) for sq in sqs]
            print(' '.join([list(row)[0] for row in rowattrs]))
            grid += [rowattrs]


        graph = defaultdict(lambda: {'nbrs': set()})

        R, C = len(grid), len(grid[0])
       
        for i in range(R):
            for j in range(C):
                attrs = grid[i][j]
                graph[(i,j)].update({att:int(att in attrs) for att in 'WSBFNP'})
                
                for off in {-1, 1}:
                    if 0 <= i+off < R:
                        graph[(i,j)]['nbrs'].add((i+off, j))

                    if 0 <= j+off < C:
                        graph[(i,j)]['nbrs'].add((i, j+off))
        
        self.graph = dict(graph.items())
        return self.graph

