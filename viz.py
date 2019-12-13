import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib import colors, colorbar
import numpy as np


class Plot:

    def __init__(self):
        '''
        '''
        plt.ion()


    def draw_layout(self, graph=[(3,4), {'F': 1}]):
        '''
        '''

        # an arbitrary assignment of integers for each of the attributes
        attrmap = {'N': 0, 'W': 1, 'F': 2, 'S': 3, 'B': 4}

        # detect rows and columns
        # TODO

        # start with a blank grid
        gdata = np.zeros(shape=(10, 10))

        for loc, attrs in graph:
            for att in 'SWBF':
                if att not in attrs: continue
                if attrs[att]:
                    gdata[loc] = attrmap
                    break

        self.draw_positions(gdata)


    def draw_positions(self, data):
        '''
        '''
        r, c = len(data), len(data[0])

        # create discrete colormap
        cmap = colors.ListedColormap(['lightblue', 'lightgrey', 'red',
                                      'green', 'darkblue'])
        bounds = [-.5, .5, 1.5, 2.5, 3.5, 4.5]

        plt.imshow(data, cmap=cmap, norm=norm)

        # draw gridlines
        plt.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        plt.xticks(np.arange(-.5, r, 1));
        plt.yticks(np.arange(-.5, c, 1));

        plt.draw()
        plt.pause(.0001)

        plt.clf()


for i in range(10):
    break
    x = np.random.random([2, 10])
    print(x)
    plt.scatter(*x)

    plt.draw()
    plt.pause(0.0001)

    plt.clf()




if __name__ == '__main__':
    grid = Plot()

    grid.draw_layout()

raise
# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue'])
bounds = range()
norm = colors.BoundaryNorm(bounds, cmap.N)

for i in range(50):

    data = np.zeros(shape=(10, 10))# * 20

    #fig, ax = plt.subplots()
    plt.imshow(data, cmap=cmap, norm=norm)

    # draw gridlines
    plt.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    plt.xticks(np.arange(-.5, 10, 1));
    plt.yticks(np.arange(-.5, 10, 1));

    plt.draw()
    plt.pause(.0001)

    plt.clf()
