#!/usr/bin/python

'''
Given a word from a wordlist, find one anagram with the most 
number of words (from the given wordlist) and one anagram with 
just two words in them (if one exists). If no anagrams exist 
with two or more words, the program should print an empty string 
for both cases.

Ignore single letter words

@author: Karan Goel
@email: karan@goel.im
'''

from collections import defaultdict

WORDLIST = 'words'


class LetterInventory:
	'''
	A class to help me count, add, and subtract letters from words and phrases.
	'''

	def __init__(self, s):
		'''
		constructs a letter inventory for the given string 
		'''
		self.inventory = defaultdict(int)
		for c in s:
			if c is not ' ':
				self.inventory[c] += 1

	def add(self, other):
		'''
		adds the letters of the given string to this one
		'''
		for c in other:
			self.inventory[c] += 1

	def __contains__(self, other):
		'''
		returns true if this inventory contains all letters at least as 
		many times as they appear in the given string
		'''
		other_dict = defaultdict(int)
		for c in other:
			other_dict[c] += 1
		for c in other_dict:
			if (c not in self.inventory or self.inventory[c] < other_dict[c]):
				return False
		return True

	def empty(self):
		'''
		returns true if the inventory contains no letters
		'''
		return len(self.inventory) == 0

	def __len__(self):
		'''
		returns the total number of letters in the inventory 
		'''
		return sum(self.inventory.values())

	def subtract(self, other):
		'''
		removes letters of the given string from this one; 
		throws Exception if not contained
		'''
		if other == None or not self.__contains__(other):
			raise Exception('Nopes, can\'t do it!')
		else:
			for c in other:
				self.inventory[c] -= 1

	def __str__(self):
		'''
		string version of inventory
		'''
		string = ''
		for c in self.inventory:
			string += (c * self.inventory[c])
		return string


def word_exists(user_word):
	'''
	Returns true if the given word exists in WORDLIST,
	false otherwise
	'''
	with open(WORDLIST) as f:
		for word in f:
			if user_word == word.lower().replace('\n', ''):
				return True
	return False

def get_words(user_word):
	'''
	Returns a list of all words that are a subset of passed
	signature.
	'''
	words = []
	inventory = LetterInventory(user_word)
	with open(WORDLIST) as f:
		for word in f:
			word = word.replace('\n', '')
			if len(word) > 1: # ignore single characters
				word = word.strip().lower() # trim and change to lower case
				if word in inventory:
					# this word is a possible candidate for being a part of anagram
					words.append(word)
	return words

def get_anagrams(user_word, anagram, words, inventory, all_anagrams):
	'''
	Finds all anagrams for the given user_word.
	'''
	if len(inventory) == 0:
		# nothing more to chose from
		all_anagrams.append(anagram)
	else:
		for choice in words:
			if len(choice) <= len(inventory) and choice in inventory:
				inventory.subtract(choice)
				get_anagrams(user_word, anagram + [choice], words, inventory, all_anagrams)
				inventory.add(choice)

def print_two_word(all_anagrams):
	'''
	Prints the sublist with exactly two elements.
	'''
	for anagram in all_anagrams:
		if len(anagram) == 2:
			print 'Two-word anagram: ' + ' '.join(anagram)
			return
	print 'No two-word anagram.'

def print_biggest_anagram(all_anagrams):
	'''
	Prints the biggest anagram in the given list of anagrams
	'''
	biggest = []
	for anagram in all_anagrams:
		if len(anagram) > len(biggest):
			biggest = anagram
	if biggest and len(biggest) > 2:
		print 'Biggest anagram: %s (%d words)' % (' '.join(biggest), len(biggest))
	else:
		print 'No anagram bigger than two words.'

def main():
	user_word = raw_input('Please enter one word from the word list: ')
	user_word = user_word.strip().lower() # force lower case

	if word_exists(user_word):
		words = get_words(user_word)
		inventory = LetterInventory(user_word)
		
		all_anagrams = [] # list to hold the anagrams
		get_anagrams(user_word, [], words, inventory, all_anagrams)
		
		print_two_word(all_anagrams)
		print_biggest_anagram(all_anagrams)

	else:
		print 'Please enter a word that exists in \'%s\' file' % WORDLIST

if __name__ == '__main__':
	main()
