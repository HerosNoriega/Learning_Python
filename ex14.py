from sys import argv

script, user_name, developed = argv
prompt = '> '

print "Hi %s, I'm the %s script developed  in %s." % (user_name, script, developed)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
print ""
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kinf of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)