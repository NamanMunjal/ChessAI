class blackking():
	def __init__(self,ordinates,board):
		self.ordinates=ordinates
		self.board=board
		self.checkMoves()

	def checkMoves(self):
		possible_moves=[]

		if self.ordinates[0] != 0:
			try:
				#check front block
				if self.board[self.ordinates[0]-1][self.ordinates[1]] == ' ' or self.board[self.ordinates[0]-1][self.ordinates[1]].startswith("W"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]-1,self.ordinates[1]]])
			except:
				pass
		else:
			pass
		if self.ordinates[0] != 7:
			try:
				#check back block
				if self.board[self.ordinates[0]+1][self.ordinates[1]] == ' ' or self.board[self.ordinates[0]+1][self.ordinates[1]].startswith("W"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+1,self.ordinates[1]]])
			except:
				pass
		else:
			pass
		if self.ordinates[1] != 7:
			try:
				#check right block
				if self.board[self.ordinates[0]][self.ordinates[1]+1] == ' ' or self.board[self.ordinates[0]][self.ordinates[1]+1].startswith("W"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0],self.ordinates[1]+1]])
			except:
				pass
		else:
			pass
		if self.ordinates[1] != 0:
			#check left block
			try:
				if self.board[self.ordinates[0]][self.ordinates[1]-1] == ' ' or self.board[self.ordinates[0]][self.ordinates[1]-1].startswith("W"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0],self.ordinates[1]-1]])
			except:
				pass
		else:
			pass
		try:
			#check top right
			if self.ordinates[0]-1 != -1 and self.ordinates[1]+1 != -1:
				if self.board[self.ordinates[0]-1][self.ordinates[1]+1] == ' ' or self.board[self.ordinates[0]-1][self.ordinates[1]+1].startswith("W"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]-1,self.ordinates[1]+1]])
		except:
			pass
		try:
			#check top left
			if self.ordinates[0]-1 != -1 and self.ordinates[1]-1 != -1:
				if self.board[self.ordinates[0]-1][self.ordinates[1]-1] == ' ' or self.board[self.ordinates[0]-1][self.ordinates[1]-1].startswith("W"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]-1,self.ordinates[1]-1]])
		except:
			pass
		try:
			#check bottom right
			if self.ordinates[0]+1 != -1 and self.ordinates[1]+1 != -1:
				if self.board[self.ordinates[0]+1][self.ordinates[1]+1] == ' ' or self.board[self.ordinates[0]+1][self.ordinates[1]+1].startswith("W"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+1,self.ordinates[1]+1]])
		except:
			pass
		try:
			#check bottom left
			if self.ordinates[0]+1 != -1 and self.ordinates[1]-1 != -1:
				if self.board[self.ordinates[0]+1][self.ordinates[1]-1] == ' ' or self.board[self.ordinates[0]+1][self.ordinates[1]-1].startswith("W"):
					possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+1,self.ordinates[1]-1]])
		except:
			pass

		return possible_moves
