print("Which expression will be longer?\n")

while True:
	a=(input("Please type your first expression: "))
	b=(input("Please type your second expression: "))
	
	if len(a) < len(b):
		print("Your second expression is longer than the first.")
		break
	if len(a) > len(b):
		print("Your first expression is longer than the second.")
		break
	else:
		print("The expressions are of equal length.")
		break
