direction = { 'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1) }

class Puzzle:

	def __init__(self):
		self.state = [[]]
		self.zeroPos = (-1, -1)
		self.size = 0
		self.depth = 0
		self.weight = 0
		self.father = self

	def loadFile (self, inputFile, size):
		self.state = [[int(d) for d in line.split()] for line in inputFile]

		i = 0
		while self.zeroPos == (-1, -1):
			j = 0
			for e in self.state[i]:
				if e == 0:
					self.zeroPos = (i, j)
					break				
				j = j+1
			i = i+1

		self.size = size

	def __hash__(self):
		return self.weight

	def __eq__(self, other):
		for i in range(self.size):
			for j in range(self.size):
				if self.state[i][j] != other.state[i][j]:
					return False
		return True

	def __lt__(self, other):
		return self.weight < other.weight

	def copySelf (self):
		copy = Puzzle()
		copy.state = [line.copy() for line in self.state]
		copy.zeroPos = self.zeroPos
		copy.size = self.size
		copy.depth = self.depth+1
		copy.weight = self.weight
		copy.father = self
		return copy

	def move(self, directionKey):
		i = self.zeroPos[0] + direction[directionKey][0]
		j = self.zeroPos[1] + direction[directionKey][1]
		#print (i, j, self.size)	#debug
		if i >= 0 and i < self.size and j >= 0 and j < self.size:
			#print('swap')	#debug
			self.state[i][j], self.state[self.zeroPos[0]][self.zeroPos[1]] = self.state[self.zeroPos[0]][self.zeroPos[1]], self.state[i][j]
			self.zeroPos = (i, j)
			return True
		return False
		
	def printState(self):
		for line in self.state:
			for e in line:
				print(e, end=' ')
			print(end='\n')
		print(end='\n')			
