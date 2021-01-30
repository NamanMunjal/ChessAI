class blackwizard():
	def __init__(self,board,ordinates):
		self.ordinates=ordinates
		self.board=board
		self.checkMoves()

	def checkMoves(self):
		possible_moves=[]
		run1=True
		run2=True
		run3=True
		run4=True
		move1=[]
		move2=[]
		move3=[]
		move4=[]
		y=self.ordinates[0]
		x=self.ordinates[1]
		#to reset x and y
		additional_y=self.ordinates[0]
		additional_x=self.ordinates[1]
		
		
		while run1:
			y-=1
			x-=1
			if y>=0 and x>=0:
				if self.board[y][x] == ' ':
					move1.append([[additional_y,additional_x],[y,x]])
				elif self.board[y][x].startswith("W"):
					move1.append([[additional_y,additional_x],[y,x]])
					run1=False
					x=additional_x
					y=additional_y
				else:
					run1=False
					x=additional_x
					y=additional_y
			else:
				y=additional_y
				x=additional_x
				run1=False

		
		while run2:
			y+=1
			x+=1
			if y<=7 and x<=7:
				if self.board[y][x] == ' ':
					move2.append([[additional_y,additional_x],[y,x]])
				elif self.board[y][x].startswith("W"):
					move2.append([[additional_y,additional_x],[y,x]])
					run2=False
					x=additional_x
					y=additional_y
				else:
					run2=False
					x=additional_x
					y=additional_y
			else:
				y=additional_y
				x=additional_x
				run2=False

		
		while run3:
			y+=1
			x-=1
			if y<=7 and x>=0:
				if self.board[y][x] == ' ':
					move3.append([[additional_y,additional_x],[y,x]])
				elif self.board[y][x].startswith("W"):
					move3.append([[additional_y,additional_x],[y,x]])
					run3=False
					x=additional_x
					y=additional_y
				else:
					run3=False
					x=additional_x
					y=additional_y
			else:
				y=additional_y
				x=additional_x
				run3=False

		
		while run3:
			y-=1
			x+=1
			if y>=0 and x<=7:
				if self.board[y][x] == ' ':
					move4.append([[additional_y,additional_x],[y,x]])
				elif self.board[y][x].startswith("W"):
					move4.append([[additional_y,additional_x],[y,x]])
					run3=False
					x=additional_x
					y=additional_y
				else:
					run3=False
					x=additional_x
					y=additional_y
			else:
				y=additional_y
				x=additional_x
				run3=False
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

