#this is like the script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#the *args is atually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %r"% arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Carol", "Balos")
print_two_again("Carol", "Balos")
print_one("First!")
print_none()
