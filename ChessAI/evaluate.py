from blackhorse import blackhorse
from blackrook import blackrook
from blackpawn import blackpawn
from blackking import blackking
from blackqueen import blackqueen
from blackwizard import blackwizard
from whitehorse import whitehorse
from whiterook import whiterook
from whitepawn import whitepawn
from whiteking import whiteking
from whitequeen import whitequeen
from whitewizard import whitewizard

class Evaluate():
	
	def __init__(self,board,ai):
		players=[]
		self.players=players
		self.board=board
		self.ai=ai
		self.checkPlayers()

	def checkPlayers(self):
		for y in range(0,len(self.board)):
			for x in range(0,len(self.board[y])):
				if self.board[y][x] != ' ':
					self.players.append([self.board[y][x],y,x])
				else:
					pass
		self.checkPossibleMoves()
		return self.players

	def checkPossibleMoves(self):
		moves=[]
		moves_final=[]
		functionsToCall={"BK":"blackking","BQ":"blackqueen","BW":"blackwizard","BH":"blackhorse","BR":"blackrook","BP":"blackpawn",
						 "WK":"whiteking","WQ":"whitequeen","WW":"whitewizard","WH":"whitehorse","WR":"whiterook","WP":"whitepawn"}
		if self.ai==True:
			for player in range(0,len(self.players)):
				if self.players[player][0].startswith("B"):
					call=globals()[functionsToCall[self.players[player][0]]](ordinates=[self.players[player][1],self.players[player][2]],board=self.board)
					moves.append(call.checkMoves())
		else:
			for player in range(0,len(self.players)):
				if self.players[player][0].startswith("W"):
					call=globals()[functionsToCall[self.players[player][0]]](ordinates=[self.players[player][1],self.players[player][2]],board=self.board)
					moves.append(call.checkMoves())
		for move in range(0,len(moves)):
			if len(moves[move])==0:
				pass
			else:
				moves_final.append((moves[move]))
		return moves_final

