class blackpawn():
	
	def __init__(self,ordinates,board):
		self.ordinates=ordinates
		self.board=board

		#To check if its pawn's first move as it can move 2 blocks then.
		if int(self.ordinates[0]) == 1:
			self.isFirstMove=True
		else:
			self.isFirstMove=False
		
		self.checkMoves()

	def checkMoves(self):
		possible_moves=[]
		diagonalMove=False
		
		#To check whether a diagonal move is possible.
		try:
			if self.board[int(self.ordinates[0])+1][int(self.ordinates[1])+1] != ' ' and self.board[int(self.ordinates[0])+1][int(self.ordinates[1])+1].startswith("W"):
				diagonalMove=True
		except:
			pass
		try:
			if self.board[int(self.ordinates[0])+1][int(self.ordinates[1])-1] != ' ' and self.board[int(self.ordinates[0])+1][int(self.ordinates[1])-1].startswith("W"):
				diagonalMove=True
		except:
			pass
		
		if self.isFirstMove == True:
			#check 1 block ahead.
			if self.board[int(self.ordinates[0]+1)][int(self.ordinates[1])] == ' ':
				possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+1,self.ordinates[1]]])
			#check 2 block ahead.
			if self.board[int(self.ordinates[0]+2)][int(self.ordinates[1])] == ' ':
				possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+2,self.ordinates[1]]])
		#if its not first move then it checks only 1 block ahead.
		else:
			if self.board[int(self.ordinates[0]+1)][int(self.ordinates[1])] == ' ':
				possible_moves.append([[self.ordinates[0],self.ordinates[1]],[self.ordinates[0]+1,self.ordinates[1]]])

		#checking diagonal kill.
		if diagonalMove==True:
			#top right.
			if self.board[int(self.ordinates[0])+1][int(self.ordinates[1])+1] != ' ' and int(self.ordinates[1]) != 7:
				possible_moves.append([[self.ordinates[0],self.ordinates[1]],[int(self.ordinates[0])+1,int(self.ordinates[1])+1]])
			#top left
			if self.board[int(self.ordinates[0])+1][int(self.ordinates[1])-1] != ' ' and int(self.ordinates[1]) != 0:
				possible_moves.append([[self.ordinates[0],self.ordinates[1]],[int(self.ordinates[0])+1,int(self.ordinates[1])-1]])

		return possible_moves
		

