x = "There are %d types of people." % 10 # string using a format of character 
binary = "binary" # variable with string 
do_not = "don't" # variable with string
y = "Those who know %s and those who %s." % (binary, do_not) # a string using characters

print x # print the string of the variable 
print y # print the string of the variable 

print "I said: %r." % x # print the string, add other variable with 
						# string with character format
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a rigth side."

print w + e # we add two strings 