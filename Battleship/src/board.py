'''
left diagonal:
x
 x
  x

right diagonal:
  x
 x
x
return all_same((self.board[i][i] for i in range (self.board.num_rows))) #this is a generator expression
'''
# Two ways of picking up every other element of a list
# e.g. produce [1, 5, 9] from [1, 3, 5, 7, 9]
#iterable = [1, 3, 5, 7, 9]

# Alternative 1. Track position with an explicit index counter
'''
index = 0
every_other = []
for elem in iterable:
    if index%2 == 0:
        every_other.append(elem)
    index += 1



# Alternative 2. Use enumerate and get position information implicitly
every_other = []
for tuple in enumerate(iterable):
    position, elem = tuple
    if position%2 == 0:
        every_other.append(elem)
print(every_other)
'''

b = Board(args to make a board)
for row in b:
  for spot in row:
    do something with spot


#to iterate through instance of board and not through board class
for row in board:
    for spot in row:
        do something with spot
