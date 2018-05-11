import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from spawners import spawnGlider, spawnReverseGlider, spawnEaterOr, spawnEaterAnd, spawnEaterNot

# N = 50
ON = 255
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
#grid = np.random.choice(vals, 80 * 158, p=[0.2, 0.8]).reshape(80, 158)

toSpawn = []
toSpawn.append(spawnGlider(1, 0))
toSpawn.append(spawnGlider(1, 40))
toSpawn.append(spawnGlider(1, 80))
toSpawn.append(spawnReverseGlider(3, 120))
toSpawn.append(spawnEaterOr())

grid = np.zeros((80, 158))

for listemt in toSpawn:
    for emt in listemt:
        grid[emt[0], emt[1]] = 1

def update(data):
  global grid
  # copy grid since we require 8 neighbors for calculation
  # and we go line by line
  newGrid = grid.copy()
  for i in range(80):
    for j in range(158):
      # compute 8-neghbor sum
      # using toroidal boundary conditions - x and y wrap around
      # so that the simulaton takes place on a toroidal surface.
      total = (grid[i, (j - 1) % 158] + grid[i, (j + 1) % 158] + grid[(i - 1) % 80, j] + grid[(i + 1) % 80, j] + grid[(i - 1) % 80, (j - 1) % 158] + grid[(i - 1) % 80, (j + 1) % 158] + grid[(i + 1) % 80, (j - 1) % 158] + grid[(i + 1) % 80, (j + 1) % 158]) / 255
      # apply Conway's rules
      if grid[i, j]  == ON:
        if (total < 2) or (total > 3):
          newGrid[i, j] = OFF
      else:
        if total == 3:
          newGrid[i, j] = ON
  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval = 1, save_count = 5)
plt.show()
