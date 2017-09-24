from puzzle import Puzzle

def bfsWeight (state):
	return 0

#considera que a solucao eh sempre a mesmo, com os valores ordenados de 0 ate state.size^2-1
def manhattanWeight (state):
	weight = 0
	for stateI in range(state.size):
		for stateJ in range(state.size):
			desiredI = state.state[stateI][stateJ] // state.size
			desiredJ = state.state[stateI][stateJ] % state.size
			weight += abs(stateI - desiredI) + abs(stateJ - desiredJ)
	return weight

def uniformWeight (state):
	return state.depth


def aStarWeight (state):
	return manhattanWeight(state) + uniformWeight(state)
			
