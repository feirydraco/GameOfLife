# GameOfLife

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically or diagonally adjacent. At each step in time, the following transitions occur:
	1. Any live cell with fewer than two live neighbours dies, as if by loneliness.
	2. Any live cell with more than three live neighbours dies, as if by overcrowding.
	3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
	4. Any dead cell with exactly three live neighbours comes to life.
The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations.
Using the above stated rules, we can create "life forms" which can be broadly categorized as:
- Stable patterns. They remain unchanged if not disturbed. The simplest one is the 2 x 2 cell square block. Another example is the generation of a beehive.
- Blinkers. They usually change their configuration in a very short cycle. 
A logical gate is some kind of "black box" which is able to process two Boolean variables, inputs according to a specified Boolean operator. To implement a logical gate we therefore need:
- Some kind of electrical pulses to represent inputs.
- Wires to transmit the electrical pulses.
- Processing devices which associate inputs and compute the Boolean result.
- A device placed after the processing device, able to check the output electrical pulses. 
This will represent the output.
We thus encode these items in the Game of Life objects as follows:
- Input and output electrical pulses >> Gliders.
- Wires >> Trajectories of glider movements.
- Processing devices >> Collision of gliders.
- Output device >> Collision of gliders with immobile patterns
