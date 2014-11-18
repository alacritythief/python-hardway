print "This is a test of the emergency broadcast system"
print "This is only a test!"

test_string = "this string variable"
test_number = 52

print "I am embedding %s!" % test_string
print "Let's play %d card pickup!" % test_number

print "I don't think there are less than %d characters in %s." % (test_number, test_string)

print "Concatenating " + "all " + "the " + "things!"

word_format = "%r %r %r %r %r"

print word_format % ("Here", "is", "some", "text", "yo")
print word_format % (1, 2, 3, 4, 5)
