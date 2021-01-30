from evaluate import Evaluate

class play():
	
	def __init__(self,board):
		self.board=board
		self.current_board=board
		self.points=[]
		self.pointstobeawarded={"WK":20,"WQ":9,"WH":3,"WW":3,"WP":1,"WR":7,
								"BK":-20,"BQ":-9,"BH":-3,"BW":-3,"BP":-1,"BR":-7," ":0}
		self.playit()

	def playit(self):
		point=0
		evaluation_ai=Evaluate(self.board,True)
		aiMoves=evaluation_ai.checkPossibleMoves()
		depth=0
		print(aiMoves[0][0][0])
		

board=[['BR','BH','BW','BQ','BK','BW','BH','BR'],
		['BP','BP','BP','BP','BP','BP','BP','BP'],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		['WP','WP','WP','WP','WP','WP','WP','WP'],
		['WR','WH','WW','WQ','WK','WW','WH','WR']]

play(board=board)