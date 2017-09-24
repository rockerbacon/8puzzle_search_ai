from puzzle import Puzzle
from agent import PuzzleAgent
import weights

import sys

# Program call: python3 main.py <file with puzzle> <method> <time limit in seconds>
# For puzzles bigger than 3x3 change puzzleSize in line 17
# For the method argument use:
#	BFS for Breadth first search
#	A* for A* search
#	GREEDY for greedy search
#	UNIFORM for uniform cost search
# 	
def main(puzzleFile, method, timeLimit):

	puzzleSize = 3

	#print(puzzleSize)	#debug
	problem = Puzzle()
	problem.loadFile(open(puzzleFile, 'r'), puzzleSize)
	solution = Puzzle()
	solution.loadFile(open('solution.txt', 'r'), puzzleSize)
	solver = None

	if method == 'BFS':
		solver = PuzzleAgent(weights.bfsWeight)
	elif method == 'A*':
		solver = PuzzleAgent(weights.aStarWeight)
	elif method == 'GREEDY':
		solver = PuzzleAgent(weights.manhattanWeight)
	elif method == 'UNIFORM':
		solver = PuzzleAgent(weights.uniformWeight)
	else:
		print('Invalid method')
		return

	#problem.printState()	#debug

	solution = solver.solve(problem, solution, timeLimit)

	while solution:
		solutionStep = solution.pop()
		solutionStep.printState()

main(sys.argv[1], sys.argv[2], float(sys.argv[3]))
