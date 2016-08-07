## given a board of characters find all words that can be formed by traversing 
## adjacent characters in all 8 possible directions starting from one particular
## cell. If word formed at a certain instant is present in dictionary then we add
## the word to the set of words formed

def boggleGame(wordmap, visited, wordset, board, i, j, M, N, word=[]):
	print "Word now: ", "".join(word)
	if visited[i][j] == False:
		word.append(board[i][j])
		visited[i][j] = True

	if wordmap.get("".join(word)) == True:
		print "Word is: ", "".join(word)
		wordset.append("".join(word))

	for row in range(i-1, i+2):
		#if row >= M:
		#	break
		for col in range(j-1, j+2):
			#if col >= N:
			#	break
			if row >=0 and col >= 0 and row < M and col < N and visited[row][col] == False:
				boggleGame(wordmap, visited, wordset, board, row, col, M, N, word)

	word = word[:-1]
	visited[i][j] = False

def playGame(wordmap, board):
	wordset = []
	M = len(board)
	N = len(board[0])

	visited = [[False] * N] * M

	print visited
	for i  in range(M):
		for j in range(N):
			boggleGame(wordmap, visited, wordset, board, i, j, M, N, [])

	return wordset

if __name__ == '__main__':
	M = int(raw_input())
	N = int(raw_input())
	words = raw_input().split(" ")
	board = []

	for i in range(M):
		chars = raw_input().split(" ")
		board.append(chars)

	wordmap = {}

	for word in words:
		wordmap[word] = True

	wordset = playGame(wordmap, board)
	print "Possible words: ", list(wordset)

