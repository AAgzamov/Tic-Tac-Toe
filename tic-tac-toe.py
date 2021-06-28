import os

# Informs that it is turn of 'X'.
def goes_x():

	print('Now it is turn for \'X\' to mark the space.')
	print('Choose where you want to mark the space.')

# Inform that it is turn of 'O'
def goes_o():
    
	print('Now it is turn for \'O\' to mark the space.')
	print('Choose where you want to mark the space.')

# This function prints out the game space.
def game():

	print('\n')
	print(a, b, c, sep = '   ', end = '\n\n')
	print(d, e, f, sep = '   ', end = '\n\n')
	print(g, h, i, sep = '   ', end = '\n\n')
	print('\n')

# Mark the space with 'X'.
def put_x(x):

	if x == 'a':
		if (a[0] != ' X ' and a[0] != ' O '):
			a.pop()
			a.append(' X ')
	elif x == 'b':
		if (b[0] != ' X ' and b[0] != ' O '):
			b.pop()
			b.append(' X ')
	elif x == 'c':
		if (c[0] != ' X ' and c[0] != ' O '):
			c.pop()
			c.append(' X ')
	elif x == 'd':
		if (d[0] != ' X ' and d[0] != ' O '):
			d.pop()
			d.append(' X ')
	elif x == 'e':
		if (e[0] != ' X ' and e[0] != ' O '):
			e.pop()
			e.append(' X ')
	elif x == 'f':
		if (f[0] != ' X ' and f[0] != ' O '):
			f.pop()
			f.append(' X ')
	elif x == 'g':
		if (g[0] != ' X ' and g[0] != ' O '):
			g.pop()
			g.append(' X ')
	elif x == 'h':
		if (h[0] != ' X ' and h[0] != ' O '):
			h.pop()
			h.append(' X ')
	elif x == 'i':
		if (i[0] != ' X ' and i[0] != ' O '):
			i.pop()
			i.append(' X ')

	return(a, b, c, d, e, f, g, h, i)

# Mark the space with 'O'.
def put_o(o):

	if o == 'a':
		if (a[0] != ' X ' and a[0] != ' O '):
			a.pop()
			a.append(' O ')          
	elif o == 'b':
		if (b[0] != ' X ' and b[0] != ' O '):
			b.pop()
			b.append(' O ')
	elif o == 'c':
		if (c[0] != ' X ' and c[0] != ' O '):
			c.pop()
			c.append(' O ')
	elif o == 'd':
		if (d[0] != ' X ' and d[0] != ' O '):
			d.pop()
			d.append(' O ')
	elif o == 'e':
		if (e[0] != ' X ' and e[0] != ' O '):
			e.pop()
			e.append(' O ')
	elif o == 'f':
		if (f[0] != ' X ' and f[0] != ' O '):
			f.pop()
			f.append(' O ')
	elif o == 'g':
		if (g[0] != ' X ' and g[0] != ' O '):
			g.pop()
			g.append(' O ')
	elif o == 'h':
		if (h[0] != ' X ' and h[0] != ' O '):
			h.pop()
			h.append(' O ')
	elif o == 'i':
		if (i[0] != ' X ' and i[0] != ' O '):
			i.pop()
			i.append(' O ')

	return a, b, c, d, e, f, g, h, i

