class whitehorse():
	def __init__(self,ordinates,board):
		self.ordinates=ordinates
		self.board=board
		self.checkMoves()

	def checkMoves(self):

		possible_moves=[]

		#top right
		try:
			if self.ordinates[0]-2 >= 0 and self.ordinates[1]+1 >=0:
				if self.board[self.ordinates[0]-2][self.ordinates[1]+1] == ' ' or self.board[self.ordinates[0]-2][self.ordinates[1]+1].startswith("B"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]-2,self.ordinates[1]+1]])
		except:	
			pass

		#top left
		try:
			if self.ordinates[0]-2 >= 0 and self.ordinates[1]-1 >=0:
				if self.board[self.ordinates[0]-2][self.ordinates[1]-1] == ' ' or self.board[self.ordinates[0]-2][self.ordinates[1]-1].startswith("B"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]-2,self.ordinates[1]-1]])
		except:	
			pass

		#bottom right
		try:
			if self.ordinates[0]+2 >= 0 and self.ordinates[1]+1 >=0:
				if self.board[self.ordinates[0]+2][self.ordinates[1]+1] == ' ' or self.board[self.ordinates[0]+2][self.ordinates[1]+1].startswith("B"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+2,self.ordinates[1]+1]])
		except:	
			pass

		#bottom left
		try:
			if self.ordinates[0]+2 >= 0 and self.ordinates[1]-1 >=0:
				if self.board[self.ordinates[0]+2][self.ordinates[1]-1] == ' ' or self.board[self.ordinates[0]+2][self.ordinates[1]-1].startswith("B"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+2,self.ordinates[1]-1]])
		except:	
			pass

		#left top
		try:
			if self.ordinates[1]-2 >= 0 and self.ordinates[0]-1 >=0:
				if self.board[self.ordinates[0]-1][self.ordinates[1]-2] == ' ' or self.board[self.ordinates[0]-1][self.ordinates[1]-2].startswith("B"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]-1,self.ordinates[1]-2]])
		except:
			pass

		#right top
		try:
			if self.ordinates[1]+2 >= 0 and self.ordinates[0]-1 >=0:
				if self.board[self.ordinates[0]-1][self.ordinates[1]+2] == ' ' or self.board[self.ordinates[0]-1][self.ordinates[1]+2].startswith("B"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]-1,self.ordinates[1]+2]])
		except:
			pass

		#left bottom
		try:
			if self.ordinates[1]-2 >= 0 and self.ordinates[0]+1 >=0:
				if self.board[self.ordinates[0]+1][self.ordinates[1]-2] == ' ' or self.board[self.ordinates[0]+1][self.ordinates[1]-2].startswith("B"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+1,self.ordinates[1]-2]])
		except:
			pass

		#right bottom
		try:
			if self.ordinates[1]+1 >= 0 and self.ordinates[0]+1 >=0:
				if self.board[self.ordinates[0]+1][self.ordinates[1]+2] == ' ' or self.board[self.ordinates[0]+1][self.ordinates[1]+2].startswith("B"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+1,self.ordinates[1]+2]])
		except:
			pass

		return possible_moves

