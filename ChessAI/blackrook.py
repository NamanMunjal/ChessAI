class blackrook():
	def __init__(self,ordinates,board):
		self.ordinates=ordinates
		self.board=board
		self.atEdge=False
		self.checkMoves()

	def checkMoves(self):
		possible_moves=[]
		#axis to check moves.
		x=self.ordinates[1]
		y=self.ordinates[0]
		#to reset values for next loop.
		additional_y=self.ordinates[0]
		additional_x=self.ordinates[1]
		#runs for four directions.
		run1=True
		run2=True
		run3=True
		run4=True
		move1=[]
		move2=[]
		move3=[]
		move4=[]
		#checks.
	 	#run1-> forward
		#run2-> backward
		#run3-> left
		#run4-> right 		
		while run1:
			y-=1
			if y >= 0:
				if self.board[y][x] == ' ':
					move1.append([[y+1,x],[y,x]])
				elif self.board[y][x].startswith("W"):
					move1.append([[y+1,x],[y,x]])
					y=additional_y
					run1=False
				else:
					y=additional_y
					run1=False
			else:
				y=additional_y
				run1=False
		
		while run2:
			y+=1
			if y <= 7:
				if self.board[y][x] == ' ':
					move2.append([[y-1,x],[y,x]])
				elif self.board[y][x].startswith("W"):
					move2.append([[y-1,x],[y,x]])
					run2=False
					y=additional_y
				else:
					run2=False
					y=additional_y
			else:
				run2=False
				y=additional_y

		while run3:
			x-=1
			if x >= 0:
				if self.board[y][x] == ' ':
					move3.append([[y,x+1],[y,x]])
				elif self.board[y][x].startswith("W"):
					move3.append([[y,x+1],[y,x]])
					run3=False
					x=additional_x
				else:
					run3=False
					x=additional_x
			else:
				run3=False
				x=additional_x

		while run4:
			x+=1
			if x <= 7:
				if self.board[y][x] == ' ':
					move4.append([[y,x-1],[y,x]])
				elif self.board[y][x].startswith("W"):
					move4.append([[y,x-1],[y,x]])
					run4=False
					x=additional_x
				else:
					run4=False
					x=additional_x
			else:
				run4=False
				x=additional_x
		
		try:
			possible_moves.append([move1[0][0],move1[-1][-1]])
		except:
			pass
		try:
			possible_moves.append([move2[0][0],move2[-1][-1]])
		except:
			pass
		try:
			possible_moves.append([move3[0][0],move3[-1][-1]])
		except:
			pass
		try:
			possible_moves.append([move4[0][0],move4[-1][-1]])
		except:
			pass

		return possible_moves
