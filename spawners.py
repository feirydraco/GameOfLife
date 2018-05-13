def spawnGlider(x, y):
    toSpawn = [[5, 1],[6, 1],[6, 2],[5, 2],[5, 5],[4, 6],[5, 6],[6, 6],[3, 7],[7, 7],[5, 8],[2, 9],[2, 10],
                [3, 11], [4, 12],[5, 12],[6, 12],[7, 11],[8, 10],[8, 9],[7, 17],[7, 20],[7, 21],[7, 22],[6, 22],[5, 21],[6, 26],
               [5, 26],[1, 26],[0, 26],[1, 28],[5, 28],[2, 29],[3, 29],[4, 29],[4, 30],[3, 30],[2, 30],[3, 35],
               [4, 35],[4, 36],[3, 36]]
    for emt in toSpawn:
        emt[0] += x
        emt[1] += y
    return toSpawn

def spawnReverseGlider(x, y):
    toSpawn = [[0, 0], [1, 0], [1, 1], [0, 1], [0, 6], [1, 6], [1, 7], [0, 7], [-1, 7], [-1, 6], [-2, 8], [-2, 10], [-3, 10],
     [2, 8], [2, 10], [3, 10], [3, 14], [4, 14], [4, 15], [4, 16], [2, 15], [4, 19], [4, 25], [3, 24], [2, 24], [1, 24], [0, 25],
      [-1, 26], [-1, 27], [5, 26], [5, 27], [2, 28], [2, 30], [2, 31], [1, 30], [3, 30], [0, 29], [4, 29], [2, 34], [2, 35], [3, 35], [3, 34]]
    for emt in toSpawn:
        emt[0] += x
        emt[1] += y
    return toSpawn

def spawnEaterAnd():
    toSpawn = [[56, 66], [57, 66], [57, 67], [57, 69], [57, 67], [55, 69], [55, 70],
               [56, 70], [55, 73], [56, 73], [56, 74], [55, 74], [59, 66], [59, 67], [60, 67], [60, 66], [57, 68]]
    return toSpawn

def spawnEaterOr():
    toSpawn = [[72, 82], [73, 82], [73, 83], [73, 84], [73, 85], [72, 86], [71, 86], [71, 85], [71, 89],
               [72, 89], [72, 90], [71, 90], [75, 82], [75, 83], [76, 83], [76, 82]]
    return toSpawn

def spawnEaterNot():
    toSpawn = [[32, 24], [32, 25], [33, 24], [33, 24], [33, 25], [32, 28], [32, 29], [33, 28],
                [34, 29], [34, 30], [34, 31], [34, 32], [33, 32], [36, 31], [36, 32], [37, 32],
                [37, 31]]
    return toSpawn

def spawnStopperOr():
    toSpawn = [[58, 111], [59, 111], [58, 112], [60, 112], [60, 113], [60, 114], [61, 114]]
    return toSpawn

def stopperAnd01():
    toSpawn = [[15, 28], [16, 28], [15, 29], [17, 29], [17, 30], [17, 31], [18, 31]]
    return toSpawn
def stopperAnd10():
    toSpawn = [[14, 68], [15, 68], [14, 69], [16, 69], [16, 70], [16, 71], [17, 71]]
    return toSpawn
def stopperAnd00():
    toSpawn = [[14, 68], [15, 68], [14, 69], [16, 69], [16, 70], [16, 71], [17, 71], [15, 28], [16, 28], [15, 29], [17, 29], [17, 30], [17, 31], [18, 31]]
    return toSpawn
def spawnStopperAnd():
    toSpawn = [[56, 55], [56, 56], [57, 56], [58, 55], [58, 54], [58, 53], [59, 53]]
    return toSpawn
