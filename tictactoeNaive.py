##A very naive implementation of tictactoe
import random

def initialize_game():
	random.seed()
	indices = [i for i in range(9)]
	cells = [(i, j) for i in range(3) for j in range(3)]

	player_row_dict = {}
	comp_row_dict = {}
	player_col_dict = {}
	comp_col_dict = {}

	for i in range(3):
		player_row_dict[i] = []
		player_col_dict[i] = []
		comp_row_dict[i] = []
		comp_col_dict[i] = []

	player_won = False
	comp_won = False

	play(indices, cells, player_row_dict, player_col_dict, comp_row_dict, comp_col_dict)



def play(indices, cells, player_row_dict, player_col_dict, comp_row_dict, comp_col_dict):
	while True:
		if len(cells) == 0:
			print "Draw !!!"
			break

		print "Choices available: ", cells

		print "Enter the row and col index of the table you want to choose..."
		i, j = map(lambda x: int(x), raw_input().split(" "))	
		cells.remove((i, j))
		
		player_row_dict[i].append(j)
		player_col_dict[j].append(i)

		won = checkCompletion(player_row_dict, player_col_dict)
		if won is True:
			print "You Won !!!"
			break

		i, j = random.choice(cells)
		cells.remove((i, j))
		print "Comp chose: (",i, ",", j, ")"  

		comp_row_dict[i].append(j)
		comp_col_dict[j].append(i)

		won = checkCompletion(dict_row=comp_row_dict, dict_col=comp_col_dict)
		if won is True:
			print "Computer won !!!"
			break



def checkCompletion(dict_row, dict_col):
	row_keys = dict_row.keys()
	col_keys = dict_col.keys()


	##check for diagonals

	won = False

	for el in dict_row[0]:
		if el == 0:
			for j in dict_row[1]:
				if j == 1:
					for k in dict_row[2]:
						if k == 2:
							won = True
							return won

		if el == 2:
			for j in dict_row[1]:
				if j == 1:
					for k in dict_row[2]:
						if k == 0:
							won = True
							return won


	## check for any complete row
	for key in row_keys:
		prod = 1
		for el in dict_row[key]:
			prod = prod * el

		sum_keys = sum(dict_row[key])

		if sum_keys == 3 and prod == 0:
			won = True
			break

	##check for any complete column

	for key in col_keys:
		prod = 1
		for el in dict_col[key]:
			prod = prod * el

		sum_keys = sum(dict_col[key])

		if sum_keys == 3 and prod == 0:
			won = True
			break

	return won

if __name__ == "__main__":
	print "Tic Tac Toe ..."
	print "Starting game ..."
	initialize_game()

