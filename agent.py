import puzzle
from heapq import heappush, heappop
from time import clock

class PuzzleAgent:

	def __init__(self, weightFunction):
		self.weightFunction = weightFunction

	def solve (self, initialState, solvedState, timeLimit):

		initialState.weight = self.weightFunction(initialState)

		#fila do prioridades feita utilizando uma heap
		heap = [(initialState.weight, initialState)]
		checked = [initialState]

		initialTime = clock()

		while heap:
			puzzleState = heappop(heap)[1]
			#puzzleState.printState()	#debug

			if puzzleState == solvedState:
				
				#se encontrou solucao, faz backtracing do caminho colocando os estados em uma pilha de solucoes
				stack = [puzzleState]

				childState = puzzleState
				fatherState = puzzleState.father
				while fatherState != childState:
					childState = fatherState
					fatherState = childState.father
					stack.append(childState)

				return stack

			else:

				#para todo movimento do puzzle
				for direction in puzzle.direction:
					#cria copia do estado atual
					nextState = puzzleState.copySelf()
					#puzzleState.printState()	#debug

					#se o movimento eh valido para o estado atual do puzzle
					if nextState.move(direction):
						#puzzleState.printState()	#debug
						#atualiza peso do estado
						nextState.weight = self.weightFunction(nextState)

						#se o estado ainda nao foi alcancado
						if nextState not in checked:
							#coloca o estado na fila de prioridade
							heappush(heap, (nextState.weight, nextState) )
							#marca o estado como alcancado
							checked.append(nextState)

			if (clock() - initialTime > timeLimit):
				print('could not solve on time')
				return None
				
