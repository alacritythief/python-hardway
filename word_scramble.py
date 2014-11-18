print "Word Scrambler!"
word = raw_input("Enter your word: ")

word_array = list(word)

print "Scrambling it up!"

reversed_word = []

for character in reversed(word_array):
    reversed_word.append(character)

print "Your reversed word: " + ''.join(reversed_word)
