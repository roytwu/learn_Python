#* Platform:    Python3
#* file name:   palindrome2.py
#* Date:        04/26/2018 Roy
#* Description: Tell if a word is palindrome or not


def is_palindrome(word):
	i=0
	j = len(word)-1

	while i<j:
		if word[i] != word[j]:
			print('Not a Palindrome!')
			return False
		i= i+1
		j= j-1

	return True

word = 'noon'
is_palindrome(word)