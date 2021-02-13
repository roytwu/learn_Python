#* Platform:    Python 3
#* File name:   palindrome.py
#* Description: Tell if a word is palindrome or not

def first(word):
	return word[0] #return the first character in the string

def	last(word):
	return word[-1]  #return the last character in the string

def middle(word):
	return word[1:-1]



def verify(word):
	head = first(word)
	tail = last(word)
	if head == tail:
		word = middle(word)
		print(word)
		verify(word)
	else:
		print('Not a palindrome!')
		return -1
				

word = 'cabbac'
verify(word)