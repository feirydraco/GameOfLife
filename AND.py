import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from spawners import *
import sys

# N = 50
ON = 255
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
#grid = np.random.choice(vals, 80 * 158, p=[0.2, 0.8]).reshape(80, 158)

# try:

# except:
    # pass





def numOfNeighbors(x, y):
    total = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            try:
                if grid[i, j] == ON:
                    total += 1
            except IndexError:
                pass
    if grid[x, y] == ON:
        total -= 1
    return total

def update(data):
    global grid
    newGrid = grid.copy()
    for i in range(80):
        for j in range(130):
            total = numOfNeighbors(i, j)
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]

# set up animation
if __name__ == '__main__':
    toSpawn = []
    toSpawn.append(spawnGlider(1, 0))
    toSpawn.append(spawnGlider(0, 40))
    toSpawn.append(spawnReverseGlider(3, 90))
    toSpawn.append(spawnEaterOr())

    if int(sys.argv[1]) == 0 and int(sys.argv[2]) == 0:
        toSpawn.append(stopperAnd00())
        toSpawn.append(spawnStopperAnd())
    elif int(sys.argv[1]) == 0 and int(sys.argv[2]) == 1:
        toSpawn.append(stopperAnd01())
    elif int(sys.argv[1]) == 1 and int(sys.argv[2]) == 0:
        toSpawn.append(stopperAnd10())
    else:
        pass


    grid = np.zeros((80, 130)).reshape(80, 130)

    for listemt in toSpawn:
        for emt in listemt:
            grid[emt[0], emt[1]] = ON

    fig, ax = plt.subplots()
    mat = ax.matshow(grid)
    ani = animation.FuncAnimation(fig, update, interval = 1, save_count = 5)
    plt.show()