# Check for the winner.
def check(winner):

    # Cheking for 'X'.
	if a[0]==' X ' and b[0]==' X ' and c[0]==' X ':
		winner = 'y'
		return winner
	elif a[0]==' X ' and e[0]==' X ' and i[0]==' X ':
		winner = 'y'
		return winner
	elif a[0]==' X ' and d[0]==' X ' and g[0]==' X ':
		winner = 'y'
		return winner

	elif b[0]==' X ' and e[0]==' X ' and h[0]==' X ':
		winner = 'y'
		return winner

	elif c[0]==' X ' and e[0]==' X ' and g[0]==' X ':
		winner = 'y'
		return winner
	elif c[0]==' X ' and f[0]==' X ' and i[0]==' X ':
		winner = 'y'
		return winner

	elif d[0]==' X ' and e[0]==' X ' and f[0]==' X ':
		winner = 'y'
		return winner

	elif g[0]==' X ' and h[0]==' X ' and i[0]==' X ':
		winner = 'y'
		return winner

    # Checking for 'O'.
	if a[0]==' O ' and b[0]==' O ' and c[0]==' O ':
		winner = 'y'
		return winner
	elif a[0]==' O ' and e[0]==' O ' and i[0]==' O ':
		winner = 'y'
		return winner
	elif a[0]==' O ' and d[0]==' O ' and g[0]==' O ':
		winner = 'y'
		return winner

	elif b[0]==' O ' and e[0]==' O ' and h[0]==' O ':
		winner = 'y'
		return winner

	elif c[0]==' O ' and e[0]==' O ' and g[0]==' O ':
		winner = 'y'
		return winner
	elif c[0]==' O ' and f[0]==' O ' and i[0]==' O ':
		winner = 'y'
		return winner

	elif d[0]==' O ' and e[0]==' O ' and f[0]==' O ':
		winner = 'y'
		return winner

	elif g[0]==' O ' and h[0]==' O ' and i[0]==' O ':
		winner = 'y'
		return winner

	# Checking for a draw.
	elif ((a[0]==' X ' or a[0]==' O ') and (b[0]==' X ' or b[0]==' O ') and (c[0]==' X ' or c[0]==' O ') and (d[0]==' X ' or d[0]==' O ') and (e[0]==' X ' or e[0]==' O ') and (f[0]==' X ' or f[0]==' O ') and (g[0]==' X ' or g[0]==' O ') and (h[0]==' X ' or h[0]==' O ') and (i[0]==' X ' or i[0]==' O ')):
		winner = 'd'
		return winner
    
	return 'n'

# Clean screen (for Unix-based Operating Systems).
def clear():
	os.system('clear')

while 1: # Main game loop.
	
	clear()

	# Rows and columns
	a = [' a ']
	b = [' b ']
	c = [' c ']
	d = [' d ']
	e = [' e ']
	f = [' f ']
	g = [' g ']
	h = [' h ']
	i = [' i ']

	turn_x = True # Setting turn for 'X'.
	err = False # No twice the same marked space.
	marked_values = list()
	winner = 'n' # No winner yet.
	again = 'n' # Variable for asking if players want to play again or otherwise.

	print('\'X\' goes firts.')

	while 1: # Start game loop.

		game()

		if turn_x == True:
			goes_x() # Turn of 'X'.

			x = str(input()) # Taking an input for 'X'.
			x = x.lower() # Lowering case of the input value of 'X'.

        	# Checking for the space availability.
			for index in range(len(marked_values)):
				if x == marked_values[index]:
					print('\n[Error]: The space is already marked! Choose another space.\n')
					err = True
					break
				elif x != marked_values[index]:
					err = False

			if err == True:
				continue
			elif err == False:
				pass

        	# Adding already marked values to the list.
			marked_values.append(x)

        	# Marking the space with 'X'.
			put_x(x)

			check(winner)
			if 'y' == check(winner):
				game()
				print('\'X\' is a winner!\n')
				again = input('Do you want to play again (y/n)?: ')
				again = again.lower()
				if again == 'y':
					break
				elif again == 'n':
					break
			elif 'd' == check(winner):
				game()
				print('Draw!\n')
				again = input('Do you want to play again (y/n)?: ')
				again = again.lower()
				if again == 'y':
					break
				elif again == 'n':
					break

			turn_x = False
			clear()
        
		elif turn_x == False:
    
			goes_o() # Turn of 'O'.
    
			o = str(input()) # Taking an input for 'O'.
			o = o.lower() # Lowering case of the input value of 'O'.

        	# Checking for the space availability.
			for index in range(len(marked_values)):
				if o == marked_values[index]:
					print('\n[Error]: The space is already marked! Chose another space.\n')
					err = True
					break
				elif o != marked_values[index]:
					err = False

			if err == True:
				continue
			elif err == False:
				pass

        	# Adding already marked values to the list.
			marked_values.append(o)

        	# Marking the space with 'O'.
			put_o(o)
        
			if 'y' == check(winner):
				game()
				print('\'O\' is a winner!\n')
				again = input('Do you want to play again (y/n)?: ')
				again = again.lower()
				if again == 'y':
					break
				elif again == 'n':
					break
			elif 'd' == check(winner):
				game()
				print('Draw!\n')
				again = input('Do you want to play again (y/n)?: ')
				again = again.lower()
				if again == 'y':
					break
				elif again == 'n':
					break

			turn_x = True
			clear()

	if again == 'y':
		continue
	elif again == 'n':
		break

input()
